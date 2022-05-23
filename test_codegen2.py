import pickle
import re
import keyword
from io import BytesIO
import token
from tokenize import tokenize  # , open
from importlib import import_module
import sys
import random
import csv
import copy
import collections
import builtins
import pandas as pd
import warnings

warnings.simplefilter('ignore')


class P(object):
    def __init__(self):
        self.A = 1
        self.B = 0


pattern = re.compile(r'[\(, .\+\-\)]')


def tokenize_pycode(code):
    try:
        ss = []
        tokens = tokenize(BytesIO(code.encode('utf-8')).readline)
        for toknum, tokval, _, _, _ in tokens:
            if toknum != 62 and tokval != '' and tokval != 'utf-8':
                ss.append(tokval)
        return ss
    except:
        return pattern.split(code)


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


MUTABLES = {
    type([]),
    type({}),
    type(set()),
    type(bytearray()),
    type(pd.DataFrame())
}


def copy_mutable(o):
    t = type(o)
    if t in MUTABLES:
        return copy.copy(o)
    return o


def is_assignment(line):
    tokens = tokenize_pycode(line)
    for token in tokens:
        if token == '=':
            return True
        if token == '(' or token == '[':
            break
    return False


def is_expression(line):
    tokens = tokenize_pycode(line)
    if len(tokens) > 0 and keyword.iskeyword(tokens[0]):
        return False
    for token in tokens:
        if token == '=':
            return False
        if token == '(' or token == '[':
            break
    return True


def shorten_name(name):
    return name[:-1] if name[-1].isdigit() else name


def extract_vars(globals, locals):
    for name, value in locals.items():
        #name = shorten_name(name)
        if name not in dir(builtins):
            values = globals.get(name, [])
            if value not in values:
                values.append(value)
            globals[name] = values


def read_vars(filename, evars):
    globals = {'print': Missing('print')}
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            if line.startswith('import ') or line.startswith('from '):
                try:
                    exec(line, None, globals)
                except:
                    print('Error', line)
            if is_assignment(line):
                locals = {}
                vars = collections.ChainMap(locals, globals)
                try:
                    exec(line, None, vars)
                    extract_vars(evars, locals)
                    for name, value in locals.items():
                        globals[name] = value
                except Exception as e:
                    print('Error2', line, e)


VALUE = set(['True', 'False', 'None'])


def iskeyword(s):
    if s in VALUE or s in dir(builtins):
        return True
    return keyword.iskeyword(s)


def extract_names(code):
    names = []
    try:
        tokens = tokenize(BytesIO(code.encode('utf-8')).readline)
        prev = ''
        for toknum, tokval, _, _, _ in tokens:
            #print(toknum, tokval, names, code)
            if toknum == token.NAME and not iskeyword(tokval) and prev != '.':
                names.append(tokval)
            if tokval == '=' and prev in names:
                names.pop()
            prev = tokval
    except Exception as e:
        print('FIXME', e, code)
    finally:
        return names


def match(value1, value2):
    s1 = str(value1)
    s2 = str(value2)
    if 'at 0x' in s1 and 'at 0x' in s2:
        s1, _, _ = s1.partition('at 0x')
        s2, _, _ = s2.partition('at 0x')
    return s1 == s2


def compare_vars(vars, vars2):
    if len(vars) != len(vars2):
        return False
    if '_' in vars and '_' in vars2:
        return match(vars['_'], vars2['_'])
    for key in vars:
        if key not in vars2:
            return False
        if not match(vars[key], vars2[key]):
            return False
    return True


def iskeyword(s):
    if s in VALUE or s in dir(builtins):
        return True
    return keyword.iskeyword(s)


def modify_code(code):
    if is_expression(code):
        return '_ = ' + code
    return code


modules = {
    'sys': Missing('sys'), 'os': Missing('os'),
    # 'plt': Missing('plt'), 'sns': Missing('sns'),
}


