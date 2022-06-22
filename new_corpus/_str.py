# 文字列

import keyword
from importlib import import_module
import re

import string
'''
[文字列モジュール|string[|モジュール]]をインポートする

@prefix(sub;部分文字列)
@alt(先頭|最初|左[側|端])
@alt(末尾|最後|後ろ|右[側|端])
@alt(左側|左)
@alt(右側|右)
'''

string = import_module('string')
keyword = import_module('keyword')

s = 'ABC abc 123'  # 文字列 s, s2, s3
s2 = 'a'
s3 = '123'
ch = 'A'

n = 1  # 整数 n, n1, n2
n2 = 3


filename = 'file.txt'  # ファイル name
aStringList = ['A', 'B', 'C']  # 文字列(リスト|タプル)

''
'''
空文字[|を得る]
an empty string
'''

'\n'
'''
改行[|文字][|を得る]
'''

'\t'
'''
タブ[|文字][|を得る]
'''

' '
'''
空白[|文字][|を得る]
space 
'''

string.ascii_letters
'''
@alt(全ての|全)
@alt(全部|全て|)
@alt(アルファベット|英字)

アルファベットの文字列
アルファベットを全部得る
'''

string.ascii_lowercase
'''
[アルファベットの|]小文字列
[アルファベットの|]小文字を全部得る
'''

string.ascii_uppercase
'''
[アルファベットの|]大文字列
[アルファベットの|]大文字を全部得る
'''

string.digits
'''
全ての数字
数字を全部得る
'''

string.hexdigits
'''
全ての十六進数字
十六進数字を全部得る
'''

string.octdigits
'''
全ての[８|八]進数字
[８|八]進数字を全部得る
'''

string.punctuation
'''
@alt(句読点|句点)

全ての句読点文字
句読点文字を全部得る
'''

string.printable
'''
@alt(印字可能な文字|印字できる文字|印字)

全ての印字可能な文字
印字可能な文字を全部得る
'''

string.whitespace
'''
全ての空白文字
空白文字を全部得る
'''

unicode = ord('A')

chr(unicode)
'''
@prefix(unicode;[文字コード|ユニコード])

unicodeを文字に変換する
unicodeに対応する文字[|を得る]
'''

ord(ch)
'''
@prefix(ch;文字)
@alt(ユニコード=[文字コード|ユニコード|ASCIIコード])

chをユニコードに変換する
chのユニコード[|を得る]
'''

[ord(ch) for ch in s]
'''
sをユニコード列に変換する
'''

s.upper()
'''
sを[全て|]大文字に変換する
[s中の|]小文字を大文字に変換する
'''

s.lower()
'''
sを[全て|]小文字に変換する
[s中の|]大文字を小文字に変換する
'''

s.casefold()
'''
@alt(ケース|大文字小文字)

sのケースを[変換する|整える]
sを[全て|]小文字に変換する
sを[積極的に|特殊文字も含め]小文字に変換する
'''

list(s)
'''
@alt(文字リスト|文字のリスト)

sを文字リストに変換する
s中の文字を列挙する
'''

s.split()
'''
@alt(区切る|分割する)
@alt(で_|によって|を[用い|使っ]て)

{sを|空白で}区切って、[文字列リストに変換する|列挙する]
{sを|空白で_}区切る
'''

map(int, s.split())
'''
@alt(整数リスト|整数のリスト|[|整]数列)

{sを|空白で_}区切って、整数リストに変換する
'''

sub = ';'

s.split(sub)
'''
@alt(セパレータ|区切り[|記号])

{sを|[sub|セパレータ]で}区切って、[文字列リストに変換する|列挙する]
{sを|[sub|セパレータ]で_}区切る
'''

__X__ = ','

s.split(__X__)
'''
@X(',';':';sep)
@Y(カンマ;コロン;[セパレータ|区切り])

{sを|__Y__で}[分割して|区切って]、文字列リストに変換する
{sを|__Y__で_}区切って、列挙する
'''

s.splitlines()
'''
{sを|改行で}[分割し|区切り]、文字列リストに変換する
{sを|改行で_}区切る
'''

s.rsplit()
'''
{sを|[末尾|最後|右]から|空白で}区切る
'''

s.rsplit(sub)
'''
{sを|[末尾|最後|右]から|subで}区切る
'''

sep = ' '

s.partition(sep)
'''
@alt(二分する|[二|]分割する|二つに分ける)

sを二分する
'''

