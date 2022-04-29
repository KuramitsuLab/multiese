import re
'''
@test($$;type(re))
@prefix(pattern;[パターン|正規表現];パターン)
正規表現を使う
正規表現をインポートする
'''

pattern = '.*'
s = '1'
repl = '\\1'

re.compile(pattern)
'''
@test(re=missing;pattern='.*';$$)
@alt(事前に|あらかじめ|前もって|)
[|正規表現で、]{事前に|patternを}コンパイルする
'''

__X__ = 0
re.compile(pattern, flag=__X__)
'''
@test(re=missing;pattern='.*';$$)
@X(re.ASCI;re.IGNORECASE;re.MULTILINE)
@Y(ASCII限定として;[大文字・小文字|ケース]を無視して;複数行対応として)
[|正規表現で、]{事前に|__Y__|patternを}コンパイルする
'''

re.search(pattern, s)
'''
@test(re=missing;pattern='.*';$$)
[|正規表現で、]sの中からpatternにマッチする[文字列|位置]を探す
[|正規表現で、]sを走査し、patternにマッチするか見る
'''

re.search(pattern, s, flags=__X__)
'''
@test(re=missing;pattern='.*';$$)
[|正規表現で、]sの中からpatternに__Y__マッチする[文字列|位置]を探す
[|正規表現で、]sを走査し、patternに__Y__マッチするか見る
'''

re.match(pattern, s)
'''
@test(re=missing;pattern='.*';$$)
[|正規表現で、]{sの先頭で|patternに}マッチさせる
[|正規表現で、]sの先頭でpatternにマッチするか見る
'''

re.match(pattern, s, flags=__X__)
'''
@test(re=missing;pattern='.*';$$)
[|正規表現で、]{sの先頭で|__Y__|patternに}マッチさせる
[|正規表現で、]sの先頭でpatternに__Y__マッチするか見る
'''

re.fullmatch(pattern, s)
'''
@test(re=missing;pattern='.*';$$)
[|正規表現で、]{s全体を|patternに}マッチさせる
[|正規表現で、]s全体がpatternにマッチするか見る
'''

re.fullmatch(pattern, s, flags=__X__)
'''
@test(re=missing;pattern='.*';$$)
[|正規表現で、]{s全体を|__Y__|patternに}マッチさせる
[|正規表現で、]s全体がpatternに__Y__マッチするか見る
'''

re.split(pattern, s)
'''
@test(re=missing;pattern='.*';$$)
@alt(分割する|区切る|分ける)
[|正規表現で、]{sを|[出現した|]patternで}分割する
'''

re.split(pattern, s, flags=__X__)
'''
@X(re.ASCI;re.IGNORECASE;re.MULTILINE)
@Y(ASCII限定の;[大文字・小文字|ケース]を無視した;複数行対応の)
@test(re=missing;pattern='.*';$$)
@alt(分割する|区切る|分ける)
[|正規表現で、]{sを|__Y__[pattern|パターン]で}分割する
'''

re.findall(pattern, s)
'''
@test(re=missing;pattern='.*';$$)
@alt(分割する|区切る|分ける)
@alt(全ての|すべての|全|)
[|正規表現で、]sの中のpatternによる全てのマッチを得る
[|正規表現で、]sの中でpatternにマッチした全ての文字列をリストに変換する
'''

re.findall(pattern, s, flags=__X__)
'''
@test(re=missing;pattern='.*';$$)
@alt(分割する|区切る|分ける)
@alt(全ての|すべての|全|)
[|正規表現で、]sの中の__Y__[pattern|パターン]による全てのマッチを得る
[|正規表現で、]sの中で__Y__[pattern|パターン]にマッチした全ての文字列をリストに変換する
'''

re.sub(pattern, repl, s)
'''
@test(re=missing;repl='\1';pattern='.*';$$)
@alt(置き換える|置換する)
[|正規表現で_、]sの中のpatternによるで置き換える
[|正規表現で_、]sの中でpatternにマッチした文字列をreplで置き換える
'''

re.sub(pattern, repl, s, flags=__X__)
'''
@test(re=missing;repl='\1';pattern='.*';$$)
@alt(置き換える|置換する)
[|正規表現で_、]sの中の__Y__[pattern|パターン]よって置き換える
[|正規表現で_、]sの中で__Y__[pattern|パターン]にマッチした文字列をreplで置き換える
'''
