import sys
import os
'''
@test(_;type(os))
osモジュールをインポートする
'''

# 出力

print()
'''
空行をプリントする
改行する
'''

element = 1
element2 = 2

print(element)
'''
xをプリントする
'''

print(element, end='')
'''
@alt(改行なしに|改行せず[|に]|改行しな[いで|くて])
{改行なしに|elementを}プリントする
elementの出力を改行なしに行う
'''

__X__ = ','
print(element, element2, sep=__X__)
'''
@X(','|'\t'|s)
@Y(カンマ|タブ|s)
{elementとelement2を|__Y__区切りで}プリントする
'''

print('Hello World')
'''
[ハローワールド|こんにちは世界][と|を]プリントする
{試しに|何か}動か[す|してみる]
[最初の|初めての]プログラムを書く
'''

x = 0.11
__X__ = ':.3f'
print(__X__.format(x))
'''
@X(':.1f'|':.2f'|':.3f'|':.4f'|':.5f')
@X('1'|'2'|'3'|'4'|'5')
xの小数点以下__Y__桁まで[を|]プリントする
'''

__X__.format(x)
'''
xの小数点以下__Y__桁[まで|]の文字列に変換する
'''

# 入力

input()
'''
[|標準]入力から1行[読み取る|受け取る]
ユーザの入力を[読み取る|受け取る]
[ユーザ|標準入力]から入力される
'''

int(input())
'''
[ユーザの]入力を整数として受け取る
ユーザが整数を入力する
ユーザから入力される
'''

# os

os.sep
'''
@alt(ファイルパス|パス|ファイル名)
@alt(セパレータ|区切り)
ファイルパスのセパレータ記号[|を使う]
'''

os.getcwd()
'''
[[現在の|カレント|][作業|ワーキング]]ディレクトリ[|を得る]
'''

filename = '/etc/man.conf'

os.chdir(os.dirname(filename))
'''
@test(None)
{[[現在の|カレント|][作業|ワーキング]]ディレクトリを|filenameに}[変更する|[設定|]する]
'''

text = "echo 'A'"
os.system(text)
'''
@test(text="echo 'A'";_)
[UNIX|]コマンドtextを実行する
'''

filename = '/etc/man.conf'

os.path.basename(filename)
'''
@prefix(filename;ファイル[|パス];)
filenameの[|拡張子付きの]ファイル名[|を得る]
filenameから[|拡張子付きの]ファイル名を[得る|取り出す]
'''

os.path.splitext(os.path.basename(filename))[0]
'''
filenameの[拡張子なしの|ベース]ファイル名[を得る]
filenameから[拡張子なしの|ベース]ファイル名を[得る|取り出す]
'''

os.path.splitext(filename)[1].lstrip('.')
'''
filenameの拡張子[|を得る]
'''

os.path.splitext(filename)[0] + text
'''
filenameの拡張子をtextに変更する
'''

os.path.dirname(filename)
'''
@alt(ディレクトリ|フォルダ)
filenameのディレクトリ名[|を得る]
filenameからディレクトリ名[を得る|取り出す]
'''

os.path.abspath(filename)
'''
filenameの絶対[|ファイル]パス[|を得る]
filenameを絶対[|ファイル]パスに変換する
'''

os.path.split(filename)
'''
filenameをディレクトリ名とファイル名に分割する
'''

os.path.splitext(filename)
'''
filenameをベース名と拡張子に分割する
'''

os.path.join(text, text2)
'''
textとtext2をファイルパスとして結合する
'''

os.path.join(filename, text)
'''
filenameとtextを結合する
'''

os.path.exists(filename)
'''
filenameが[存在する|ある]かどうか
'''

not os.path.exists(filename)
'''
filenameが[存在し|]ないかどうか
'''

os.path.get_size(filename)
'''
filenameのファイルサイズ
'''


os.path.abspath(__file__)
'''
スクリプトファイルの[絶対|]パス[|を得る]
'''

os.path.dirname(os.path.abspath(__file__))
'''
スクリプトファイルのディレクトリ[名|パス][|を得る]
'''

os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
'''
スクリプトファイルと同じディレクトリのfilenameのパス[|を得る]
'''


open(filename)
'''
@alt(オープンする|開く]
@alt(オープンして|開[いて|き]、]
@alt(からの|から|の)
filenameをオープンする
filenameからの[入力|読み込み|]ストリームを得る
'''

X = open(filename)
'''
@test(_;type(X))
filenameからストリームを読み込[み|んで]Xとする
filenameからストリームをオープンしてXとする
'''

__X__ = 'a'
open(filename, mode=__X__)
'''
@test(type(_))
@X('r'|'rb'|'w'|'a')
@Y(読み込み|バイナリ|書き込み|追加)
{filenameを|__Y__[モードで_|用に]}オープンする
filenameから__Y__ストリームをオープンする
'''

X = open(filename, mode=__X__)
'''
@test(_;type(X))
{filenameを|__Y__[モードで_|用に]}オープンしてXとする
filenameから__Y__ストリームをオープンしてXとする
'''

__X__ = 'utf-8'
open(filename, encoding=__X__)
'''
@test(type(_))
@X('utf-8'|'shift_jis'|'euc_jp'|'utf_8_sig'|text2)
@Y(UTF8|SJIS|EUC|BOM付き|文字コードtext2)
{filenameを|__Y__で_|読み込み[用|できるよう]に}オープンする
'''

open(filename, mode='w', encoding=__X__)
'''
@test(type(_))
{filenameを|__Y__で_|書き込み[用|できるよう]に}オープンする
'''

open(filename, mode='a', encoding=__X__)
'''
@test(type(_))
{filenameを|__Y__で_|追加できるように}オープンする
'''

f = sys.stdin
f.close()
'''
@alt(クローズする|閉じる|解放する)
@prefix(f;[ファイル|[入力|出力|]ストリーム])
@test(f=open('filer.txt');_)
fをクローズする
'''

f.read()
'''
@alt(読み込む|読む)
@prefix(f;[ファイル|[入力|]ストリーム])
@test(f=open('filer.txt');_)
@test_let(f=open('filer.txt');X = _; X)
f全体を文字列として読み込む
'''

f.read(1)
'''
@alt(読み込む|読む)
@test(f=open('filer.txt');_)
@test_let(f=open('filer.txt');X = _; X)
fから１[文字|バイト]、読み込む
'''

f.read(n)
'''
@alt(読み込む|読む)
@test(f=open('filer.txt');_)
@test_let(f=open('filer.txt');X = _; X)
fからn[文字|バイト]、読み込む
'''

f.readlines()
'''
@test(f=open('filer.txt');_)
f全体を[行[単位で|]分割して|リストとして]読み込む
'''

[s.strip() for s in f.readlines()]
'''
@test(f=open('filer.txt');_)
f全体を[行[単位で|ごとに]分割して|]リストに変換する
'''

f.readline()
'''
@test(f=open('filer.txt');_)
fを一行ずつ読み込む
'''

f.readline()
'''
@test(f=open('filer.txt');_)
{fを|改行[を取り除いて|除外して|なしで]}一行ずつ読み込む
'''

s = ''
f.write(s)
'''
@prefix(f;[ファイル|[出力|]ストリーム])
@test(f=open('filew.txt','w');_)
@alt(書き込む|書く)
{fに|sを}書き込む
'''

x = 0
f.write(str(x))
'''
@test(f=open('filew.txt','w');_)
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
