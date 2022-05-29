# Python 基本文法

# 演算子

obj = 'A'
obj2 = 'A'

obj == obj2
'''
@prefix(obj;オブジェクト)

２つのobj[が|は]等しいかどうか
'''

obj is obj2
'''
@alt(同一|同じ)

２つのobj[が|は]同一[参照|]かどうか
'''

repr(obj)
'''
objをデバッグ向けの文字列に変換する
'''

str(obj)
'''
objを[|ユーザ向けの]文字列に変換する
'''

# 組み込み関数（リスト）

iter(obj)
'''
objのイテレータ
objを[イテラブル|イテレータ]に変換する
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
obj[が|は]関数かどうか
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

プロパティ名 = 'age'

delattr(obj, プロパティ名)
'''
@alt(プロパティ|属性|フィールド)
@alt(削除する|消す|取り除く)

obj[の|から]プロパティを削除する
'''

getattr(obj, プロパティ名)
'''
objのプロパティの値[|を得る]
'''

hasattr(obj, プロパティ名)
'''
@alt(存在する|ある)
objにプロパティが存在するかどうか
objがプロパティを持つかどうか
'''

値 = 'A'

setattr(obj, プロパティ名, 値)
'''
objのプロパティ[の値|]を値に設定する
objのプロパティの値を設定する
'''

hash(obj)
'''
objのハッシュ値[|を求める]
'''

クラス = int

isinstance(obj, クラス)
'''
@alt(クラス|型)

obj[が|は][ある|]クラス[|のインスタンス]かどうか
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

サブクラス = object

issubclass(サブクラス, クラス)
'''
[クラスの|]サブクラスかどうか
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
