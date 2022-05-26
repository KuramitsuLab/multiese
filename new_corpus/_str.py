# 文字列

from importlib import import_module
import re
import keyword
import string

string = import_module('string')
keyword = import_module('keyword')

s = 'ABC abc 123'  # 文字列 s, s2, s3
s2 = 'a'
s3 = '123'
ch = 'A'

n = 1  # 整数 n, n1, n2
n2 = 3

filename = 'file.txt'  # テキストファイル name
aStringList = ['A', 'B', 'C']  # 文字列(リスト|タプル)

''
'''
空文字[|を得る]
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
'''

string.ascii_letters
'''
@alt(全ての|全)
全ての[アルファベット|英字][|を[得る|使う]]
'''

string.ascii_lowercase
'''
@test(import string;$$)
全ての小文字[|を[得る|使う]]
'''

string.ascii_uppercase
'''
@test(import string;$$)
全ての大文字[|を[得る|使う]]
'''

string.digits
'''
@test(import string;$$)
全ての数字[|を[得る|使う]]
'''

string.hexdigits
'''
@test(import string;$$)
全ての十六進数字[|を[得る|使う]]
'''

string.octdigits
'''
@test(import string;$$)
全ての[８|八]進数字[|を[得る|使う]]
'''

string.punctuation
'''
@test(import string;repr($$))
全ての句読点文字[|を[得る|使う]]
'''

string.printable
'''
@test(import string;repr($$))
全ての印字[|可能な]文字[|を[得る|使う]]
'''

string.whitespace
'''
@test(import string;repr($$))
全ての空白文字[|を[得る|使う]]
'''

unicode = ord('A')

chr(unicode)
'''
unicodeを文字に変換する
unicodeの文字[|を得る]
'''

ord(ch)
'''
@prefix(ch;文字)
@alt(ユニコード=[文字コード|ユニコード|ASCIIコード])

chのユニコード[|を得る]
'''

s.upper()
'''
@alt(大文字|英大文字)
@alt(の_|[内|中]の)

sを[全て|]大文字に変換する
[s中の|]小文字を大文字に変換する
'''

s.lower()
'''
@alt(小文字|英小文字)

sを[全て|]小文字に変換する
[s中の|]大文字を小文字に変換する
'''

s.casefold()
'''
@alt(小文字|英小文字)

sを[全て|]小文字に変換する
sを[積極的に|特殊文字も含め]小文字に変換する
'''

list(s)
'''
@alt(文字リスト|文字のリスト)

sを文字リストに変換する
sの文字を列挙する
'''

s.split()
'''
@alt(区切る|分割する)
@alt(で_|によって|を[用い|使っ]て)
@alt(文字列リスト|文字列のリスト|リスト)

{sを|空白で}区切って、[文字列リストに変換する|列挙する]
{sを|空白で_}区切る
'''

map(int, s.split())
'''
@alt(整数リスト|整数のリスト|[|整]数列)

{sを|空白で_}区切って、整数リストに変換する
'''

s.split(sub)
'''
{sを|s2で}区切って、[文字列リストに変換する|列挙する]
{sを|subで_}区切る
'''

__X__ = ','
s.split(__X__)
'''
@X(','|':'|sep)
@Y(カンマ|コロン|[セパレータ|区切り])

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

s.rsplit(sep)
'''
{sを|[末尾|最後|右]から|s2で}区切る
'''

s.partition(s2)
'''
@alt(二分する|[二|]分割する|二つに分ける)
@return(文字列タプル)
{sを|[|最初の]s2で}二分する
'''

s.rpartition(s2)
'''
@return(文字列タプル)
{sを|最後のs2で}二分する
'''

s.partition(s2)[0]
'''
@alt(とき|時|場合)
@alt(二分し|二つに区切って)
@alt(分けた|に分割した)
{sを|[|最初の]s2で}二分し、[前半の|最初の|先頭の]文字列を得る
{sを|[|最初の]s2で}分けたときの[前半の|最初の|先頭の]文字列[|を得る|を取り出す]
'''

s.partition(s2)[-1]
'''
{sを[|最初の]s2で}二分し、、[後半の|残りの]文字列を得る
{sを|[|最初の]s2で}分けたときの[後半の|残りの]文字列[|を得る|を取り出す]
'''

s.rpartition(s2)[0]
'''
{sを|最後のs2で}二分し、[前半の|最初の|先頭の]文字列を得る
{sを|最後のs2で}分けたときの[前半の|最初の|先頭の]文字列[|を得る|を取り出す]
'''

s.rpartition(s2)[-1]
'''
{sを最後のs2で}二分し、[後半の|残りの]文字列を得る
{sを最後のs2で}分けたときの[後半の|残りの]文字列[|を得る|を取り出す]
'''

s.replace(s2, s3)
'''
@alt(置き換える|置換する)
文字列を置き換える
{s中のs2を|s3に}[全て|]置き換える
sにおいて{s2を|s3に}[全て|]置き換える
'''

s.replace(s2, s3, n)
'''
{s[内|中]のs2を|[|最大]n回[だけ|のみ]|s3に}置き換える
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
sの両端から[|不要な|余分な][空白|改行]を取り除く
sをトリムする
'''

s.strip(sub)
'''
sの両端からsubを取り除く
'''

s.strip('\n')
'''
sの両端から改行を取り除く
'''

s.lstrip()
'''
sの[左[側|端]|先頭]から[|不要な|余分な][空白|改行]を取り除く
sを左トリムする
'''

s.lstrip(sub)
'''
sの[左[側|端]|先頭]からsubを取り除く
'''

s.rstrip()
'''
sの[右[側|端]|末尾]から[|不要な|余分な][空白|改行]を取り除く
sを右トリムする
'''

s.rstrip(sub)
'''
sの[右[側|端]|末尾]からsubを取り除く
'''

s.zfill(n)
'''
{sを|[長さ|文字数|幅]nで}[パディング|ゼロ埋め]する
'''

str(n).zfill(n2)
'''
{整数nを|ゼロ[パディング|埋め]で_}n2桁の文字列に変換する
'''

width = 40
s.center(width)
'''
@prefix(width;[長さ|文字数|幅])
{sを|[widthで|]}[センタリング|中央寄せ][に|]する
'''

s.ljust(n)
'''
{sを|[長さ|文字数|幅]nで}左寄せ[に|]する
'''

s.rjust(n)
'''
{sを|[長さ|文字数|幅]nで}右寄せ[に|]する
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
@prefix(aStringList;文字列リスト)

