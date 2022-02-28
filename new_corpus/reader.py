import re
import csv
import sys
import pegtree as pg

from naming import type_augmentation
from testing import test_code
from parse import multiese_da, encode_text_code

# naming


GRAMMAR = '''

Sentense = { (Block / . )* }

Block = {
    { (!LF .)+ #Code } LF
    QUOTE LF
    { (!QUOTE (!LF .)* LF)+ #Doc }
    QUOTE LF
    #Pair
}

QUOTE = '\\'\\'\\'' _ / '"""' _
LF = '\\r'? '\\n' / !.

'''

parse_as_tree = pg.generate(pg.grammar(GRAMMAR))

# prefix

BEGIN = '([^A-Za-z0-9]|^)'
END = ('(?![A-Za-z0-9]|$)')
VARPAT = re.compile(BEGIN+r'([a-z]+)(\d?)'+END)

PREFIX = {
    's': ('文字列', ''),
    'iterable': ('[[リスト|タプル|配列]|列|イテラブル|]', ''),
    'element': ('[文字列|オブジェクト|]', ''),
    'obj': ('[オブジェクト|]', ''),
    # 'alist': ('リスト', ''),
    # 'atuple': ('タプル', ''),
    # 'adict': ('辞書', ''),

    # 'aset': ('セット', ''),
    # 'key': ('[キー|]', ''),
    # 'filename': ('[ファイル[名|パス]|文字列]', ''),
    # 'df': ('データフレーム', ''),
    # 'args': ('引数[|列|リスト]', ''),
    # 'colname': ('', '[行|カラム]'),
}


def _ta(name, number, prefixdic):
    prefix, suffix = prefixdic.get(name, ('', ''))
    if prefix == '' and suffix == '':
        if name.endswith('func'):
            prefix = '関数'
    return f'{name}{number}', f'{prefix}{name}{number}{suffix}'


def type_augmentation(doc, prefixdic):
    names = [_ta(x[1], x[2], prefixdic) for x in VARPAT.findall(doc)]
    doc = re.sub(VARPAT, r'\1@\2\3@', doc)  # @s@
    for old, new in names:
        if old != new:
            doc = doc.replace(f'@{old}@', new)
    return doc.replace('@', '')


def _split(s):
    if ',' in s and '|' not in s:
        return [x.strip() for x in s.split(',')]
    if ';' in s:
        return s.split(';')
    return s.split('|')


def read_settings(docs, settings):
    ss = []
    settings['option'] = {}
    for line in docs:
        if line.startswith('@'):
            name, _, argument = line.strip().partition('(')
            if argument.endswith(')'):
                argument = argument[:-1]
            if name == '@alt':
                key, _, _ = argument.partition('|')
                argument = argument.replace('_', '')
                settings['alt'][key] = f'[{argument}]'
            elif name == '@X':
                settings['X'] = _split(argument)
            elif name == '@Y':
                settings['Y'] = _split(argument)
            elif name == '@prefix':
                t = _split(argument)
                if len(t) == 2:
                    t.append('')
                settings['prefix'][t[0]] = tuple(t[1:])
                print('@', settings['prefix'])
            else:
                settings['option'][name] = argument
        else:
            if line.count('[') != line.count(']') or line.count('{') != line.count('}'):
                print('SyntaxError:', line)
            ss.append(line)
    return ss


def replace_with_rules(s, altdic, prefixdic):
    s = type_augmentation(s, prefixdic)
    for old, new in altdic.items():
        if old in s:
            #print('=>', old, new)
            s = s.replace(old, new)
    return s


def augment_doc(code, docs, altdic, prefixdic):
    docs2 = []
    for i, doc in enumerate(docs):
        doc = replace_with_rules(doc, altdic, prefixdic)
        docs2.append(doc)
    return code, docs2


ANDTHEN = [
    ('読み込む', '読み込[んで|み、]'),
    ('読む', '読[んで|み、]'),
]


def make_letdoc(doc):
    found = False
    for old, new in ANDTHEN:
        if old in doc:
            doc = doc.replace(old, new)
            found = True
    return doc + 'X[に|と]する' if found else None


def make_triple(ss, code, docs, settings):
    option = settings['option']
    altdic = settings['alt']
    prefixdic = settings['prefix']
    code, docs = augment_doc(code, docs, altdic, prefixdic)
    test_with = option.get('@test', '_')
    result = test_code(code, test_with)
    for doc in docs:
        text = multiese_da(doc)
        ss.append((code, text, doc, test_with, result))
        print(encode_text_code(doc, code))
        if '@test_let' in option:
            doc = make_letdoc(doc)
            if doc is not None:
                test_with = option['@test_let']
                result = test_code(code, test_with)
                ss.append((f'X = {code}', multiese_da(
                    doc), doc, test_with, result))
                print(f'[LET] X = {code}', doc, test_with, result)


def scaleXY(ss, code, docs, settings):
    if '__X__' not in code:
        make_triple(ss, code, docs, settings)
        return
    for x, y in zip(settings['X'], settings['Y']):
        codeX = code.replace('__X__', x)
        docYs = [doc.replace('__Y__', y) for doc in docs]
        make_triple(ss, codeX, docYs, settings)


def new_altdic():
    return {
        'に変換する': 'に[変換|]する',
        'が_': '[が|は]',
        'で_': '[で|として|を[用いて|使って]]',
        'の中': '[|の[中|内]]',
        '一つ': '[ひとつ|一つ]', '二つ': '[ふたつ|二つ]',
        '１': '[一|１|1]', '２': '[二|２|2]', '３': '[三|３|3]',
        'かどうか': '[か[|どうか][調べる||[確認|判定|テスト]する]|]',
        '、': '[、|]',
        '求める': '[求める|計算する|算出する]',
        '見る': '[見る|確認する|調べる]',
        '使う': '[使う|[使用する|用いる]]',
        'プリントする': '[表示する|出力する|プリントする]',
        'コピーする': '[コピーする|複製する]'
    }


def read_corpus(filename):
    ss = []
    settings = {'alt': new_altdic(), 'prefix': PREFIX.copy()}
    with open(filename) as f:
        tree = parse_as_tree(f.read())
        for t in tree:
            code = str(t[0]).strip()
            docs = str(t[1]).splitlines()
            docs = read_settings(docs, settings)
            scaleXY(ss, code, docs, settings)
    return ss


def main():
    tuples = []
    for file in sys.argv[1:]:
        tuples.extend(read_corpus(file))
    with open('new_corpus.tsv', 'w') as f:
        f = csv.writer(f, delimiter="\t")
        for tuple in tuples:
            f.writerow(tuple)


if __name__ == '__main__':
    main()