from audioop import mul
import re
import csv
import sys
import pegtree as pg
import random
from multiese_da import multiese_da

##
# Multiese Parser

GRAMMAR0 = '''

Sentense = { (Block / . )* }

// { (!LF .)+ #Code } LF

Code = {
    (!LF .)+ (LF [ \t]+ (!LF .)+ )* #Code
}

Block = {
    Code LF
    QUOTE LF
    { (!QUOTE (!LF .)* LF)+ #Doc }
    QUOTE LF
    #Pair
}

QUOTE = '\\'\\'\\'' _ / '"""' _
LF = '\\r'? '\\n' / !.

'''

GRAMMAR = '''

Sentense = { (Block / . )* }

Code = {
    (!QUOTE (!LF .)+ LF)+ #Code
}

Block = {
    Code
    QUOTE LF
    { (!QUOTE (!LF .)* LF)+ #Doc }
    QUOTE LF
    #Pair
}

QUOTE = '\\'\\'\\'' _ / '"""' _
LF = '\\r'? '\\n' / !.

'''

parse_as_tree = pg.generate(pg.grammar(GRAMMAR))


# Document Settings

PREFIX = {
    's': ('文字列', ''),
    'obj': ('[オブジェクト]', ''),
    'element': ('[文字列|オブジェクト]', ''),
    'aArray': ('配列', ''),
    'aList': ('リスト', ''),
    'aTuple': ('[タプル|組]', ''),
    'aSet': ('[セット|集合]', ''),
    'aDict': ('[辞書|マッピング|タプル]', ''),
    'df': ('[データフレーム|表データ]', ''),
    'col': ('', '[列|カラム]'),
    'column': ('', '[列|カラム]'),
    'ds': ('データ列', ''),
    'ty': ('', '型'),
    'fin': ('[ファイル[入力|]|入力[|ストリーム]]', ''),
    'fout': ('[ファイル[出力|]|出力[|ストリーム]]', ''),
    'iterable': ('[イテラブル|列|シーケンス|[リスト|タプル|配列]]', ''),
}

ALTDIC = {
    '\n': '<nl>',
    '変換する': '[変換|]する',
    '設定する': '[設定する|[指定|セット|]する|変更する]',
    'に代入する': '[に[代入|]する|とする]',
    #    'が_': '[が|は]',
    'で_': '[で|として|を[用いて|使って]]',
    # 'の中の': '[[|の][中|内]の|の]', 'の中に': '[[|の][中|内]に|に]', '中で': '[[の|][中|内]で|で]',
    '全ての': '[全ての|すべての|全|]',
    'の名前': '[名|の名前]',
    '指定した': '[指定した|指定された|ある]',
    'された': '[された|された|した]',
    'まとめて': '[まとめて|一度に|]',
    '一つ': '[ひとつ|一つ]', '二つ': '[ふたつ|二つ]',
    '１': '[一|１|1]', '２': '[二|２|2]', '３': '[三|３|3]',
    'かどうか': '[か[|どうか][調べる||[確認|判定|テスト]する]|]',
    '、': '[、|]',
    '求める': '[求める|計算する|算出する]',
    '見る': '[見る|確認する|調べる]',
    '使う': '[使う|用いる|使用する]',
    '得る': '[使う|見る|求める]',
    '新たに': '[新しく|新たに|]',
    '作る': '[[作る|作成する]|[|新規]生成する|[用意|準備]する]',
    '作って': '[[作って|作成して]|[|新規]生成して|[用意|準備]して]',
    'プリントする': '[表示する|出力する|プリントする]',
    'コピーする': '[コピーする|複製する]',
    'が欲しい': '[が[欲|ほ]しい|]',
}

