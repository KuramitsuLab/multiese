import sys

obj = 1.0
n = 1

sys.byteorder
'''
@alt(プラットホーム|環境|OS)
@alt(知る|調べる|使う)
プラットホームのバイトオーダ[|を知る]
'''

sys.getdefaultencoding()
'''
[デフォルトの|]エンコーディング[|を知る]
'''

sys.getrefcount(obj)-1
'''
objの参照カウント[|を知る]
'''

sys.getsizeof(obj)
'''
objのバイトサイズ[|を知る]
'''

sys.getrecursionlimit()
'''
alt(最大再帰数|スタックの最大[長|の深さ])
[現在の|]最大再帰数[|を知る]
'''

sys.setrecursionlimit(1000000)
'''
再帰エラーを防ぐ
最大再帰数の上限を上げる
'''

sys.setrecursionlimit(n)
'''
@test(n=5000;_)
最大再帰数をnに設定する
再帰エラーを防ぐため[に|]、上限をnに設定する
'''

s = 'A'

sys.intern(s)
'''
sを隔離する
'''

sys.maxsize
'''
[プラットフォームの|][符号付きの|]最大整数値[|を知る]
'''

sys.maxunicode
'''
@alt(コードポイント|文字コード)
[プラットフォームの|]ユニコード最大コードポイント[|を知る]
'''

sys.platform
'''
プラットホーム[|を知る]
'''

sys.argv[0]
'''
@alt(得る)
@alt(スクリプト名|スクリプトファイル名)
スクリプト名[|を得る]
'''

sys.argv[1]
'''
コマンドの第一引数[|を得る]
'''

sys.argv[n]
'''
コマンドのn番目の引数[|を得る]
'''

sys.argv[1:]
'''
コマンド引数をリストとして[|得る]
'''

sys.path.append('/path/to/whatever')
'''
Pythonパスに'/path/to/whatever'を追加する
'''

#sys.path.append(os.path.join(os.path.dirname(__file__), 'subdir'))

sys.stdin
'''
@test(type(_))
標準入力[|を[得る|使う]]
'''

sys.stdout
'''
@test(type(_))
標準出力[|を[得る|使う]]
'''

sys.stderr
'''
@test(type(_))
標準エラー[|を[得る|使う]]
'''

sys.stdin.read(1)
'''
@test(None)
@alt(読む|読み込む)
標準入力から1文字[だけ|]読む
'''

sys.stdin.readline()
'''
@test(None)
標準入力から1行[だけ|]読む
'''

sys.stdin.readline().rstrip()
'''
@test(None)
標準入力から1行[だけ|]読み込んで、改行を取り除く
'''


sys.stdout.flush()
'''
標準出力をフラッシュする
'''

sys.exit()
'''
@test(None)
プログラムを[正しく|正常[に|]|適切に]終了する
'''

sys.exit(0)
'''
@test(None)
プログラムを正常終了する
'''

sys.exit(1)
'''
@test(None)
プログラムを異常終了する
'''
