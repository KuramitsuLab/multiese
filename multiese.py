from audioop import mul
import re
import csv
import sys
import pegtree as pg
import random
from multiese_da import multiese_da

##
# Multiese Parser

GRAMMAR = '''

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

parse_as_tree = pg.generate(pg.grammar(GRAMMAR))


# Document Settings

PREFIX = {
    's': ('文字列', ''),
    'element': ('[文字列|オブジェクト|]', ''),
    'obj': ('[オブジェクト|]', ''),
    'alist': ('リスト', ''),
    'atuple': ('タプル', ''),
    'aset': ('セット', ''),
    'adict': ('辞書', ''),
    'ty': ('型', '型'),
    'fin': ('[ファイル[入力|]|入力[|ストリーム]]', ''),
    'fout': ('[ファイル[出力|]|出力[|ストリーム]]', ''),
    'iterable': ('[[リスト|タプル|配列]|列|イテラブル|]', ''),
}

ALTDIC = {
    '\n': '<NL>',
    'に変換する': 'に[変換|]する',
    'に設定する': '[に設定する|に変更する|に[セット|指定]する|にする]',
    'に代入する': '[に[代入|]する|とする]',
    'が_': '[が|は]',
    'で_': '[で|として|を[用いて|使って]]',
    'の中の': '[[|の][中|内]の|の]', 'の中に': '[[|の][中|内]に|に]', '中で': '[[の|][中|内]で|で]',
    '全ての': '[全ての|すべての|全|]',
    'の名前': '[名|の名前]',
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
}


# auto_augmentation

BEGIN = '([^A-Za-z0-9]|^)'
END = ('(?![A-Za-z0-9]|$)')
VARPAT = re.compile(BEGIN+r'([A-Za-z][A-Za-z_]+)(\d?)'+END)


def _ta(name, number, prefixdic):
    prefix, suffix = prefixdic.get(name, ('', ''))
    if prefix == '' and suffix == '':
        if name.endswith('func'):
            prefix = '関数'
            suffix = '関数'
    if '|' not in prefix:
        prefix = f'[{prefix}|]'
    if suffix != '' and '|' not in suffix:
        suffix = f'[{suffix}|]'
    var = f'{name}{number}'
    if suffix == '':
        return var, f'{prefix}{var}'
    return var, f'[{prefix}{var}|{var}{suffix}]'


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
                self.make_pair(codeX, [doc.replace('__Y__', y)
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
            self.altDic[key] = argument
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
                for _ in range(max_iter):
                    doc2 = multiese_da(doc, choice=0.99, shuffle=shuffle)
                    if doc0 != doc2:
                        train_test_data.add(doc2)
                train_test_data = list(train_test_data)
                if len(train_test_data) > 2:
                    random.shuffle(train_test_data)
                    for doc in train_test_data[:-1]:
                        self.train_data.append((doc, code))
                    self.test_data.append((train_test_data[-1], code))
                else:
                    for doc in train_test_data[:-1]:
                        self.train_data.append((doc, code))

    def save_data(self, filename='kogi.tsv'):
        if len(self.test_data) == 0:
            random.shuffle(self.train_data)
            train_size = (len(self.train_data) * 7) // 10
            self.test_data = self.train_data[train_size:]
            self.train_data = self.train_data[:train_size]
        filename = filename.replace('.tsv', '_train.tsv')
        with open(filename, 'w') as f:
            writter = csv.writer(f, delimiter="\t")
            for row in self.train_data:
                writter.writerow(row)
        filename = filename.replace('_train.tsv', '_test.tsv')
        with open(filename, 'w') as f:
            writter = csv.writer(f, delimiter="\t")
            for row in self.test_data:
                writter.writerow(row)


def main_small():
    corpus = Corpus()
    for filename in sys.argv[1:]:
        corpus.read(filename, multi=False)
    corpus.generate(max_iter=0)
    corpus.save_data('kogi0.tsv')


def main(max_iter=5):
    corpus = Corpus()
    for filename in sys.argv[1:]:
        corpus.read(filename)
    corpus.generate(max_iter=max_iter)
    corpus.save_data(f'kogi{max_iter}.tsv')


if __name__ == '__main__':
    main(6)
