# Python 基本文法

# 演算子

obj = 'A'
obj2 = 'A'

obj == obj2
'''
objがobj2に等しいかどうか
objがobj2かどうか
'''

obj is obj2
'''
@alt(同一|同じ)
objがobj2と同一[オブジェクト |]かどうか
objとobj2は同一[オブジェクト |]かどうか
'''

repr(obj)
'''
objをデバッグ向けの文字列に変換する
'''

str(obj)
'''
objをユーザ向けの文字列に変換する
'''

# 組み込み関数（リスト）

iter(obj)
'''
objのイテレータ
'''

# 組み込み関数（バイト列、IO）

bytearray(s)
'''
sをバイト配列に変換する
'''

bytes(s)
'''
sをバイト列に変換する
'''

memoryview(obj)
'''
objのメモリビュー[|を得る]
'''

# 組み込み関数（関数）

callable(obj)
'''
objが_関数かどうか
'''

eval(s)
'''
sを[式として|]評価する
'''

globals()
'''
グローバル変数の一覧[|を得る]
'''


class Person:
    def __init__(self):
        self.TYPE = 'Konoha'
        self.age = 17


obj = Person()
text = 'age'
s = 'age'

# 組み込み関数（オブジェクト）

delattr(obj, text)
'''
@alt(プロパティ|属性|フィールド)
@alt(削除する|消す|取り除く)
@test(text='age';_)
objのtextプロパティを削除する
'''

getattr(obj, text)
'''
objのtextプロパティの値[|を得る]
@test(text='age';_)
'''

getattr(obj, s)
'''
objのプロパティをsで指定して、その値を得る
@test(s='age';_)
'''

hasattr(obj, text)
'''
@alt(存在する|ある)
objにtextプロパティが存在するかどうか
objがtextプロパティを持つかどうか
'''

hasattr(obj, s)
'''
objにsという[名前の|]プロパティが存在するかどうか
objがsという[名前の|]プロパティを持つかどうか
'''

setattr(obj, text, element)
'''
objのtextプロパティ[の値|]をelementに設定する
'''

hash(obj)
'''
objのハッシュ値[|を求める]
'''

TYPE = Person
isinstance(obj, TYPE)
'''
@alt(クラス|型)
@alt(TYPE=Person;_)
objがTYPEクラス[|のインスタンス]かどうか
'''

__X__ = int
isinstance(obj, __X__)
'''
@X(int|float|str|bool|list|tuple|dict|set|bytes)
@Y(整数|浮動小数点数|文字列|論理値|リスト|タプル|辞書|集合|バイト列)
obj[は|が]__Y__[クラス[|のインスタンス]|]かどうか
'''

isinstance(obj, __X__)
'''
@X((int,float)|(list|tuple))
@Y(数値|リストかタプル)
obj[は|が]__Y__かどうか
'''

issubclass(TYPE, TYPE2)
'''
@alt(TYPE=TYPE2=Person;_)
TYPEクラスが_TYPE2クラスのサブクラスかどうか
'''

id(obj)
'''
@alt(オブジェクト識別子|固有のID|ポインタ)
objのオブジェクト識別子[|を得る]
'''

type(obj)
'''
objの[クラス|型|種類][|を得る|を調べる]
'''
