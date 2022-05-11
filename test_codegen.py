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
import datetime
import builtins
import pandas as pd
import numpy as np
import warnings

warnings.simplefilter('ignore')

df = pd.DataFrame(data={'A': [1, 2, 3],
                        'B': [1, 1, 0],
                        'C': [1, 0, 1]})
df2 = pd.DataFrame(data={'A': [1, 2, 3],
                         'B': ["a", "b", "c"],
                         'C': ["111", "01", "1"]})


class P(object):
    def __init__(self):
        self.A = 1
        self.B = 0


SAMPLE = dict(
    n=[1, 2, 3, 0, -1],
    k=[0, 1, 100],
    i=(0, 1, 2),
    s=['A B C', '1 2', '1 2 3', 'A', '1', ''],
    x=(1.0, 2.0, 0.5, 0.0, -1.0),
    y=(1.0, 2.0, 0.5, 0.0, -1.0),
    obj=(P(), P()),
    iterable=[[1, 2], ['1', '2', '3'], [], range(10), '123'],

    text=['/usr', 'utf-8', '.txt'],
    filename=['file.txt', 'file.csv', 'file.c', 'file.tsv'],
    # リスト
    alist=[[1, 2, 3], [1, 2], [1, 1], [1], []],
    atuple=[(1, 2, 3), (1, 2), (1, 1), (1,)],
    aset=[set([1, 2, 3]), set([1, 2]), set([1]), set([])],
    array=[np.array([1, 2, 3]), np.array([1, 2])],
    element=[0, 1, -1, 'A', True, []],
    value=[0, 1, -1, 'A'],
    adict=[{'A': 1}, {'B': 2}, {'A': 0, 'B': 1}, {}],
    key=['A', 'B', 'C'],
    name=['A', 'B', 'C'],
    ty=[int, float, str, list],
    deq=[collections.deque(),
         collections.deque([1, 2]),
         collections.deque([1, 2, 3])],
    aCounter=[collections.Counter(),
              collections.Counter(['A', 'B']),
              collections.Counter(['A', 'B', 'A'])],
    df=[df, df2],
    col=['A', 'B', 'C'],
    ch=['A', 'a', 'あ'],
    ds=[df['A'], df['B'], df2['A']],
    xdata=[[1, 2, 3], np.array([1, 2, 3]), df['A']],
    ydata=[[3, 2, 1], np.array([1, 1, 1]), df['B']],
    names=[['A', 'B'], ['A', 'C'], ['A']],
    pattern=['A+', 'A*', 'A|B'],
    rgb=['#ffffff', '#000000', '#deadbe'],
    # module
    math=import_module('math'),
    datetime=import_module('datetime'),
    collections=import_module('collections'),
    itertools=import_module('itertools'),
    np=import_module('numpy'),
    operator=import_module('operator'),
    keyword=import_module('keyword'),
    string=import_module('string'),
    sympy=import_module('sympy'),
    typing=import_module('typing'),
    json=import_module('json'),
    dt=[datetime.datetime(2022, 12, 12), datetime.datetime(
        2021, 1, 1), datetime.datetime(2022, 1, 2)],
    adate=[datetime.datetime(2022, 12, 12), datetime.datetime(
        2021, 1, 1), datetime.datetime(2022, 1, 2)],
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

    # def __getitem__(self, index):
    #     return self.msg[index]


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
            # print(toknum, tokval)
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
        return copy.copy(v), copy.copy(v)
    except:
        return v, v


MISSING_NAMES = set([])


def randomize_name(name, value):
    if name[-1].isdigit():
        name = name[:-1]
    if name in SAMPLE:
        value = SAMPLE[name]
        if not isinstance(value, (list, tuple)):
            return value, value
        return duplicate(random.choice(value))
    if name not in MISSING_NAMES:
        MISSING_NAMES.add(name)
    return value, value


def randomize(vars):
    vars2 = {}
    for name in vars:
        vars[name], vars2[name] = randomize_name(name, vars[name])
    return vars2


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


def match(value1, value2):
    s1 = str(value1)
    s2 = str(value2)
    if 'at 0x' in s1 and 'at 0x' in s2:
        s1, _, _ = s1.partition('at 0x')
        s2, _, _ = s2.partition('at 0x')
    return s1 == s2


class TestSuite:
    def __init__(self):
        self.tested = 0
        self.syntax_errors = 0
        self.notest = 0
        self.testok = 0
        self.missing = 0

    def test_code(self, code, code2, check_exact_match=True):
        self.tested += 1
        if code.startswith('import '):
            self.test_import(code, code2)
            return
        let = code.find(' = ')
        lpr = code.find('(')
        left = ''
        if let > 0 and (lpr == -1 or let < lpr):
            left, _, _ = code.partition(' = ')
            left = ';'+left
        self.test_exec(code, code2, left)

    def test_import(self, code, code2):
        vars = {}
        vars2 = {}
        try:
            global_vars = parse_pyname(code)
            exec(code, global_vars, vars)
            try:
                exec(code2, global_vars, vars2)
                if vars == vars2:
                    self.testok += 1
                return
            except SyntaxError:
                self.syntax_errors += 1
                return
        except Exception as e:
            print('BAD', code, e)
            self.notest += 1

    def test_exec(self, code, code2, left=''):
        vars = parse_pyname(code)
        tcount = 0
        tpass = 0
        result2 = None
        for i in range(1+len(vars)*3):
            vars2 = randomize(vars)
            result = exec_code(code+left, vars)
            if isinstance(result, Exception):
                continue
            tcount += 1
            result2 = exec_code(code2+left, vars2)
            if isinstance(result2, SyntaxError):
                self.syntax_errors += 1
                break
            if match(result, result2):
                tpass += 1
            if isinstance(result, Missing):
                self.missing += 1
                break
        if tcount == 0:
            #print('NOTEST', f'{tpass}/{tcount}', code, code2, result)
            self.notest += 1
        elif tpass == tcount:
            self.testok += 1
        else:
            print('FAILED', f'{tpass}/{tcount}', code, code2, result2)


def read_tsv(filename, index=2, pred_index=1):
    ss = []
    try:
        with open(filename) as f:
            reader = csv.reader(f, delimiter="\t")
            for row in reader:
                ss.append((row[index], row[pred_index]))
    except:
        with open(filename) as f:
            reader = csv.reader(f, delimiter="\t")
            for row in reader:
                ss.append((row[1], row[1]))
    return ss


def main():
    ss = read_tsv(sys.argv[1])
    suite = TestSuite()
    for code, code2 in ss:
        suite.test_code(code, code2)
    print(MISSING_NAMES)
    print(f'Test Count {suite.tested}')
    print(f' Syntax Error {suite.syntax_errors}')
    print(f' Untested {suite.notest} {suite.notest/suite.tested:.5f}')
    print(f' Pass {suite.testok} {suite.testok/suite.tested:.5f} ')
    print(
        f' Missing {suite.missing} {suite.missing/suite.tested:.5f}')


main()
