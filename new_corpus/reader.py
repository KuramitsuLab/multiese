from nis import maps
import re
import pegtree as pg

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

W = '([^A-Za-z0-9])'
てにをは = r'([はがとをのに\[])'

VARPAT = re.compile(W+r'([a-z][a-z]?\d?)'+てにをは)

PATTERNS = [
    (re.compile(W+r'(s\d?)'+てにをは), r'\1文字列\2\3'),
    (re.compile(W+r'(ch\d?)'+てにをは), r'\1文字\2\3'),
    (re.compile(W+r'(df\d?)'+てにをは), r'\1データフレーム\2\3'),
    (re.compile(W+r'(ds\d?)'+てにをは), r'\1データシリーズ\2\3'),
    (re.compile(W+r'(value\d?)'+てにをは), r'\1[|文字列|リスト]\2\3'),

    #(re.compile(W+r'([xy]\d?)'+てにをは), r'\1[整数|浮動少数点数]\2\3'),
]

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
                settings['option'][name]=argument
        else:
            ss.append(line)
    return ss

def replace_with_rules(s, altdic):
    s = ' '+ s # 正規表現の都合
    for old, new in PATTERNS:
        s = re.sub(old, new, s)
    for old, new in altdic.items():
        if old in s:
            print('=>', old, new)
            s = s.replace(old, new)
    return s[1:]

def augment_doc(code, docs, altdic):
    docs2=[]
    for i, doc in enumerate(docs):
        if doc.endswith('に変換する'):
            doc = doc.replace('に変換する', 'に[変換|]する')
        doc = replace_with_rules(doc, altdic)
        docs2.append(doc)
    return code, docs2

def scaleXY(ss, code, docs, settings):
    option = settings['option']
    altdic = settings['alt']
    if '__X__' not in code:
        code, docs = augment_doc(code, docs, altdic)
        ss.append((code, tuple(docs), option))
        return
    for x, y in zip(settings['X'], settings['Y']):
        codeX = code.replace('__X__', x)
        docYs = [doc.replace('__Y__', y) for doc in docs]
        codeX, docYs = augment_doc(codeX, docYs, altdic)
        print(codeX, docYs)
        ss.append((codeX, tuple(docYs), option))

def read_corpus(filename):
    ss=[]
    settings = { 'alt': {} }
    with open(filename) as f:
        tree = parse_as_tree(f.read())
        for t in tree:
            code = str(t[0]).strip()
            docs = str(t[1]).splitlines()
            docs = read_settings(docs, settings)
            scaleXY(ss, code, docs, settings)
            #print(code, docs)
            ##ss.append((code, tuple(docs)))
    return ss

read_corpus('_pandas.py')