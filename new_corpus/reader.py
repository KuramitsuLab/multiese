import sys
from nis import maps
import re
import itertools
import pegtree as pg

from naming import type_augmentation, test_code

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


# PATTERNS = [
#     (re.compile(BEGIN+r'(s\d?)'+END), r'\1文字列\2'),
#     (re.compile(BEGIN+r'(iterable\d?)'+END), r'\1[イテラブル|リスト|タプル|[配|データ|]列]\2'),
#     (re.compile(BEGIN+r'(mapping\d?)'+END), r'\1[マッピング|辞書]\2'),
#     (re.compile(BEGIN+r'(func\d?)'+END), r'\1関数\2'),
#     (re.compile(BEGIN+r'(df\d?)'+END), r'\1データフレーム\2'),
#     (re.compile(BEGIN+r'(ds\d?)'+END), r'\1データ列\2'),
#     (re.compile(BEGIN+r'(value\d?)'+END), r'\1[|文字列|リスト]\2'),
# ]


def read_settings(docs, settings):
    ss = []
    settings['option'] = {}
    for line in docs:
        if line.startswith('@'):
            name, sep, argument = line.strip().partition('(')
            if argument.endswith(')'):
                argument = argument[:-1]
            if name == '@alt':
                key, _, _ = argument.partition('|')
                argument = argument.replace('_', '')
                settings['alt'][key] = f'[{argument}]'
            elif name == '@X':
                settings['X'] = argument.split('|')
            elif name == '@Y':
                settings['Y'] = argument.split('|')
            else:
                settings['option'][name] = argument
        else:
            ss.append(line)
    return ss


def replace_with_rules(s, altdic):
    s = type_augmentation(s)
    for old, new in altdic.items():
        if old in s:
            #print('=>', old, new)
            s = s.replace(old, new)
    return s


def augment_doc(code, docs, altdic):
    docs2 = []
    for i, doc in enumerate(docs):
        doc = replace_with_rules(doc, altdic)
        docs2.append(doc)
    return code, docs2


def make_triple(ss, code, docs, settings):
    option = settings['option']
    altdic = settings['alt']
    code, docs = augment_doc(code, docs, altdic)
    test_with = option.get('@test_with', '_')
    result = test_code(code, test_with)
    for doc in docs:
        ss.append((code, doc, test_with, result))


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
        'かどうか': '[|か[|どうか]|とき|ならば]',
        '求める': '[求める|計算する|算出する|得る]',
        '見る': '[見る|確認する|調べる|得る]',
    }


def read_corpus(filename):
    ss = []
    settings = {'alt': new_altdic()}
    with open(filename) as f:
        tree = parse_as_tree(f.read())
        for t in tree:
            code = str(t[0]).strip()
            docs = str(t[1]).splitlines()
            docs = read_settings(docs, settings)
            scaleXY(ss, code, docs, settings)
    return ss


def main():
    ss = []
    for file in sys.argv[1:]:
        ss.extend(read_corpus(file))
    for s in ss:
        print(s)


if __name__ == '__main__':
    main()
