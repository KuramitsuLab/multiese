import keyword
from io import BytesIO
import token
from tokenize import tokenize, open
from importlib import import_module
import sys
import random
import csv
import copy
import collections
import builtins
import pandas as pd
import numpy as np
import warnings

warnings.simplefilter('ignore')

SAMPLE = dict(
    n=[1, 2, 3, 0, -1],
    s=['A B C', '1 2', '1 2 3', 'A', '1', ''],
    x=(1.0, 2.0, 0.5, 0.0, -1.0),
    iterable=[[1, 2], ['1', '2', '3'], [], range(10), '123'],

    text='/usr', text2='utf-8', text3='.txt',
    # リスト
    alist=[[1, 2, 3], [1, 2], [1, 1], [1], []],
    atuple=[(1, 2, 3), (1, 2), (1, 1), (1,)],
    aset=[set([1, 2, 3]), set([1, 2]), set([1]), set([])],
    array=[np.array([1, 2, 3]), np.array([1, 2])],
    element=[2, -1, 'A', True, []],
    adict=[{'A': 1}, {'B': 2}, {'A': 0, 'B': 1}, {}],
    key=['A', 'B', 'C'],
    deq=[collections.deque(), collections.deque([1, 2]),
         collections.deque([1, 2, 3])],
    df=[pd.DataFrame(data={'A': [1, 2, 3], 'B': [1, 1, 0], 'C': [1, 0, 1]})],
    col=['A', 'B', 'C'],
    # module
    math=import_module('math'),
    datetime=import_module('datetime'),
    collections=import_module('collections'),
    itertools=import_module('itertools'),
    np=import_module('numpy'),

    # func=function,
    # predicatefunc=lambda x: True,
    # filepath='./file.txt',
    # filename='/etc/man.conf',
    # math=import_module('math'),
    # # str
    # re=import_module('re'),
    # operator=import_module('operator'),
    # dt=datetime.datetime(2022, 12, 12),
    # adate=datetime.date(2022, 12, 12),
    # typing=import_module('typing'),
    # iterable=[0, 1, 2, 4],
    # iterable2=[7, 8, 9],
    # np=import_module('numpy'),
    # pd=import_module('pandas'),
    # sns=import_module('seaborn'),
    # df=df, df2=df, ds=df['A'], ds2=df['B'], col='A', col2='B',
)


class Missing:

    def __init__(self, name=''):
        self.msg = name

    def __str__(self):
        return self.msg

    def __repr__(self):
        return self.msg

    def __getattr__(self, name):
        return Missing(f'{self.msg}.{name}')

    def __call__(self, *args, **kwargs):
        if len(kwargs) == 0:
            return Missing(f'{self.msg}{args}')
        else:
            return Missing(f'{self.msg}{args}{dict(**kwargs)}')


VALUE = set(['True', 'False', 'None'])


def iskeyword(s):
    if s in VALUE or s in dir(builtins):
        return True
    return keyword.iskeyword(s)


def parse_pyname(code):
    vars = {}
    try:
        tokens = tokenize(BytesIO(code.encode('utf-8')).readline)
        prev = ''
        for toknum, tokval, _, _, _ in tokens:
            #print(toknum, tokval)
            if toknum == token.NAME and not iskeyword(tokval) and prev != '.':
                name = tokval[:-1] if tokval[-1].isdigit() else tokval
                if tokval not in vars:
                    vars[tokval] = None if name in SAMPLE else Missing(tokval)
            if tokval == '=' and prev in vars:
                del vars[prev]
            prev = tokval
        # print(ss)
    finally:
        return vars


VARS = dict(
    print=Missing('print'),
    input=Missing('input'),
    open=Missing('open'),
)


def duplicate(v):
    try:
        return copy.copy(v)
    except:
        return v


MISSING_NAMES = set([])


def randomize_name(name, value):
    if name[-1].isdigit():
        name = name[:-1]
    if name in SAMPLE:
        value = SAMPLE[name]
        if not isinstance(value, (list, tuple)):
            return value
        return random.choice(duplicate(value))
    if name not in MISSING_NAMES:
        MISSING_NAMES.add(name)
    return value


def randomize(vars):
    for name in vars:
        vars[name] = randomize_name(name, vars[name])


def exec_code(code, vars):
    global_vars = VARS.copy()
    try:
        if ';' in code:
            block, _, code = code.rpartition(';')
            v = exec(block, global_vars, vars)
        v = eval(code, global_vars, vars)
        return v
    except Exception as e:
        return e


class TestSuite:
    def __init__(self):
        self.syntax_errors = 0
        self.test_pass = 0
        self.total = 0

    def test_code(self, code, code2):
        vars = parse_pyname(code)
        tcount = 0
        tpass = 0
        for i in range(1+len(vars)*3):
            randomize(vars)
            result = exec_code(code, vars)
            if isinstance(result, Exception):
                #print(code, repr(result))
                continue
            tcount += 1
            result2 = exec_code(code2, vars)
            if str(result) == str(result2):
                tpass += 1
            #print(result, result2)
            if isinstance(result, Missing):
                break
            if isinstance(result2, SyntaxError):
                self.syntax_errors += 1
                break
        self.test_pass += tpass
        self.total += tcount


def read_tsv(filename, index=1, index2=1):
    ss = []
    with open(filename) as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            ss.append((row[index], row[index2]))
    return ss

#print(test_code("math.sin(x)", "math.sin(x)"))
#print(test_code("len(str(n))", "len(str(n))"))
#print(test_code("print(str(n))", "print(str(n))"))


def main():
    ss = read_tsv('kogi_trans.tsv')
    suite = TestSuite()
    for code, code2 in ss:
        suite.test_code(code, code2)
    print(suite.test_pass, suite.total,
          suite.test_pass / suite.total, suite.syntax_errors)
    print(MISSING_NAMES)


main()
