import os
import sys

obj = 1.0
n = 1

sys.byteorder
'''
@alt(プラットホーム|環境|[実行|動作]環境|OS)
@alt(知る|調べる|[確認する|確める])
@alt(バイトオーダ|エンディアン)
[|プラットホームの]バイトオーダ[を知る|を使う|を得る|]
'''

sys.getdefaultencoding()
'''
[|デフォルトの|プラットホームの]エンコーディング[|を知る|を使う|を得る]
'''

sys.getrefcount(obj)-1
'''
@test(sys=missing;$$)
objの参照カウント[を知る|を使う|を得る|]
'''

sys.getsizeof(obj)
'''
@test(sys=missing;$$)
@alt(バイトサイズ|バイト長|大きさ)
objのバイトサイズ[を知る|]
'''

sys.getrecursionlimit()
'''
@test(sys=missing;$$)
@alt(最大の再帰数|スタックの最大[長|の深さ])
[現在の|]最大の再帰数[|を知る]
{何回まで|再帰が}できるか知る
'''

sys.setrecursionlimit(1000000)
'''
@test(sys=missing;$$)
再帰エラーを[未然に|]防ぐ
再帰数の[上限|最大[|値]]を[上げる|増やす]
'''

sys.setrecursionlimit(n)
'''
@test(sys=missing;$$)
最大の再帰数をnに設定する
再帰エラーを防ぐため[に|]、上限をnに設定する
'''

s = 'A'

sys.intern(s)
'''
@test(sys=missing;$$)
sを[隔離する|インターンする]
'''

sys.maxsize
'''
[プラットフォームの|][符号付きの|]最大整数値[|を知る]
'''

sys.maxunicode
'''
@alt(コードポイント|文字コード)
[プラットフォームの|]ユニコードの最大コードポイント[|を知る]
'''

sys.platform
'''
@test(sys=missing;$$)
プラットホーム[|を知る|を確認する]
'''

sys.argv[0]
'''
@test(sys=missing;$$)
@alt(得る)
@alt(スクリプト名|[スクリプト|プログラム]ファイル名|プログラム名)
スクリプト名[を得る|を知る|を使う|]
[プログラム|スクリプト]の[ファイル名|名前]を知る
'''

sys.argv[1]
'''
@test(sys=missing;$$)
[最初の|第一]コマンド引数[を得る|を知る|を使う|]
コマンドの第一引数[を得る|を知る|を使う|]
'''

sys.argv[n]
'''
@test(sys=missing;$$)
[第n|n番目]コマンド引数[を得る|を知る|を使う|]
コマンド引数のn番目[を得る|を知る|を使う|]
コマンドのn番目の引数[を得る|を知る|を使う|]
'''

sys.argv[1:]
'''
@test(sys=missing;$$)
@alt(一覧|リスト)
コマンドの一覧[を得る|を知る|を使う|]
コマンド引数を一案として得る
'''

sys.path
'''
@test(sys=missing;$$)
Pythonパス[の一覧][|を得る|を知る|を使う]
'''

sys.path.append(s)
'''
@test(sys=missing;$$)
Pythonパスにsを追加する
'''

sys.path.append(os.path.join(os.path.dirname(__file__), s))
'''
@test(sys=os=missing;$$)
{sというサブディレクトリを|Pythonパスに}加える
'''

sys.stdin
'''
@test(sys=missing;$$)
標準入力[を得る|]
標準入力[を使う|]
'''

file = sys.__X__
'''
@test(sys=missing;$$;file)
@X(stdout;stderr;open(filename, 'w'))
@Y(標準出力;標準エラー;ファイル)
オプションで、出力先を__Y__に設定する
オプションで、__Y__に出力する
オプションで、__Y__を使う
オプションで、__Y__を出力[|先]にする
'''

sys.stdout
'''
@test(sys=missing;$$)
標準出力[を得る|]
標準出力[を使う|]
'''

sys.stderr
'''
@test(sys=missing;$$)
標準エラー[を得る|]
標準エラー[を使う|]
エラーを出力する
'''

sys.stdin.read(1)
'''
@test(sys=missing;$$)
@alt(読む|読み込む)
{標準入力から|1文字[だけ|分|]}読む
'''

sys.stdin.readline()
'''
@test(sys=missing;$$)
{標準入力から|1行[だけ|分|]}読む
'''

sys.stdin.readline().rstrip()
'''
@test(sys=missing;$$)
{標準入力から|1行[だけ|分|]|改行[なし[で|に]|を[取り|]除いて]}読む
{標準入力から|1行[だけ|分|]}読み込んで、改行を取り除く
'''

sys.stdout.flush()
'''
@test(sys=missing;$$)
@alt(フラッシュする|強制表示する|即時表示する)
標準出力[のバッファ|]をフラッシュする
'''

sys.exit()
'''
@test(sys=missing;$$)
@alt(終了する|停止する|止める|終える)
@alt(プログラムの実行|プログラム|実行)
プログラムの実行を[強制的に|ここで|即座に]終了する
'''

sys.exit(0)
'''
@test(sys=missing;$$)
プログラムの実行を[正しく|正常[に|]|適切に]終了する
'''

sys.exit(1)
'''
@test(sys=missing;$$)
プログラムの実行を[異常|エラーとして]終了する
'''
