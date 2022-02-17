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

PATTERNS = [
    (re.compile(W+r'(s\d?)'+てにをは), r'\1文字列\2\3'),
    (re.compile(W+r'(ch\d?)'+てにをは), r'\1文字\2\3'),
    (re.compile(W+r'([xy]\d?)'+てにをは), r'\1[整数|浮動少数点数]\2\3'),
]

STATIC_MAPS = [
    ('片仮名', '[片仮名|カタカナ]'),
    ('平仮名', '[平仮名|ひらがな]')
]

def replace_with_rules(s):
    s = ' '+ s # 正規表現の都合
    for old, new in PATTERNS:
        s = re.sub(old, new, s)
    for old, new in STATIC_MAPS:
        s = s.replace(old, new)
    return s[1:]

def augment_doc(code, docs):
    docs2=[]
    for i, doc in enumerate(docs):
        if doc.endswith('に変換する'):
            doc = doc.replace('に変換する', 'に[変換|]する')
        doc = replace_with_rules(doc)
        docs2.append(doc)
    return code, docs2

def read_corpus(filename):
    ss=[]
    with open(filename) as f:
        tree = parse_as_tree(f.read())
        for t in tree:
            code = str(t[0]).strip()
            docs = str(t[1]).splitlines()
            code, docs = augment_doc(code, docs)
            print(code, docs)
            ss.append((code, tuple(docs)))
    return ss

read_corpus('_str.py')