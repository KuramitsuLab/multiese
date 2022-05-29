import sys
import os
'''
osモジュールをインポートする
'''


# os

os.sep
'''
@alt(ファイルパス|パス|ファイル名)
@alt(セパレータ|区切り)
ファイルパスのセパレータ記号[|を使う|を見る]
'''

os.getcwd()
'''
[[現在の|カレント|][作業|ワーキング]]ディレクトリ[|を得る]
'''

filepath = '/etc/man.conf'

os.chdir(os.dirname(filepath))
'''
@test(os=missing;$$)
{[[現在の|カレント|][作業|ワーキング]]ディレクトリを|filepathに}[変更する|[設定|]する]
'''

text = "echo 'A'"
os.system(text)
'''
@test(os=missing;text="echo 'A'";$$)
[UNIX|]コマンドtextを実行する
'''

filepath = '/etc/man.conf'

os.path.basename(filepath)
'''
@prefix(filepath;ファイル[|パス];)
filepathの[|拡張子付きの]ファイル名[|を得る]
filepathから[|拡張子付きの]ファイル名を[得る|取り出す]
'''

os.path.splitext(os.path.basename(filepath))[0]
'''
filepathの[拡張子なしの|ベース]ファイル名[を得る]
filepathから[拡張子なしの|ベース]ファイル名を[得る|取り出す]
'''

os.path.splitext(filepath)[1].lstrip('.')
'''
filepathの拡張子[|を得る]
'''

os.path.splitext(filepath)[0] + text
'''
filepathの拡張子をtextに変更する
'''

os.path.dirname(filepath)
'''
@alt(ディレクトリ|フォルダ)
filepathのディレクトリ名[|を得る]
filepathからディレクトリ名[を得る|取り出す]
'''

os.path.abspath(filepath)
'''
filepathの絶対[|ファイル]パス[|を得る]
filepathを絶対[|ファイル]パスに変換する
'''

os.path.split(filepath)
'''
filepathをディレクトリ名とファイル名に分割する
'''

os.path.splitext(filepath)
'''
filepathをベース名と拡張子に分割する
'''

filepath = "../"
filename = "file.txt"

os.path.join(filepath, filename)
'''
filepathとfilenameを結合する
'''


os.path.exists(filepath)
'''
filepathが[存在する|ある]かどうか
'''

not os.path.exists(filepath)
'''
filepathが[存在し|]ないかどうか
'''

os.path.get_size(filepath)
'''
filepathのファイルサイズ
'''

__file__ = 'file.py'

os.path.abspath(__file__)
'''
スクリプトファイルの[絶対|]パス[|を得る]
'''

os.path.dirname(os.path.abspath(__file__))
'''
スクリプトファイルのディレクトリ[名|パス][|を得る]
'''

os.path.join(os.path.dirname(os.path.abspath(__file__)), filepath)
'''
スクリプトファイルと同じディレクトリのfilepathのパス[|を得る]
'''


open(filepath)
'''
@test(open=missing;$$)
@alt(オープンする|開く]
@alt(オープンして|開[いて|き]]
@alt(からの|から|の)
filepathをオープンする
filepathからの[入力|読み込み|]ストリームを得る
'''

file = open(filepath)
'''
@test(open=missing;$$;file)
filepathからストリームを読み込[み|んで]、fileとする
filepathからストリームをオープンして、fileとする
'''

__X__ = 'a'
open(filepath, mode=__X__)
'''
@test(open=missing;$$)
@X('r'|'rb'|'w'|'wb'|'a')
@Y(読み込み|バイナリ|書き込み|バイナリ書き込み|追加)
{filepathを|__Y__[モードで_|用に]}オープンする
{filepathを|__Y__できるように}オープンする
filepathをオープンして、__Y__ストリームを得る
'''

f = open(filepath, mode=__X__)
'''
@test(open=missing;$$)
{filepathを|__Y__[モードで_|用に]}オープンして、fとする
filepathから__Y__ストリームをオープンして、fとする
'''

