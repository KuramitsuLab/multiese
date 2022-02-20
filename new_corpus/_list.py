# list

alist = [1, 2, 3]
alist2 = [4, 5]
atuple = (1, 2, 3)
atuple2 = (4, 5)
element = 2
n = 1
n2 = 3

# リスト

[]
'''
@alt(作る|得る)
空列[|を作る]
空のリスト[|を作る]
'''

()
'''
空の[タプル|組][|を作る]
'''

(element,)
'''
[要素|element]一つの[タプル|組][|を作る]
'''

tuple(alist)
'''
@alt(に変換する|[に|化]する)
alistを[タプル|組]に変換する
alistをイミュータブルにする
'''

list(atuple)
'''
atupleをリストに変換する
atupleをミュータブルにする
'''

__X__ = alist

len(__X__)
'''
@alt(見る|調べる|知る|得る)
@alt(長さ|要素数|個数)
@X(alist|atuple)
@Y(alist|atuple)
__Y__の長さ[|を見る]
'''

len(alist) == 0
'''
alistが空かどうか
'''

len(alist) > 0
'''
alistが空でないかどうか
'''


[element] * n
'''
長さnのリスト[|を作る]
n個の[要素|element]があるリスト[|を作る]
'''

__X__ + __X__2
'''
@alt(連結する|結合する|接続する|加える)
__X__と__Y__2を連結する
'''

__X__ * n
'''
__Y__をn倍する
__Y__をn個連結する
'''

__X__[0]
'''
@alt(先頭|最初)
@alt(末尾|最後)
__Y__の先頭[|の[要素|値]][|を得る]
'''

alist[-1]
'''
__Y__の末尾[|の[要素|値]][|を得る]
'''

__X__[1:]
'''
@alt(取り除く|除く|捨てる)
__Y__の先頭を[取り除く|除く|捨てる]
'''

__X__[n:]
'''
@alt(取り出す|得る|抽出する)
__Y__の先頭のn要素を取り除く
__Y__のn番目以降の[部分|要素]を取り出す
'''

__X__[:-1]
'''
__Y__の末尾を取り除く
'''

__X__[:-n]
'''
__Y__の末尾のn要素を取り除く
__Y__の末尾からn番目以前の[部分|要素]を取り出す
'''

__X__[::-1]
'''
__Y__の[要素|値]を逆順にする
__Y__を逆順にする
'''

__X__[::2]
'''
{__Y__を/[ひとつ置きに|ひとつ飛ばしで]}取り出す
'''

__X__[n:n2]
'''
__Y__のn番目からn2番目[まで][の部分][|を取り出す]
'''

sum(__X__)
'''
__Y__の[合計値|合計|総和][|を求める]
'''

min(__X__)
'''
__Y__の[最小値|一番小さい値][|を求める]
'''

max(__X__)
'''
__Y__の[最大値|一番大きい値][|を求める]
'''

sum(__X__)/len(__X__)
'''
__X__の[平均値|平均][|を求める]
'''

range(len(alist))
'''
@test_with(list(_))
alistの長さだけ繰り返せるようにする
'''

range(n)
'''
@test_with(list(_))
n[個|回]の数値イテラブル[|を得る]
0からnの範囲[|で|を得る]
'''

range(n, n2)
'''
@test_with(list(_))
nからn2の範囲[|で|を得る]
'''

list(range(n))
'''
@alt(数列|整数列|整数リスト)
[|0から始まる]n個の数列[|を作る]
'''

list(range(n+1))
'''
0からnまでの数列[|を作る]
'''

list(range(1, n+1))
'''
1からnまでの数列[|を得る|を作る]
'''

list(range(n, n2+1))
'''
nからn2までの数列[|を得る|を作る]
'''

list(range(n, n2+1, 2))
'''
@alt(ひとつ飛ばし|一つ置き)
nからn2までのひとつ飛ばしの数列
'''

alist.append(element)
'''
@test_with(None)
@alt(追加する|加える)
alist[に|の末尾に][element|要素]を追加する
'''

alist.extend(alist2)
'''
@test_with(None)
alist[に|の末尾に]alist2を[追加する|展開する]
alist[に|の末尾に]alist2を追加して、[拡張する|広げる]
'''


alist.insert(n, element)
'''
@test_with(None)
@alt(挿入する|差し込む)
alistのn番目にelementを挿入する
'''

alist.pop()
'''
@test_with(None)
alistの末尾から[要素|値]を[ポップする|取り出す|取り除く]
'''

alist.pop(n)
'''
@test_with(None)
alistn番目から[要素|値]を[ポップする|取り出す|取り除く]
'''

alist.clear()
'''
@test_with(None)
@alt(消去する|消す)
alistの[全ての|全|][要素|値]を[クリアにする|取り除く|消去する|空にする]
'''

alist.remove(element)
'''
@test_with(None)
alistから[lement[|と等しい最初の要素]を取り除く
'''

del alist[n]
'''
@test_with(None)
alistのn番目[の[要素|値]|]を[削除する|消す]
'''

element in __X__
'''
elementが__Y__の要素かどうか
element[がは]__Y__に含まれるかどうか
'''

element not in __X__
'''
elementが__Y__の要素でないかどうか
element[がは]__Y__に含まれないかどうか
'''

__X__.index(element)
'''
@alt(内|中)
@alt(インデックス|位置|場所)
__Y__[|中]のelementが最初に見つかるインデックス[|を探す|を得る]
__Y__[|中]の最初のelementを探す
'''

sorted(__X__)
'''
@alt(ソートする|並べる|並べ変える|並べ直す)
__Y__[の[要素|値]]をソートする
'''

sorted(__X__, reverse=False)
'''
@alt(昇順に|小さい[順に|方から])
{__Y__[の[要素|値]]を|昇順に}ソートする
'''

sorted(__X__, reverse=True)
'''
@alt(降順に|大きい[順に|方から])
{__Y__[の[要素|値]]を|昇順に}ソートする
'''


def func(x): return x+1


sorted(__X__, key=func)
'''
__Y__[の[各|][要素|値]をfuncに適用した結果でソートする
'''

alist.copy()
'''
@alt(複製する|コピーする)
alistを複製する
'''

reversed(__X__)
'''
@test_with(list(_))
@alt(反転する|逆順にする|リバースする|逆さにする)
__Y__を反転する
'''

all(__X__)
'''
__Y__[内の要素が]全て真かどうか
'''

any(__X__)
'''
__Y__[内の要素が]少なくとも一つ真かどうか
'''

print(*__X__)
'''
@test_with(None)
__Y__を[引数として展開して|]プリントする
'''

sum(__X__)
'''
@alt(フラット化する|flattenする)
__Y__をフラット化する
'''

enumerate(__X__)
'''
@test_with(list(_))
__Y__をナンバリングする
'''

enumerate(__X__, start=n)
'''
@test_with(list(_))
__Y__をnからナンバリングする
'''