class TestSuite:
    def __init__(self, name_values):
        self.name_values = name_values
        self.tested = 0
        self.syntax_errors = 0
        self.failed = 0
        self.baddata = 0
        self.untested = 0
        self.tested_ok = 0
        self.missing = 0

    def test_code(self, code, code2, check_exact_match=True):
        self.tested += 1
        code = modify_code(code)
        code2 = modify_code(code2)
        self.epoch_succ = 0
        self.epoch_refok = 0
        self.epoch_missing = False
        for _ in range(10):
            if self.try_test_code(code, code2) == False:
                if self.epoch_missing:
                    self.missing += 1
                return
            if self.epoch_succ > 3 and self.epoch_refok > 2:
                break
        if self.epoch_missing:
            self.missing += 1
        if self.epoch_succ > 3 and self.epoch_refok > 2:
            self.tested_ok += 1
            return
        if self.epoch_refok == 0:
            self.baddata += 1
        self.untested += 1
        print(f'untested({self.epoch_succ})', code)

    def try_test_code(self, code, code2):
        globals = {
            'print': Missing('print'),
            'input': Missing('input'),
            'list': lambda x: [x],
            'open': Missing('open'),
        }
        locals = {}
        globals, globals2, useMissing = self.choose_vars(code, globals)
        globals.update(modules)
        vars = collections.ChainMap(locals, globals)
        refFailed = False
        try:
            exec(code, None, vars)
            self.epoch_refok += 1
        except SyntaxError:
            self.untested += 1
            return False
        except Exception as e:
            locals['_'] = e
            refFailed = True
        if useMissing:
            self.epoch_missing = True
        locals2 = {}
        globals2.update(modules)
        vars2 = collections.ChainMap(locals2, globals2)
        try:
            exec(code2, None, vars2)
        except SyntaxError:
            self.syntax_errors += 1
            return False
        except Exception as e:
            locals2['_'] = e
            # if not refFailed:
            #     print('FAILED', str(e), code2)
        if compare_vars(locals, locals2) == False:
            self.failed += 1
            return False
        if useMissing and refFailed:
            self.tested_ok += 1
            return False
        if not refFailed:
            self.epoch_succ += 1
        return True

    def choose_vars(self, code, vars):
        names = extract_names(code)
        useMissing = False
        for name in names:
            if name == '_' or name in vars:
                continue
            if name in self.name_values:
                values = self.name_values[name]
                random.shuffle(values)
                vars[name] = copy_mutable(values[0])
            else:
                #print('@Missing', name)
                useMissing = True
                vars[name] = Missing(name)
        vars2 = {}
        for name, value in vars.items():
            vars2[name] = copy_mutable(value)
        return vars, vars2, useMissing


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

# main()


def save_vars(filename, data):
    with open(filename, 'wb') as f:
        for key, values in data.items():
            for value in values:
                try:
                    if isinstance(value, type(sys)):
                        pickle.dump((0, key, value.__name__), f)
                    else:
                        pickle.dump((1, key, value), f)
                except Exception as e:
                    print('PICKLE FAIL', key, value)


def load_vars(filename, vars):
    with open(filename, 'rb') as f:
        try:
            kind, key, value = pickle.load(f)
            if kind == 0:
                value = import_module(value)
            values = vars.get(key, [])
            if value not in values:
                values.append(value)
            vars[key] = values
        except EOFError:
            pass


def main():
    vars = {}
    tsvfile = None
    for file in sys.argv[1:]:
        if file.endswith('.py'):
            read_vars(file, vars)
        if file.endswith('.tsv'):
            tsvfile = file
        if file.endswith('.vars'):
            load_vars(file, vars)
    save_vars('multiese.vars', vars)

    suite = TestSuite(vars)
    if tsvfile is not None:
        ss = read_tsv(tsvfile)
        for code, code2 in ss:
            suite.test_code(code, code2)
    else:
        #suite.test_code('n<0', 'n<0')
        suite.test_code(
            "print(f'\033[32m{s}\033[0m')", "print(f'\033[32m{s}\033[0m')")

    print(f'Test Count {suite.tested}')
    print(
        f' Syntax Error {suite.syntax_errors} {suite.syntax_errors/suite.tested:.5f}')
    print(f' Pass {suite.tested_ok} {suite.tested_ok/suite.tested:.5f} ')
    print(f' Failed {suite.failed} {suite.failed/suite.tested:.5f} ')
    print(f' Untested {suite.untested} {suite.untested/suite.tested:.5f}')
    print(f' Bad Data {suite.baddata} {suite.baddata/suite.tested:.5f}')
    print(
        f' Missing {suite.missing} {suite.missing/suite.tested:.5f}')


main()
# print(isinstance(sys, type(sys)))
