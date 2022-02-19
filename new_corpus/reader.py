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

import re
BEGIN = '([^A-Za-z0-9]|^)'
END = ('(?![A-Za-z0-9]|$)')
VARPAT = re.compile(BEGIN+r'([a-z]+)(\d?)'+END)

def _replace_vars(s, oldnews):
    s = re.sub(VARPAT, r'\1@\2\3@', s)  # @s@
    for old, new in oldnews:
        s = s.replace(f'@{old}@', f'{new}')
    return s.replace('@', '')

def _check_variables(doc, code):
    names = [(x[1],x[2]) for x in VARPAT.findall(doc)]
    ss=set(name[0] for name in names if names[1] != '')
    if len(ss) == 0:
        return doc, code
    d={name: [] for name in ss}
    for name in names:
        if name[0] in ss:
            d[name[0]].append(name[1])
    oldnews = []
    for key in d:
        order_names = d[key]
        sorted_names = list(sorted(order_names))
        if order_names != sorted_names:
            print('diff', key, order_names, sorted_names)
            oldnews += [(key+s1, key+s2) for s1, s2 in zip(order_names, sorted_names) if s1 != s2]
    doc = _replace_vars(doc, oldnews)
    code = _replace_vars(code, oldnews)
    return doc, code



PATTERNS = [
    (re.compile(BEGIN+r'(s\d?)'+END), r'\1文字列\2'),
    (re.compile(BEGIN+r'(iterable\d?)'+END), r'\1[イテラブル|リスト|タプル|[配|データ|]列]\2'),
    (re.compile(BEGIN+r'(mapping\d?)'+END), r'\1[マッピング|辞書]\2'),
    (re.compile(BEGIN+r'(func\d?)'+END), r'\1関数\2'),
    (re.compile(BEGIN+r'(df\d?)'+END), r'\1データフレーム\2'),
    (re.compile(BEGIN+r'(ds\d?)'+END), r'\1データ列\2'),
    (re.compile(BEGIN+r'(value\d?)'+END), r'\1[|文字列|リスト]\2'),
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
    for old, new in PATTERNS:
        s = re.sub(old, new, s)
    for old, new in altdic.items():
        if old in s:
            #print('=>', old, new)
            s = s.replace(old, new)
    return s

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
    for s in ss:
        print(s)
    return ss

read_corpus('_itertools.py')