sがaStringList内のいづれかどうか
'''

s = 'ABCDEFG'
sub = 'C'
start = 1
end = 3

sub in s
'''
@alt(含まれる|ある|存在する)
@prefix(sub;部分文字列)

{s中に|subが}含まれるかどうか
'''

sub not in s
'''
@alt(含まれない|ない|存在しない)
{sの中に|subが}含まれないかどうか
'''

s.find(sub)
'''
@alt(先頭|最初|左[側|端])
@alt(末尾|最後|後ろ|右[側|端])
@prefix(sub;[部分文字列|文字列|])

{s[の中|]から|subを}[探す|見つける]
{sの先頭から|subを}[探す|見つける]
'''

s.find(sub, start) != -1
'''
{sのstart[|番目][以降に|より後に|から先に]|subが}含まれるかどうか
'''

s.find(sub, start) == -1
'''
{sのstart番目[以降に|より後に|から先に]|subが}含まれないかどうか
'''

s.find(sub, 0, end) != -1
'''
{sのend番目[より前に|以前に]|subが}含まれるかどうか
'''

s.find(sub, 0, end) == -1
'''
{sのend番目[より前に|以前に]|subが}含まれないかどうか
'''


s.find(sub, start, end) != -1
'''
{sのstart番目とend番目の間に|subが}含まれるかどうか
{sのstart[|番目]からとend[|番目]までの[間|範囲]に|subが}含まれるかどうか
'''

s.find(sub, start, end) == -1
'''
sのstart番目とend番目の間にsubが含まれないかどうか
{sのstart[|番目]からとend[|番目]までの[間|範囲]に|subが}含まれないかどうか
'''

s.find(sub, start)
'''
{sのstart[番目|]から|subを}探す
'''

s.find(sub, start, end)
'''
{sのnからn2[まで|]の[間|範囲]で|subを}探す
'''

s.rfind(sub)
'''
{sの末尾から|subを}[探す|見つける]
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

','.join(map(str, iterable))
'''
{iterableを|カンマ区切りで}連結する
'''

s.join(map(str, iterable))
'''
{iterableを|sで}連結する
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

s.startswith(s2)
'''
@alt(接頭辞|先頭|プレフィックス|左[側|端])
@alt(始まる|開始する)
{subが|subで}始まるかどうか
sの接頭辞[が|は]subかどうか
'''

s.startswith(sub, n)
'''
{sのn番目が|s2で}始まるかどうか
'''

s.endswith(sub)
'''
@alt(接尾辞|末尾|サフィックス|右[側|端])
@alt(終わる|終了する)

{sが|subで}終わるかどうか
sの接尾辞[が|は]subかどうか
'''

s.removeprefix(s2)
'''
@alt(安全に|エラーなく)
{[|安全に]|sの接頭辞から|s2を}取り除く
'''

s.removesuffix(s2)
'''
{[|安全に]|sの接尾辞から|s2を}取り除く
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
sが[全て|][アルファベット|英字]かどうか
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

any(not c.__Y__() for c in s)
'''
{s内に|[ひとつでも|]非__Y__が}含まれるかどうか
'''

s.isidentifier()
'''
s[は|が][全て|]識別子名かどうか
'''

keyword.iskeyword(s)
'''
s[は|が]キーワードかどうか
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
{sを|UTF8で}バイト列に変換する
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
sとs2を比較する
sとs2[は|が][同じ|等しい]かどうか
s[が|は]s2と[同じ|等しい]か比較する
'''

s != s2
'''
sとs2[は|が][等しく|同じで]ないかどうか
'''

s < s2
'''
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
[sの|]片仮名を平仮名に変換する
'''

''.join([chr(ord(ch) + 96) if ('ぁ' <= ch <= 'ん') else ch for ch in s])
'''
[sの|]平仮名を片仮名に変換する
'''

s.translate(str.maketrans('０１２３４５６７８９', '0123456789'))
'''
[sの|]全角数字を半角数字に変換する
'''
