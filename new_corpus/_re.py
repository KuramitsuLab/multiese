import re
'''
@prefix(pattern;[正規表現|パターン])

正規表現モジュールをインポートする
正規表現を使う
'''

pattern = '.*'
s = '1'
newsub = '\\1'

re.compile(pattern)
'''
@alt(事前に|あらかじめ|前もって|)

{事前に|patternを}コンパイルする
'''

flag = re.ASCII
'''
option: [ASCII|アスキー]文字に限定する
'''

flag = re.IGNORECASE
'''
option: [大文字・小文字|ケース]を無視する
'''

flag = re.MULTILINE
'''
option: 複数行に対応する
'''

__X__ = 0

re.compile(pattern, flag=__X__)
'''
@X(re.ASCI;re.IGNORECASE;re.MULTILINE)
@Y(ASCII限定として;[大文字・小文字|ケース]を無視して;複数行対応として)

{事前に|__Y__|patternを}コンパイルする
'''

re.search(pattern, s)
'''
s中からpatternにマッチする[文字列|位置]を探す
sを走査し、patternにマッチするか見る
'''

re.search(pattern, s, flags=__X__)
'''
s中からpatternに__Y__マッチする[文字列|位置]を探す
sを走査し、patternに__Y__マッチするか見る
'''

re.match(pattern, s)
'''
{sが|patternに}マッチさせる
sの先頭でpatternにマッチするか見る
'''

re.match(pattern, s, flags=__X__)
'''
{sの先頭で|__Y__|patternに}マッチさせる
sの先頭でpatternに__Y__マッチするか見る
'''

re.fullmatch(pattern, s)
'''
{s全体を|patternに}マッチさせる
s全体がpatternにマッチするか見る
'''

re.fullmatch(pattern, s, flags=__X__)
'''
{s全体を|__Y__|patternに}マッチさせる
s全体がpatternに__Y__マッチするか見る
'''

re.split(pattern, s)
'''
@alt(分割する|区切る|分ける)
{sを|patternで}分割する
'''

re.split(pattern, s, flags=__X__)
'''
@alt(分割する|区切る|分ける)
{sを|__Y__patternで}分割する
'''

re.findall(pattern, s)
'''
@alt(分割する|区切る|分ける)
@alt(全ての|すべての|全|)

sの中のpatternによる全てのマッチを得る
sの中でpatternにマッチした全ての文字列をリストに変換する
'''

re.findall(pattern, s, flags=__X__)
'''
@alt(分割する|区切る|分ける)
@alt(全ての|すべての|全|)

sの中の __Y__[pattern|パターン]による全てのマッチを得る
sの中で __Y__[pattern|パターン]にマッチした全ての文字列をリストに変換する
'''

re.sub(pattern, newsub, s)
'''
@alt(置き換える|置換する)
@prefix(newsub;新しい文字列)

{sを|patternによって}置き換える
{s中のpatternを|newsubで_}置き換える
{patternにマッチした文字列を|newsubで}置き換える
'''
