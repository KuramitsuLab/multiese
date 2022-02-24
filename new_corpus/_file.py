import os
'''
@test_with(_;type(os))
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
ファイルパスのセパレータ記号を使う
'''

os.getcwd()
'''
[[現在の|カレント|][作業|ワーキング]]ディレクトリを得る
'''

filename = '/etc/man.conf'

os.chdir(os.dirname(filename))
'''
@test_with(None)
{[[現在の|カレント|][作業|ワーキング]]ディレクトリを|filenameに}[変更する|[設定|]する]
'''


os.system(text)
'''
[UNIX|]コマンドtextを実行する
'''

filename = '/etc/man.conf'

os.path.basename(filename)
'''
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
filenameをオープンする
filenameからストリームを読み込む
'''

X = open(filename)
'''
@test_with(_;type(X))
filenameからストリームを読み込[み|んで]Xとする
filenameからストリームをオープンしてXとする
'''

__X__ = 'a'
open(filename, mode=__X__)
'''
@test_with(type(_))
@X('r'|'rb'|'w'|'a')
@Y(読み込み|バイナリ|書き込み|追加)
{filenameを|__Y__[モードで_|用に]}オープンする
filenameから__Y__ストリームをオープンする
'''

X = open(filename, mode=__X__)
'''
@test_with(_;type(X))
{filenameを|__Y__[モードで_|用に]}オープンしてXとする
filenameから__Y__ストリームをオープンしてXとする
'''

__X__ = 'utf-8'
open(filename, encoding=__X__)
'''
@test_with(type(_))
@X('utf-8'|'shift_jis'|'euc_jp'|'utf_8_sig'|text2)
@Y(UTF8|SJIS|EUC|BOM付き|文字コードtext2)
{filenameを|__Y__で_|読み込み用に}オープンする
'''

open(filename, mode='w', encoding=__X__)
'''
@test_with(type(_))
{filenameを|__Y__で_|書き込み用に}オープンする
'''

open(filename, mode='a', encoding=__X__)
'''
@test_with(type(_))
{filenameを|__Y__で_|追加するように}オープンする
'''

f.read()
'''
@alt(読み込む|読む)
@test_with(f=open('filer.txt');_)
@test_let(f=open('filer.txt');X = _; X)
f全体を文字列として読み込む
'''

f.readlines()
'''
@test_with(f=open('filer.txt');_)
f全体を[行[単位で|]分割して|リストとして]読み込む
'''

[s.strip() for s in f.readlines()]
'''
@test_with(f=open('filer.txt');_)
f全体を[行[単位で|ごとに]分割して|]リストに変換する
'''

f.readline()
'''
@test_with(f=open('filer.txt');_)
fを一行ずつ読み込む
'''

f.readline()
'''
@test_with(f=open('filer.txt');_)
{fを|改行[を取り除いて|除外して|なしで]}一行ずつ読み込む
'''

s = ''
f.write(s)
'''
@test_with(f=open('filew.txt','w');_)
@alt(書き込む|書く)
{fに|sを}書き込む
'''

x = 0
f.write(str(x))
'''
@test_with(f=open('filew.txt','w');_)
@alt(書き込む|書く)
{fに|xを文字列に[|変換]して}書き込む
'''
