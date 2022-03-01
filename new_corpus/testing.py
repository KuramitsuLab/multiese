from importlib import import_module
import numpy as np
import pandas as pd


def _print(*args, **kw):
    sep = kw.get('sep', ' ')
    end = kw.get('end', '\n')
    return sep.join(map(str, args)) + end


def _input(s=None):
    return '123'


class Person:
    def __init__(self):
        self.name = 'Konoha'
        self.age = 17


obj = Person()


def _load_variables():
    df = pd.DataFrame(data=[[1, 2.2, 'a'], [4, 5.8, 'a']],
                      columns=['A', 'B', 'C'])
    return dict(
        n=1,
        n2=3,
        n3=-1,
        x=1.5,
        x2=3.0,
        x3=0.19,
        s=' ABC abc 123あ',  # [文字列]
        s2='a',
        s3='123',
        s4='101',
        text='/usr',  # [|文字列]
        text2='utf-8',
        text3='.txt',
        # リスト
        alist=[1, 2, 3], alist2=[4, 5],
        atuple=(1, 2, 3), atuple2=(4, 5),
        element=2,    # [|文字列|[リスト|タプル]]
        element2=-1,
        element3='A',
        adict={'A': 1}, key='A',
        adict2={'B': 2}, key2='B',
        obj=obj, obj2=obj, Person=Person,
        print=_print,
        input=_input,
        func=lambda x: x,
        predicatefunc=lambda x: True,
        filename='/etc/man.conf',
        math=import_module('math'),
        os=import_module('os'),
        sys=import_module('sys'),
        # str
        re=import_module('re'),
        operator=import_module('operator'),
        itertools=import_module('itertools'),
        iterable=[0, 1, 2, 4],
        iterable2=[7, 8, 9],
        np=import_module('numpy'),
        pd=import_module('pandas'),
        sns=import_module('seaborn'),
        df=df, df2=df, ds=df['A'], ds2=df['B'], col='A', col2='B',
    )


VARS = _load_variables()


def test_code(code, test_with='', reload=True):
    global VARS
    try:
        if test_with != '':
            code = test_with.replace('_', code)
        if ';' in code:
            statement, sep, code = code.rpartition(';')
            exec(statement, VARS)
        v = eval(code, VARS)
        if reload == True:
            VARS = _load_variables()
        return str(v).replace('\n', '\\n')
    except Exception as e:
        # print(repr(e))
        return (e, test_with)