s.partition(sub)
'''
{sを|[|最初の]subで_}二分する
'''

s.rpartition(sub)
'''
{sを|最後のsubで_}二分する
'''

s.partition(sub)[0]
'''
@alt(とき|時|場合)
@alt(二分し|二つに区切って)
@alt(分けた|分割した)

{sを|[|最初の]subで}二分し、[前半の|最初の|先頭の]文字列を得る
{sを|[|最初の]subで}分けたときの[前半の|最初の|先頭の]文字列[|を得る|を取り出す]
'''

s.partition(sub)[-1]
'''
{sを[|最初の]subで}二分し、[後半の|残りの]文字列を得る
{sを|[|最初の]subで}分けたときの[後半の|残りの]文字列[|を得る|を取り出す]
'''

s.rpartition(sub)[0]
'''
{sを|最後のsubで}二分し、[前半の|最初の|先頭の]文字列を得る
{sを|最後のsubで}分けたときの[前半の|最初の|先頭の]文字列[|を得る|を取り出す]
'''

s.rpartition(sub)[-1]
'''
{sを最後のsubで}二分し、[後半の|残りの]文字列を得る
{sを最後のsubで}分けたときの[後半の|残りの]文字列[|を得る|を取り出す]
'''

sub = 'A'
subnew = 'a'

s.replace(sub, newsub)
'''
@alt(置き換える|置換する)
@prefix(newsub;[新しい|別の]文字列)

文字列を置き換える
{文字列を|newsubで_}[|全部]置き換える
{s中のsubを|newsubに}[|全部]置き換える
{s中のsubを|s3に}[|全部]置き換える
'''

s.replace(sub, newsub, n)
'''
{文字列を|[回数を制限して|n回だけ]}置き換える
{s中のsubを|newsubに|回数を制限して}置き換える
'''

s.replace(sub, '')
'''
@alt(取り除く|除く|除去する|消す)

sからsubを[全て|]取り除く
'''

s.expandtabs(tabsize=n)
'''
s中のタブ文字を[|n個の]空白に[置き換える|する]
'''

s.strip()
'''
@alt(不要な=[|不要な|余分な])

sの両端から不要な[空白|空白と改行]を取り除く
sをトリムする
'''

s.strip(sub)
'''
sの両端からsubを取り除く
'''

s.lstrip()
'''
sの先頭[から|の]不要な[空白|空白やタブ]を取り除く
sを左トリムする
'''

__X__ = sub

s.lstrip(__X__)
'''
@X(sub;'\t';' ')
@Y(sub;タブ;空白)

sの[左[側|端]|先頭]から__Y__を取り除く
'''

s.rstrip()
'''
sの[右[側|端]|末尾]から[|不要な|余分な][空白|改行]を取り除く
sを右トリムする
'''

__X__ = sub

s.rstrip(__X__)
'''
@X(sub;'\t';'\n';' ')
@Y(sub;タブ;改行;空白)

sの[右[側|端]|末尾]から__Y__を取り除く
'''

文字列幅 = 10

s.zfill(文字列幅)
'''
@alt(ゼロ埋めする|パディングする)

sをゼロ埋めする
'''

str(n).zfill(文字列幅)
'''
[整数|数値]をゼロ埋めした文字列に変換する
'''

s.center(文字列幅)
'''
sを[センタリング|中央寄せ][に|]する
'''

s.ljust(文字列幅)
'''
sを左寄せ[に|]する
'''

s.rjust(文字列幅)
'''
sを右寄せ[に|]する
'''

s.capitalize()
'''
sをキャピタライズする
sの先頭だけ大文字化する
'''

s.swapcase()
'''
[sの|]大文字と小文字を[交換する|逆にする|入れ替える]
sのケースを[入れ替える|交換する|逆にする]
'''

aStringList = ['A', 'B', 'C']

s in aStringList
'''
@alt(含まれる|ある|存在する)
@prefix(aStringList;文字列リスト)

sがaStringListのいづれかどうか
sがaStringListに含まれるかどうか
'''

s = 'ABCDEFG'
sub = 'C'
start = 1
end = 3

sub in s
'''
部分文字列かどうか
{s中に|subが}含まれるかどうか
'''

sub not in s
'''
@alt(含まれない|ない|存在しない)
{s中に|subが}含まれないかどうか
'''

