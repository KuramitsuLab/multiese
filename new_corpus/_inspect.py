import inspect
'''
@alt(得る|取得する)
'''

inspect.currentframe().f_code.co_name
'''
[実行中の|プログラムの|][関数|メソッド][名|の名前]を得る
'''

オブジェクト = None
識別子 = inspect

__X__ = オブジェクト
'''
@X(オブジェクト;識別子)
@Y(オブジェクト;[識別子|変数名])
'''

# docから

inspect.ismodule(__X__)
'''
__Y__[が|は]モジュールかどうか
'''

inspect.isclass(__X__)
'''
__Y__[が|は]クラスかどうか
'''

inspect.ismethod(__X__)
'''
__Y__[が|は]メソッドかどうか
'''

inspect.isfunction(__X__)
'''
__Y__[が|は]関数かどうか
'''

inspect.isgeneratorfunction(__X__)
'''
__Y__[が|は]ジェネレータ関数かどうか
'''

inspect.isgenerator(__X__)
'''
__Y__[が|は]ジェネレータかどうか
'''

'''
__Y__[が|は][コルーチン|async]関数かどうか
'''

inspect.iscoroutine(__X__)
'''
__Y__[が|は]コルーチンかどうか
'''

inspect.isawaitable(__X__)
'''
ジェネレータベースのコルーチンと通常のジェネレータを区別する
'''

inspect.isasyncgenfunction(__X__)
'''
__Y__[が|は]非同期ジェネレータ関数かどうか
'''

inspect.isasyncgen(__X__)
'''
__Y__[が|は]非同期ジェネレータかどうか
'''

inspect.istraceback(__X__)
'''
__Y__[が|は]トレースバックかどうか
'''

inspect.isframe(__X__)
'''
__Y__[が|は][スタック|]フレームかどうか
'''

inspect.iscode(__X__)
'''
__Y__[が|は]コードかどうか
'''

inspect.isbuiltin(__X__)
'''
__Y__[が|は]ビルトイン[|関数]かどうか
'''

inspect.isabstract(__X__)
'''
__Y__[が|は]抽象クラスかどうか
'''
