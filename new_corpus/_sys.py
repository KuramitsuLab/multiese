import os
import sys

obj = 1.0
n = 1

sys.byteorder
'''
@alt(プラットホーム|環境|[実行|動作]環境|OS)
@alt(ランタイム|実行環境|インタプリタ)
@alt(知る|調べる|[確認する|確める])
@alt(バイトオーダ|エンディアン)

[|プラットホームの]バイトオーダ[を知る|を使う|を得る|]
'''

sys.getdefaultencoding()
'''
[|デフォルトの|プラットホームの]エンコーディング[|を知る|を得る]
'''

sys.getrefcount(obj)
'''
@prefix(obj;オブジェクト)

objの参照カウント[|を知る|を得る]
'''

sys.getsizeof(obj)
'''
@alt(バイトサイズ|バイト長|大きさ)

objのバイトサイズ[|を知る]
'''

sys.getrecursionlimit()
'''
@alt(最大の再帰数|スタックの最大[長|の深さ])

[現在の|ランタイムの|]再帰の[最大回数|上限][|を知る]
{何回まで|再帰が}できるか[を|、][|知る]
'''

sys.setrecursionlimit(1000000)
'''

再帰エラーを[未然に|]防ぐ
再帰の[上限|最大回数]を[上げる|増やす]
'''

s = 'A'

sys.intern(s)
'''
sを[隔離する|インターンする]
'''

sys.maxsize
'''
[プラットフォームの|][符号付き|]整数の最大値[|を知る]
'''

sys.maxunicode
'''
@alt(コードポイント|文字コード)

[プラットフォームの|]コードポイントの最大値[|を知る]
'''

sys.platform
'''
@alt(の名前|名)

プラットホームの名前[|を知る|]
'''

__X__ = 'darwin'

sys.platform.startswith('darwin')
'''
@X('darwin';'linux';'win32')
@Y(MacOS;Linux;Windows)
プラットホーム[が|は]__Y__かどうか
'''

sys.argv
'''
コマンドライン引数[|を列挙する]
'''

sys.argv[0]
'''
@alt(得る)
@alt(スクリプト名|[スクリプト|プログラム]ファイル名|プログラム名)

スクリプトの名前[|を知る]
[プログラム|スクリプト]のファイルの名前[|を知る]
'''

sys.argv[1]
'''
[最初の|第一]コマンド引数[|を知る]
コマンドの第一引数[を知る]
第一引数[で指定された|の]ファイルの名前
'''

sys.argv[1]
'''
第２コマンド引数[|を知る]
コマンドの第２引数[を知る]
第２引数[で指定された|の]ファイルの名前
'''

sys.argv[1:]
'''
@test(sys=missing;$$)
@alt(一覧|リスト)

コマンド引数の一覧[|を得る]
コマンド引数を[列挙する|一覧として得る]
'''

sys.flags
'''
コマンド[ライン|]フラグの状態[|を知る]
'''

sys.path
'''
モジュールを検索するパス[|を列挙する]
Pythonパス[の一覧][|を知る]
'''

sys.path.append(dir)
'''
@prefix(dir;[ディレクトリ|])
{モジュールを検索するパスに|dirを}追加する
{Pythonパスに|dirを}追加する
'''

sys.path.append(os.path.join(os.path.dirname(__file__), dir))
'''
{dirを|Pythonパスに}加える
'''

sys.modules
'''
[|既に]ロードされたモジュール[の一覧[|を知る]|を列挙する]
'''

sys.modules[__name__]
'''
現在のモジュール[|を得る]
{自分自身を|モジュールとして}[|を得る]
'''

sys.exc_info()
'''
[現在|][処理|実行]中の例外を情報[|を知る]
'''

sys.stdout.isatty()
'''
[実行時の|]標準出力の出力先がターミナルかどうか
'''

os.isatty(sys.stdin.fileno())
'''
[実行時の|]標準出力の出力先がターミナルかどうか
'''

not sys.stdout.isatty()
'''
[実行時に|]標準出力がパイプかどうか
'''

_, exception, tb = sys.exc_info()
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, '..')
sys.path.insert(0, os.path.abspath('/my/source/lives/here'))
os.path.dirname(sys.modules['__main__'].__file__)
sys.path.append(os.path.join(os.environ['SPARK_HOME'], 'bin'))
os.path.realpath(os.path.dirname(sys.argv[0]))
sys.stdout.isatty()
os.path.dirname(sys.executable)
getattr(sys.modules[__name__], 'A')
os.isatty(sys.stdin.fileno())
sys.stdout = sys.stdout.detach()
caller = sys._getframe(1)
calling_frame = sys._getframe().f_back
current_frame = sys._getframe(0)
cur_version = sys.version_info
f = sys.exc_info()[2].tb_frame
sys.stdin.fileno()
inspect.getmembers()
func_name = sys._getframe().f_code.co_name
if not sys.stdin.isatty():
sys.version_info >= (3, 2):
sys._getframe().f_code.co_name

sys.executable
'''
[Python|]インタプリタの実行ファイルの絶対パス[|を知る]
'''

sys.stdin
'''
標準入力[を得る|]
標準入力[を使う|]
'''

file = sys.__X__
'''
@X(stdout;stderr;open(filename, 'w'))
@Y(標準出力;標準エラー;ファイル)

オプションで、出力先を__Y__に設定する
オプションで、__Y__に出力する
オプションで、__Y__を使う
オプションで、__Y__を出力[|先]にする
'''

sys.stdout
'''
標準出力[を得る|]
標準出力[を使う|]
'''

sys.stderr
'''
標準エラー[を得る|]
標準エラー[を使う|]
エラーを出力する
'''

sys.stdin.read(1)
'''
@alt(読む|読み込む)
{標準入力から|1文字[だけ|分|]}読む
'''

sys.stdin.readline()
'''
{標準入力から|1行[だけ|分|]}読む
'''

sys.stdin.readline().rstrip()
'''
{標準入力から|1行[だけ|分|]|改行[なし[で|に]|を[取り|]除いて]}読む
{標準入力から|1行[だけ|分|]}読み込んで、改行を取り除く
'''

sys.stdout.flush()
'''
@alt(フラッシュする|強制表示する|即時表示する)
標準出力[のバッファ|]をフラッシュする
'''

sys.exit()
'''
@alt(終了する|停止する|止める|終える)
@alt(プログラムの実行|プログラム|実行)

プログラムの実行を[強制的に|ここで|即座に]終了する
'''

sys.exit(0)
'''
プログラムの実行を[正しく|正常[に|]|適切に]終了する
'''

sys.exit(1)
'''
プログラムの実行を[異常|エラーとして]終了する
'''
