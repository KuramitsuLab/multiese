import csv
import sys
from nis import maps
import re
import itertools
import pegtree as pg

from naming import type_augmentation
from testing import test_code
from parse import multiese_da

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
                settings['X'] = argument.split('|')
            elif name == '@Y':
                settings['Y'] = argument.split('|')
            else:
                settings['option'][name] = argument
        else:
            if line.count('[') != line.count(']'):
                print('syntax error', line)
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
    code, docs = augment_doc(code, docs, altdic)
    test_with = option.get('@test_with', '_')
    result = test_code(code, test_with)
    for doc in docs:
        ss.append((code, multiese_da(doc), doc, test_with, result))
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
        'かどうか': '[|か[|どうか][|確認する|調べる|判定する|テストする]',
        '求める': '[求める|計算する|算出する|得る]',
        '見る': '[見る|確認する|調べる|得る]',
        '使う': '[使う|[使用する|用いる]]',
        'プリントする': '[表示する|出力する|プリントする]'
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
    tuples = []
    for file in sys.argv[1:]:
        tuples.extend(read_corpus(file))
    with open('new_corpus.tsv', 'w') as f:
        f = csv.writer(f, delimiter="\t")
        for tuple in tuples:
            f.writerow(tuple)


if __name__ == '__main__':
    main()
