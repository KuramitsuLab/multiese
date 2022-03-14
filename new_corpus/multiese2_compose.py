try:
    import pegtree as pg
except ModuleNotFoundError:
    import os
    os.system('pip install pegtree')
    import pegtree as pg

import pandas as pd

TYPE_PREFIX = {
    'type': 'クラス',
    'bool': 'ブール値',
    'int': '',
    'float': '',
    'dict': '辞書',
    'list': 'リスト',
    'tuple': 'タプル',
    'function': '関数',
    'set': 'セット',
    'deque': 'デック',
    'Counter': 'カウンタ',
    'ndarray': '配列',
    'DataFrame': 'データフレーム',
    'Series': 'データ列',
    'Symbol': 'シンボル',
    'AssocOp': '式',
}

FILEEXT = {
    'txt': 'テキストファイル',
    'csv': 'CSVファイル',
    'tsv': 'TSVファイル',
}


COLUMN_NAMES = set()


def update_columns(columns):
    COLUMN_NAMES.update(columns)


def detect_string_prefix(name, s):
    if s in COLUMN_NAMES:
        return 'カラム'
    _, sep, ext = s.rpartition('.')
    if sep == '.' and ext in FILEEXT:
        return FILEEXT[ext]
    if '{' in s and '}' in s:
        return '書式'
    return '文字列'


def detect_prefix(name, v):
    if isinstance(v, str):
        return detect_string_prefix(name, v)
    if isinstance(v, pd.DataFrame):
        update_columns(list(v.columns))
    typename = type(v).__name__
    if typename in TYPE_PREFIX:
        return TYPE_PREFIX[typename]
    supername = (type(v).__base__).__name__
    if supername in TYPE_PREFIX:
        return TYPE_PREFIX[supername]
    return ''  # '{typename}'

# code, prefix, key, index = prefix_index_code(str(fix(t)), index)


def prefix_code(code, index, always_policy=False):
    try:
        v = eval(code)
    except:
        if always_policy:
            return code, '', f'<e{index}>', index+1
        return code, '', '', index
    return code, detect_prefix(code, v), f'<e{index}>', index+1


PEG = '''
Start = {
    (Code _ / Chunk)*
    #Statement
}

Chunk = {
    . (!Code .)* #Chunk
}

Code = '`' { (!'`' .)+ #Code } '`' / { '<' (!'>' .)+ '>' #Special } / Expression

Expression =
  Suffix {^ OP Suffix #Binary }*

OP =
  / "==" / "!=" / "<=" / ">=" / "<>"
  / "**" / "//" / ">>" / "<<<" / ">>"
  / "+" / "-" / "*" / "/" / "%" / "="

Suffix = Primary _Postfix*

_Postfix =
  / {^ "(" Expression? ("," Expression )* ")" #App}
  / {^ "[" Expression? (([:,] _) Expression )* "]" #Index}

Primary =
  / Group
  / String
  / Name
  / Number

Group = 
  / "(" Expression ")"
  / { "[" Expression? ("," Expression)* ","? "]"  #List }
  / { "(" Expression? ("," Expression)* ","? ")"  #Tuple }

Name = 
  { [A-Za-z_] [A-Za-z_.0-9]* #Name } _

Number = 
  / { [0-9]+ ('.' [0-9]+)? #Number } _
  / { '.' [0-9]+ #Number } _

String =
  / { 'f'? '"'  (!'"' .)* '"' #String } _
  / { 'f'? "'" (!"'" .)*  "'" #String } _
'''

peg = pg.grammar(PEG)
parser = pg.generate(peg)


def _fix(tree):
    a = [tree.epos_]
    for t in tree:
        a.append(_fix(t).epos_)
    for key in tree.keys():
        a.append(_fix(tree.get(key)).epos_)
    tree.epos_ = max(a)
    return tree


def _replace_expression(s: str, always_policy=False):
    tree = parser(s)
    ss = []
    vars = {}
    index = 0
    # print(repr(tree))
    for t in tree:
        tag = t.getTag()
        if tag == 'Chunk' or tag == 'Special':
            ss.append(str(t))
        else:
            code = str(_fix(t))
            code, prefix, key, index = prefix_code(
                code, index, always_policy=always_policy)
            if key == '':
                ss.append(str(t))
            else:
                vars[key] = code
                ss.append(f'{prefix}{key}')
    return ''.join(ss), vars


def _replace_special(s: str, vars: dict) -> str:
    if isinstance(s, (list, tuple)):
        return tuple(_replace_special(x, vars) for x in s)
    for key in vars:
        s = s.replace(key, vars[key])
    return s


def _translate(s: str) -> str:
    return s


def noprint(*args):
    pass


def _ZEN():
    _ZA = ''.join(chr(ord('Ａ')+c) for c in range(26))
    _Za = ''.join(chr(ord('ａ')+c) for c in range(26))
    _Z0 = ''.join(chr(ord('０')+c) for c in range(10))
    _Z = '\u3000「」！＂＃＄％＆＇（）＊＋，－．／：；＜＝＞＠［＼］＾＿｀｛｜｝'
    return _Z + _ZA + _Za + _Z0


def _HAN():
    _HA = ''.join(chr(ord('A')+c) for c in range(26))
    _Ha = ''.join(chr(ord('a')+c) for c in range(26))
    _H0 = ''.join(chr(ord('0')+c) for c in range(10))
    _H = '\u0020\'\'!"#$%&\'()*+, -./:<=>@[\\]^_`{|}'
    return _H + _HA + _Ha + _H0


_ZEN2HAN = str.maketrans(_ZEN(), _HAN())


def zen2han(s: str) -> str:
    return s.translate(_ZEN2HAN)


def compose(translate=_translate):
    def replace_around(s, always_policy=False, print=noprint):
        s = s.translate(_ZEN2HAN)
        s, vars = _replace_expression(s, always_policy=always_policy)
        print('[BEFORE]', s)
        s = _translate(s)
        print('[AFTER]', s)
        return _replace_special(s, vars)
    return replace_around


if __name__ == '__main__':
    tr = compose()
    tr('「a」をみる', always_policy=True, print=print)

# def compose_nmt(nmt, replace_before=replace_expression, replace_after=replace_special):
#     def translate(s, beams=5):
#         s, vars = replace_before(s)
#         pred, prob = nmt(s, max(beams, 5))
#         pred = [replace_after(s, vars) for s in pred]
#         if beams <= 1:
#             return pred[0]
#         return pred, prob
#     return translate
