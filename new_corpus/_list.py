# list

aList = [1, 2, 3]
aList2 = [4, 5]
aTuple = (1, 2, 3)
aTuple2 = (4, 5)
element = 2
n = 1
n2 = 3
step = 2
iterable = [1, 2, 3]

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

(n, n2)
'''
bとn2から成るペア[|を作る]
'''

[element]
'''
[要素|element]一つのりスト[|を作る]
'''

[element] * n
'''
n個の[要素|element]があるリスト[|を作る]
'''

[0] * n
'''
長さnのリスト[|を作る]
'''

[[0] * n for _ in range(n2)]
'''
n2行n列の２次元リスト[|を作る]
n[×| x ]n2の２次元リスト[|を作る]
'''

tuple(aList)
'''
@alt(に変換する|[に|化]する)
aListを[タプル|組]に変換する
aListをイミュータブルにする
'''

list(aTuple)
'''
aTupleをリストに変換する
aTupleをミュータブルにする
'''

__X__ = aList
__X__2 = aList2

len(__X__)
'''
@alt(見る|調べる|知る|得る)
@alt(長さ|要素数|個数)
@X(aList|aTuple)
@Y(aList|aTuple)
__Y__の長さ[|を見る]
'''

len(aList) == 0
'''
aListが空かどうか
'''

len(aList) != 0
'''
aListが空でないかどうか
'''

__X__ + __X__2
'''
@alt(連結する|結合する|接続する|加える)
__Y__と__Y__2を連結する
'''

__X__ * n
'''
__Y__をn倍する
__Y__をn回、連結する
'''

__X__[0]
'''
@alt(先頭|最初)
@alt(末尾|最後)
__Y__の先頭[|の[要素|値]][|を得る]
'''

__X__[-1]
'''
__Y__の末尾[|の[要素|値]][|を得る]
'''

__X__[n]
'''
__Y__のn番目の[|の[要素|値]][|を得る]
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
{__Y__を|[ひとつ置きに|ひとつ飛ばしで]}取り出す
'''

__X__[n:n2]
'''
__Y__のn番目からn2番目[まで][の部分][|を取り出す]
'''

slice(n)
'''
[0から|]nまでのスライス
'''

slice(n, n2)
'''
nからn2までのスライス
'''

slice(n, n2, step)
'''
nからn2までのstepごとによるスライス
'''


sum(__X__)
'''
__Y__の[合計値|合計|総和][|を求める]
'''

min(__X__)
'''
@alt(一番|最も)
__Y__の中の[最小値|一番小さい値][|を求める]
'''

max(__X__)
'''
__Y__の中の[最大値|一番大きい値][|を求める]
'''

sum(__X__)/len(__X__)
'''
__Y__の[平均値|平均][|を求める]
'''

range(len(aList))
'''
@test(list(_))
aListの長さだけ繰り返す
'''

range(n)
'''
@test(list(_))
n[個|回]の数値イテラブル[|を得る]
0からnの範囲[|で|を得る]
'''

range(n, n2)
'''
@test(list(_))
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
nからn2までのひとつ飛ばしの数列[|を作る]
'''

list(range(2, n, 2))
'''
@alt(ひとつ飛ばし|一つ置き)
nまでの偶数列[|を作る]
'''

list(range(1, n, 2))
'''
@alt(ひとつ飛ばし|一つ置き)
nまでの奇数列[|を作る]
'''

aList.append(element)
'''
@test($$;aList)
@alt(追加する|加える)
aList[に|の末尾に][element|要素]を追加する
'''

aList.extend(aList2)
'''
@test($$;aList)
aList[に|の末尾に]aList2を[追加する|展開する]
aList[に|の末尾に]aList2を追加して[拡張する|広げる]
'''

aList.insert(n, element)
'''
@test($$;aList)
@alt(挿入する|差し込む)
aListのn番目にelementを挿入する
'''

aList.pop()
'''
@test($$;aList)
aListの末尾から[要素|値]を[ポップする|取り出す|取り除く]
'''

aList.pop(n)
'''
@test($$;aList)
aListn番目から[要素|値]を[ポップする|取り出す|取り除く]
'''

aList.clear()
'''
@test($$;aList)
@alt(消去する|消す)
aListの[全ての|全|][要素|値]を[クリアにする|取り除く|消去する|空にする]
'''

aList = [1, 2, 1]
element = 1

aList.remove(element)
'''
@test($$;aList)
aListからelement[|と等しい最初の要素]を取り除く
'''
aList = [1, 2, 1]
n = 1

del aList[n]
'''
@test($$;aList)
aListのn番目[の[要素|値]|]を[削除する|消す]
'''

element in __X__
'''
element[が|は]__Y__の要素かどうか
element[が|は]__Y__に含まれるかどうか
'''

element not in __X__
'''
element[が|は]__Y__の要素でないかどうか
element[が|は]__Y__に含まれないかどうか
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


aList.index(element) if element in aList else -1
'''
{aListのelementの位置を|エラーなく}得る
'''


def func(x): return x+1


sorted(__X__, key=func)
'''
__Y__の[各|][要素|値]をfuncに適用した結果でソートする
'''

aList.copy()
'''
@alt(複製する|コピーする)
aListを複製する
'''

reversed(__X__)
'''
@test(list(_))
@alt(反転する|逆順にする|リバースする|逆さにする)
__Y__を反転する
'''

all(__X__)
'''
__Y__[内の要素][が|は]全て真かどうか
'''

any(__X__)
'''
__Y__[内の要素][が|は]少なくとも一つ真かどうか
'''

print(*__X__)
'''
__Y__を[引数として展開して|順に]プリントする
'''

print(*__X__, sep=',')
'''
__Y__を[引数として展開して|カンマ区切りで]プリントする
'''

sum(__X__)
'''
@alt(フラット化する|flattenする)
２次元__Y__をフラット化する
'''

enumerate(__X__)
'''
@test(list(_))
@alt(ナンバリングする|番号付けする|順序付けする|順番付けする)
__Y__をナンバリングする
'''

enumerate(__X__, start=n)
'''
@test(list(_))
__Y__をnからナンバリングする
'''

filter(func, iterable)
'''
@alt(のそれぞれ||の各要素)
iterableのそれぞれをfuncでフィルタする
'''

map(func, iterable)
'''
iterableのそれぞれをpredicatefuncでフィルタする
'''