s.find(sub)
'''

{s中から|subを}[探す|見つける]
{sの先頭から|subを}[探す|見つける]
'''

s.find(sub, start) != -1
'''
@prefix(start;開始位置)
@prefix(end;終了位置)

{sのstart[以降に|より後に|先に]|subが}含まれるかどうか
'''

s.find(sub, start) == -1
'''
{sのstart[以降に|より後に|から先に]|subが}含まれないかどうか
'''

s.find(sub, 0, end) != -1
'''

{sのend[より前に|以前に]|subが}含まれるかどうか
'''

s.find(sub, 0, end) == -1
'''
{sのend[より前に|以前に]|subが}含まれないかどうか
'''


s.find(sub, start, end) != -1
'''
{sのstartとendの間に|subが}含まれるかどうか
{sのstartからとendの[間|範囲]に|subが}含まれるかどうか
'''

s.find(sub, start, end) == -1
'''
sのstart番目とend番目の間にsubが含まれないかどうか
{sのstart[|番目]からとend[|番目]までの[間|範囲]に|subが}含まれないかどうか
'''

s.find(sub, start)
'''
{sのstartから|subを}探す
'''

s.find(sub, 0, end)
'''
{sのendまで|subを}探す
'''

s.find(sub, start, end)
'''
subを範囲を指定して探す
{sのstartからendまで|subを}探す
'''

s.rfind(sub)
'''
{sの末尾から|subを}[探す|見つける]
'''

s.find(sub, start, end)
'''
subを範囲を指定して探す
{sの末尾から|範囲を指定してsubを}探す
'''

''.join(aStringList)
'''
@alt(連結する|結合する|つなげる|一つにする)

aStringListを連結する
aStringListを[連結して|]一つの文字列にする
'''

sep = ','

sep.join(aStringList)
'''
{aStringListを|sepを区切りとして}連結する
{aStringListを|sepを区切りにして}一つの文字列にする
'''

iterable = [1, 1, 2]
''.join(map(str, iterable))
'''
{iterableを|文字列[に変換し|とし]て}連結する
aStringListを[連結して|]一つの文字列にする
'''

__X__.join(map(str, iterable))
'''
@X(' ';',';'\t';'\n';sub)
@Y(空白;カンマ;タブ;'改行;部分文字列)
{iterableを|文字列[リスト|]に}変換して、__Y__で_連結する
'''

s.count(sub)
'''
@alt(カウントする|数える)
@alt(出現数=出現[|回数]|登場[|回数])

s中のsubの出現数[をカウントする|]
s中のsubをカウントする
s中にsubがいくつか含まれるか[調べる|カウントする]
'''

s.count(sub, start, end)
'''
@alt(までの範囲|の[範囲|間])

sのstartからendまでの範囲でsubの出現数[をカウントする|]
sのstartからendまでの範囲でsubをカウントする
sののstartからendまでの間にsubがいくつか含まれるか[調べる|カウントする]
'''

s.startswith(sub)
'''
@alt(接頭辞|先頭|プレフィックス|左[側|端])
@alt(始まる|開始する)

{subが|subで}始まるかどうか
sの接頭辞[が|は]subかどうか
'''

s.startswith(sub, start)
'''
{sのstart以降が|subで}始まるかどうか
'''

s.endswith(sub)
'''
@alt(接尾辞|末尾|サフィックス|右[側|端])
@alt(終わる|終了する)

{sが|subで}終わるかどうか
sの接尾辞[が|は]subかどうか
'''

s.removeprefix(sub)
'''
@alt(安全に|エラーなく)
{[|安全に]|sの接頭辞から|subを}取り除く
'''

s.removesuffix(sub)
'''
{[|安全に]|sの接尾辞から|subを}取り除く
'''

__X__ = '.csv'
filename.endswith(__X__)
'''
@X('.csv';'.txt';'.tsv';'.json')
@Y(CSV;テキスト;TSV;JSON)
@prefix(filename;ファイル名)

{filenameが|__Y__ファイル}かどうか
'''

s.isupper()
'''
sが[全て|]大文字かどうか
'''

s.islower()
'''
sが[全て|]小文字かどうか
'''

s.isdigit()
'''
sが[全て|]数字かどうか
'''

s.isalpha()
'''
sが[全て|]アルファベットかどうか
'''

s.isalnum()
'''
sが[全て|]英数字かどうか
'''

s.isascii()
'''
@alt(アスキー文字|ASCII文字)

sが[全て|]アスキー文字かどうか
'''