VERB = [
    ('する', 'して', 'し'),
    ('させる', 'させて', 'させ'),

    ('作る', '作って', '作り'),
    ('使う', '使って', '使い'),
    ('見る', '見て', '見'),
    ('得る', '得て', '得'),
    ('求める', '求めて', '求め'),
    ('変える', '変えて', '変え'),
    ('替える', '替えて', '替え'),
    ('換える', '換えて', '換え'),
    ('分ける', '分けて', '分け'),
    ('並べる', '並べて', '並べ'),
    ('調べる', '調べて', '調べ'),
    ('入れる', '入れて', '入れ'),

    ('まとめる', 'まとめて', 'まとめ'),
    ('付ける', '付けて', '付け'),
    ('つける', 'つけて', 'つけ'),
    ('止める', '止めて', '止め'),
    ('終える', '終えて', '終え'),
    ('加える', '加えて', '加え'),
    ('数える', '数えて', '数え'),
    ('閉じる', '閉じて', '閉じ'),

    ('開く', '開いて', '開き'),
    ('除く', '除いて', '除き'),
    ('描く', '描いて', '描き'),
    ('書く', '書いて', '書き'),
    ('引く', '引いて', '引き'),
    ('出す', '出して', '出し'),
    ('残す', '残して', '残し'),
    ('消す', '消して', '消し'),
    ('増やす', '増やして', '増やし'),
    ('減らす', '減らして', '減らし'),
    ('直す', '直して', '直し'),
    ('足す', '足して', '足し'),

    ('切る', '切って', '切り'),
    ('読む', '読んで', '読み'),
    ('込む', '込んで', '込み'),
    ('積む', '積んで', '積み'),
    ('選ぶ', '選んで', '選び'),
]


def verb_then(verb, alt_form=False):
    for suffix, then, then2 in VERB:
        if verb.endswith(suffix):
            then = verb.replace(suffix, then)
            if alt_form:
                then2 = verb.replace(suffix, then2)
                return f'[{then}|{then2}]'
            return then
    return None


def alter_all_verb_then(s):
    alt = 0
    for verb, then, then2 in VERB:
        if verb in s:
            alt += 1
            s = s.replace(verb, f'[{then}|{then2}、]')
    if alt == 0:
        print('NON', verb)
    return s


def append_altdic(altdic, key, value):
    altdic[key] = value
    then = verb_then(key)
    if then is not None:
        value = alter_all_verb_then(value)
        #print('altDic', then, value)
        altdic[then] = value

# auto_augmentation


BEGIN = '([^A-Za-z0-9]|^)'
END = ('(?![A-Za-z0-9]|$)')
VARPAT = re.compile(BEGIN+r'([A-Za-z][A-Za-z_]*)(\d?)'+END)


def _ta(name, number, prefixdic):
    prefix, suffix = prefixdic.get(name, ('', ''))
    if prefix == '' and suffix == '':
        if name.endswith('func'):
            prefix = '関数'
            suffix = '関数'
    var = f'{name}{number}'
    if suffix != '':
        if prefix != '':
            return var, f'[{prefix}|{suffix}]'
        return var, f'{suffix}'
    if prefix != '':
        return var, f'{prefix}'
    return var, var


def _split(s):
    if ';' in s:
        return s.split(';')
    if ',' in s and '|' not in s:
        return [x.strip() for x in s.split(',')]
    return s.split('|')


