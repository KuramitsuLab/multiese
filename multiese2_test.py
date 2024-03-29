from functools import partial
from importlib import import_module
import datetime
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

    def __str__(self):
        return repr((self.name, self.age))


class Missing:

    def __init__(self):
        self.msg = ''

    def __str__(self):
        return self.msg

    def __repr__(self):
        return '_'

    def __call__(self, *args, **kwargs):
        if len(kwargs) == 0:
            self.msg += repr((*args,))
        else:
            self.msg += repr((*args, dict(**kwargs)))
        return self

    def __getattr__(self, name):
        self.msg += f'.{name}'
        return self

    def __getitem__(self, index):
        self.msg += f'[{index}]'
        return self

    def __add__(self, index):
        self.msg += f'__add__({index})'
        return self

    def __sub__(self, index):
        self.msg += f'__sub__({index})'
        return self

    def __mul__(self, index):
        self.msg += f'__mul__({index})'
        return self

    def __truediv__(self, index):
        self.msg += f'__truediv__({index})'
        return self

    def __floordiv__(self, index):
        self.msg += f'__floordiv__({index})'
        return self

    def __mod__(self, index):
        self.msg += f'__mod__({index})'
        return self

    def __eq__(self, index):
        self.msg += f'__eq__({index})'
        return self

    def __ne__(self, index):
        self.msg += f'__ne__({index})'
        return self

    def __le__(self, index):
        self.msg += f'__le__({index})'
        return self

    def __ge__(self, index):
        self.msg += f'__ge__({index})'
        return self

    def __lt__(self, index):
        self.msg += f'__lt__({index})'
        return self

    def __gt__(self, index):
        self.msg += f'__gt__({index})'
        return self


obj = Person()
missing = Missing()


def function(x): return x


def _load_variables():
    df = pd.DataFrame(data=[[1, 2.2, 'a'], [4, 5.8, 'a']],
                      columns=['A', 'B', 'C'])
    return dict(
        missing=Missing(),
        n=1, n2=3, n3=-1,
        x=1.5, x2=3.0, x3=0.19,
        s=' ABC abc 123あ',  # [文字列]
        s2='a', s3='123', s4='101',
        text='/usr', text2='utf-8', text3='.txt',
        # リスト
        alist=[1, 2, 3], alist2=[4, 5], names=['A', 'B'],
        atuple=(1, 2, 3), atuple2=(4, 5), atuple3=('A', 'B'),
        array=np.array([1, 2, 3]), array2=np.array([4, 5]),
        element=2, element2=-1, element3='A',
        adict={'A': 1}, key='A', adict2={'B': 2}, key2='B',
        obj=obj, obj2=obj, Person=Person,
        print=_print,
        input=_input,
        func=function,
        predicatefunc=lambda x: True,
        filepath='./file.txt',
        filename='/etc/man.conf',
        math=import_module('math'),
        os=import_module('os'),
        sys=import_module('sys'),
        # str
        re=import_module('re'),
        operator=import_module('operator'),
        datetime=import_module('datetime'),
        dt=datetime.datetime(2022, 12, 12),
        adate=datetime.date(2022, 12, 12),
        typing=import_module('typing'),
        itertools=import_module('itertools'),
        collections=import_module('collections'),
        iterable=[0, 1, 2, 4],
        iterable2=[7, 8, 9],
        np=import_module('numpy'),
        pd=import_module('pandas'),
        sns=import_module('seaborn'),
        df=df, df2=df, ds=df['A'], ds2=df['B'], col='A', col2='B',
    )


VARS = _load_variables()


def test_code(code, test_with='$$', reload=True):
    global VARS
    try:
        code = test_with.replace('$$', code)
        if ';' in code:
            statement, _, code = code.rpartition(';')
            exec(statement, VARS)
        v = eval(code, VARS)
        if reload == True:
            VARS = _load_variables()
        return str(v).replace('\n', '\\n')
    except Exception as e:
        return f'\033[31m{e}\033[0m'