s.isspace()
'''
sが[全て|]空白[文字|][からなる|]かどうか
'''


s.isdecimal()
'''
s[は|が][全て|]十進数字かどうか
'''

s.isnumeric()
'''
s[は|が][全て|]数値かどうか
'''

any(c.__X__() for c in s)
'''
@alt(含まれる|ある)
@X(isupper|islower|isdigit|isalpha|isalnum|isspace|isascii)
@Y(大文字|小文字|数字|アルファベット|英数字|空白|アスキー文字)

{s内に|[ひとつでも|]__Y__が}含まれるかどうか
'''

any(not c.__X__() for c in s)
'''
{s中に|[ひとつでも|]非__Y__が}含まれるかどうか
'''

s.isidentifier()
'''
s[は|が][全て|]識別子名かどうか
'''

keyword.iskeyword(s)
'''
s[は|が][Pythonの|]キーワードかどうか
'''

s.isprintable()
'''
s[は|が][全て|]印字できるかどうか
'''

s.istitle()
'''
s[は|が]タイトルケースかどうか
'''

s.encode(encoding='utf-8', errors='strict')
'''
{sを|[UTF8で|]}バイト列に変換する
'''

s.encode(encoding='sjis', errors='ignore')
'''
{sを|SJISで}バイト列に変換する
'''

s.encode(encoding='unicode_escape')
'''
{sを|ユニコードエスケープで}バイト列に変換する
'''

encoding = 'utf-8'

s.encode(encoding=encoding)
'''
@prefix(encoding;[エンコーディング|文字コード])

{sを|encodingで_}バイト列に変換する
'''

s.encode(errors='ignore')
'''
{エラーを無視して|sを}バイト列に変換する
'''

args = []
formatText = ''

formatText.format(*args)
'''
@test(text='<{}>';$$)
@alt(フォーマットする|文字列整形する)

@prefix(formatText;[書式|テンプレート])
formatTextを{argsを|引数として}フォーマットする
'''

aDict = {'A': '1'}
formatText = '{A}'

formatText.format_map(aDict)
'''
@test(text='<{}>';mapping={};$$)
formatTextをaDictでフォーマットする
'''

len(s)
'''
sの[長さ|文字数|大きさ][|を得る]
'''

s[0]
'''
sの[先頭|最初][|の文字][|を得る]
'''

s[-1]
'''
sの[末尾|最後][|の文字][|を得る]
'''

s[n]
'''
sのn番目[|の文字][|を得る]
'''

s == s2
'''
２つの文字列[は|が][同じ|等しい]かどうか
'''

s != s2
'''
２つの文字列[は|が][等しく|同じで]ないかどうか
'''

s < s2
'''
{２つの文字列を|辞書順で}比較する
{s[が|は]s2より|辞書順で}前かどうか
'''

s > s2
'''
{s[が|は]s2より|辞書順で}後かどうか
'''

s.casefold() == s2.casefold()
'''
@alt(ケースを無視して|大文字小文字を無視して)
２つの文字列[が|は]ケースを無視して同じか
'''

s.casefold() < s2.casefold()
'''
２つの文字列をケースを無視して比較する
'''

# Tips
('ァ' <= ch <= 'ン')
'''
@alt(片仮名|カタカナ)
@alt(平仮名|ひらがな)
s[が|は]片仮名かどうか
'''

('ぁ' <= ch <= 'ん')
'''
s[が|は]平仮名かどうか
'''

('\u4E00' <= ch <= '\u9FD0')
'''
s[が|は]漢字かどうか
'''

re.search('[\u4E00-\u9FD0]', s)
'''
{s[|内|中]に|漢字が}[含まれる|使われている]かどうか
'''

re.search('[あ-んア-ン\u4E00-\u9FD0]', s)
'''
{s[|内|中]に|日本語が}[含まれる|使われている]かどうか
'''

''.join([chr(ord(ch) - 96) if ('ァ' <= ch <= 'ン') else ch for ch in s])
'''
[s中の|]片仮名を平仮名に変換する
'''

''.join([chr(ord(ch) + 96) if ('ぁ' <= ch <= 'ん') else ch for ch in s])
'''
[s中の|]平仮名を片仮名に変換する
'''

s.translate(str.maketrans('０１２３４５６７８９', '0123456789'))
'''
[s中の|]全角数字を半角数字に変換する
'''