class Corpus(object):
    def __init__(self):
        self.corpus = []
        self.prefixDic = {}
        self.altDic = {}

    def extend_type(self, doc):
        names = [_ta(x[1], x[2], self.prefixDic)
                 for x in VARPAT.findall(doc + ' ')]
        doc = re.sub(VARPAT, r'\1@\2\3@', doc + ' ')  # @s@
        for old, new in names:
            if old != new:
                doc = doc.replace(f'@{old}@', new)
        return doc.replace('@', '').strip()

    def extend_alt(self, doc):
        doc = self.extend_type(doc)
        for old, new in self.altDic.items():
            if old in doc:
                #print('=>', old, new)
                doc = doc.replace(old, new)
        return doc

    def make_pair(self, code, docs):
        self.corpus.append((code, [self.extend_alt(doc) for doc in docs]))

    def multiplex(self, code, docs, multi=True):
        if '__X__' in code:
            for x, y in zip(self.X, self.Y):
                codeX = code.replace('__X__', x)
                self.make_pair(codeX, [doc.replace('__X__', '__Y__').replace('__Y__', y)
                                       for doc in docs])
                if multi == False:
                    break
        else:
            self.make_pair(code, docs)

    def parse_argument(self, name, argument):
        if name == '@alt':
            if '=' in argument:
                key, _, argument = argument.partition('=')
            else:  # old-style
                key, _, other = argument.partition('|')
                if key in other:
                    argument = other
                argument = argument.replace('_', '')
            if not argument.startswith('['):
                argument = f'[{argument}]'
            #self.altDic[key] = argument
            append_altdic(self.altDic, key, argument)
        elif name == '@prefix':
            t = _split(argument)
            if len(t) == 2:
                t.append('')
            self.prefixDic[t[0]] = tuple(t[1:])
        elif name == '@X':
            self.X = _split(argument)
        elif name == '@Y':
            self.Y = _split(argument)

    def parse_settings(self, docs):
        ss = []
        for line in docs:
            line = line.strip()
            if line.startswith('@'):
                name, _, argument = line.strip().partition('(')
                if argument.endswith(')'):
                    argument = argument[:-1]
                self.parse_argument(name, argument)
            elif len(line) > 0:
                if line.count('[') != line.count(']') or line.count('{') != line.count('}'):
                    print(f'SyntaxError({self.reading_filename}):', line)
                ss.append(line)
        return ss

    def read(self, filename, multi=True):
        #settings = {'alt': new_altdic(), 'prefix': PREFIX.copy()}
        self.altDic = ALTDIC.copy()
        # print(self.altDic)
        self.prefixDic = PREFIX.copy()
        self.reading_filename = filename
        with open(filename) as f:
            tree = parse_as_tree(f.read())
            for t in tree:
                code = str(t[0]).strip()
                docs = self.parse_settings(str(t[1]).splitlines())
                self.multiplex(code, docs, multi=multi)

    def generate(self, max_iter=4, shuffle=0.5):
        self.train_data = []
        self.test_data = []
        for code, docs in self.corpus:
            for doc in docs:
                train_test_data = set()
                doc0 = multiese_da(doc, choice=0.0, shuffle=0.0)
                self.train_data.append((doc0, code))
                _choice = 0.7
                _shuffle = 0.3
                for _ in range((max_iter*2)+1):
                    doc2 = multiese_da(doc, choice=_choice, shuffle=_shuffle)
                    _choice = min(_choice + 0.03, 0.999)
                    _shuffle = _shuffle + 0.2
                    if _shuffle > 0.95:
                        _shuffle = 0.2
                    if doc0 != doc2:
                        train_test_data.add(doc2)
                train_test_data = list(train_test_data)
                for doc in train_test_data:
                    self.test_data.append((doc, code))
        random.shuffle(self.test_data)
        n_train = len(self.train_data)
        n_test = len(self.test_data)
        if max_iter == 0:
            return
        n_train2 = (n_train + n_test) * 8 // 10
        if n_train2 > n_train:
            diff = n_train2-n_train
            self.train_data = self.train_data + self.test_data[:diff]
            self.test_data = self.test_data[diff:]
        random.shuffle(self.train_data)
        print(n_train, n_test, len(self.train_data), len(self.test_data))

    def check(self, intent, code):
        if '{' in intent or '[' in intent or '_' in intent:
            print(f'\033[33m エラー{(intent, code)}\033[0m')
        if intent.startswith('option:') or intent.startswith('keyword:'):
            intent = intent.replace(':', ': ')
        return intent, code.replace('\n', '<nl>').replace('    ', '<tab>')

    def save_data(self, filename='kogi.tsv'):
        if len(self.test_data) == 0:
            random.shuffle(self.train_data)
            train_size = (len(self.train_data) * 7) // 10
            self.test_data = self.train_data[train_size:]
            self.train_data = self.train_data[:train_size]
        else:
            random.shuffle(self.train_data)
            random.shuffle(self.test_data)
        filename = filename.replace('.tsv', '_train.tsv')
        with open(filename, 'w') as f:
            writter = csv.writer(f, delimiter="\t")
            for intent, code in self.train_data:
                intent, code = self.check(intent, code)
                if '\n' not in code:
                    writter.writerow((intent, code))
        filename = filename.replace('_train.tsv', '_test.tsv')
        with open(filename, 'w') as f:
            writter = csv.writer(f, delimiter="\t")
            for intent, code in self.test_data:
                intent, code = self.check(intent, code)
                if '\n' not in code:
                    writter.writerow((intent, code))


def main_small():
    corpus = Corpus()
    for filename in sys.argv[1:]:
        corpus.read(filename, multi=False)
    corpus.generate(max_iter=0)
    corpus.save_data('kogi0.tsv')


def main():
    corpus = Corpus()
    for filename in sys.argv[1:]:
        corpus.read(filename)
    if len(sys.argv) == 2:
        corpus.generate(max_iter=10)
        name = sys.argv[1].replace('.py', '').replace('/', '')
        print(f'test debug_{name}.tsv')
        corpus.save_data(f'debug_{name}.tsv')
    else:
        for i in [0, 1, 2, 3, 5]:
            print(f'codegen{i}.tsv')
            corpus.generate(max_iter=i)
            corpus.save_data(f'codegen{i}.tsv')


if __name__ == '__main__':
    main()