mode = __X__
'''
@test($$;mode)
＜オプション＞__Y__[モード|用]に設定する
＜オプション＞__Y__モードを使う
'''


__X__ = 'utf-8'
open(filepath, encoding=__X__)
'''
@test(open=missing;$$)
@alt(エンコーディング|文字コード)
@X('utf-8'|'shift_jis'|'euc_jp'|'utf_8_sig'|text|s)
@Y(UTF8|SJIS|EUC|BOM付き|文字コードtext|sの示すエンコーディング)
{filepathを|__Y__で_}オープンする
'''

open(filepath, mode='w', encoding=__X__)
'''
@test(open=missing;$$)
{filepathを|__Y__で_|書き込み[用|できるよう]に}オープンする
'''

open(filepath, mode='a', encoding=__X__)
'''
@test(open=missing;$$)
{[既存の|]filepathを|__Y__で_|追加できるように}オープンする
'''

encoding = __X__
'''
@test($$;encoding)
＜オプション＞エンコーディングを__Y__に設定する
＜オプション＞__Y__を使う
'''

buffering = 0
'''
＜オプション＞[バッファリングを無効にする|バッファを使わない]
'''

n = 4096

buffering = 4096
'''
＜オプション＞[バッファリング|バッファ]のサイズを[設定する|大きくする|小さくする]
'''

errors = 'strict'
'''
＜オプション＞エラーがあるとき、例外を発生させる[ように設定する|]
'''

errors = 'ignore'
'''
＜オプション＞エラーを無視する[ように設定する|]
'''

newline = __X__
'''
@X('\n';'\r';'\r\n';None)
@Y(UNIX;旧Mac;Windows;動作環境依存)

＜オプション＞改行コードを__Y__に設定する
'''

f = Missing('f')

f.close()
'''
@alt(クローズする|閉じる|解放する)
@prefix(f;[ファイル|[入力|出力|]ストリーム])

fをクローズする
'''

f.read()
'''
@alt(読み込む|読む)

fを[全部、|全て]読み込む
'''

f.read(1)
'''
fから1[文字|バイト]、読み込む
'''

f.read(n)
'''
fからn[文字|バイト]、読み込む
'''

f.readlines()
'''
f全体を[行[単位で|]分割して|リストとして]読み込む
'''

[s.strip() for s in f.readlines()]
'''
f全体を[行[単位で|ごとに]分割して|]リストに変換する
'''

f.readline()
'''
fを一行ずつ読み込む
'''

f.readline()
'''
{fを|改行[を取り除いて|除外して|なしで]}一行ずつ読み込む
'''

s = ''
f.write(s)
'''
@prefix(f;[ファイル|[出力|]ストリーム])
@alt(書き込む|書く)

{fに|sを}書き込む
'''

x = 0
f.write(str(x))
'''
@test(f=missing;$$)
@alt(書き込む|書く)

{fに|xを文字列に[変換|]して}書き込む
'''

# プラットホーム依存なしに = 安全に | プラットホーム依存なしに | プラットホーム依存せずに |
# 新規に = 新しく | 新たに | 新規に
# ディレクトリ = ディレクトリ | フォルダ
# ファイルパス = ファイルパス | パス

# os.mkdir('dir/')
# '''
# [新規に]/{'dir/'のディレクトリ}を作る
# '''

# os.makedirs('dir/', exist_ok=True)
#    'dir/'のディレクトリを[再帰的に | 階層的に]作る

#    os.listdir('dir/')
#    'dir/'(ファイルパス)のファイル一覧

#    os.path.exists(p)
#    p(ファイルパス)が[存在する]かどうか

#    os.path.isdir(p)
#    p(ファイルパス)がディレクトリかどうか

#    os.path.isfile(p)
#    p(ファイルパス)がファイルかどうか

#    os.path.getsize('file.txt')
#    'file.txt'(ファイル名)の[ファイルサイズ | バイト数 | 大きさ]

#    os.path.join(p, p2)
#    {p(ファイルパス)とp2}を/[プラットホーム依存なしに]結合する
