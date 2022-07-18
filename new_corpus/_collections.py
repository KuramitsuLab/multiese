# collections
from importlib import import_module

import collections
'''
@alt(両端キュー=[両端キュー|双方向キュー|[キュー|スタック|デック]])

[コレクション|データ構造|両端キュー|カウンタ|名前付きタプル]を使う
'''

itertools = import_module('itertools')
typing = import_module('typing')
collections = import_module('collections')

n = 1
iterable = [1, 2]
element = 1
deq = collections.deque([1, 2])
names = ['A', 'B']


両端キュー = collections.deque()
'''
[空の|]両端キュー[|を作る]
両端キュー[|が欲しい]
'''

最大長 = 10

collections.deque(maxlen=最大長)
'''
@alt(最大長|上限[|長||制限された長さ])

両端キューの長さを制限する
最大長[を指定して、|のある]両端キュー[|を作る]
最大長nの両端キューを作る
'''

__X__ = 1
'''
@X(要素;整数;文字列)
@Y(要素;整数;文字列)
'''

両端キュー.appendleft(__X__)
'''
@alt(先頭|最初|左[|側])
@alt(追加する|[付け|つけ]加える|入れる)

{両端キューの先頭に|__Y__を}追加する
'''

両端キュー.append(__X__)
'''
@alt(末尾|最後|右[|側])
@alt(プッシュする|積む|スタックする)
@alt(エンキューする|enqueueする)

{両端キューの末尾に|__Y__を}追加する
{両端キューに|__Y__を}エンキューする
{両端キューに|__Y__を}プッシュする
'''

両端キュー.insert(n, __X__)
'''
@alt(挿入する|差し込む|[途中|]追加する)

{両端キューのn番目に|__Y__を}挿入する
'''

両端キュー.popleft()
'''
@alt(デキューする|dequeue|要素を出す)

{両端キューの先頭から|要素を}取り出す
両端キュー[を|から]デキューする
'''

両端キュー.pop()
'''
{両端キューの末尾から|要素を}取り出す
両端キュー[を|から]ポップする
'''

両端キュー.remove(__X__)
'''
@alt(取り除く|削除する)

{両端キューから|[最初の|]__Y__を}取り除く
'''

両端キュー.clear()
'''
@alt(空にする|クリアする|全て取り除く)

両端キューを空にする
'''

deq = collections.deque([1, 2, 3, 0], maxlen=5)

両端キュー.rotate(1)
'''
@alt(ローテーションする|回転させる|輪番で回す)
@alt(順序|順[|番])

{両端キューの[要素|順序]を|[右に|]}ローテーションする
'''

両端キュー.rotate(-1)
'''
{両端キューの[要素|順序]を|左に}ローテーションする
'''

両端キュー.maxlen
'''
両端キューの最大長[|を得る]
'''

len(両端キュー)
'''
両端キューの[大きさ|要素数|サイズ|長さ][|を求める]
'''

len(両端キュー) == 0
'''
両端キュー[が|は]空[|である]かどうか
'''

len(両端キュー) != 0
'''
両端キュー[が|は]空でないかどうか
'''

element = 1
deq = collections.deque([1, 2, 3])

__X__ in 両端キュー
'''
@alt(含まれてる|存在する|ある)

{両端キューの中に|__Y__[が|は]}含まれてるかどうか
'''

両端キュー[0]
'''
両端キューの先頭[|の要素][|を得る]
'''

両端キュー[-1]
'''
deqの末尾[|の要素][|を得る]
'''

両端キュー[n]
'''
deqのn番目[|の要素][|を得る]
'''

deq = collections.deque([1, 2, 1, 2, 1, 2])
start = 1
end = 3

collections.deque(itertools.islice(deq, start, end))
'''
deqから[部分|指定された範囲]を取り出す
deqのstart〜endの[部分|]要素[|を得る]
deqのstart番目からend[番目[|まで]]の[部分|]要素[|を得る]
'''

両端キュー.index(__X__)
'''
@alt(インデックス|位置)

両端キュー中の__Y__のインデックス[|を得る]
'''

両端キュー.count(__X__)
'''
@alt(数える|カウントする)

両端キュー中の__X__[の[数|出現数]]を数える
'''

両端キュー.reverse()
'''
@alt(反転する|逆順にする|逆に並べ直す)

{両端キューの要素を|[インプレースに|]}反転する
'''

reversed(両端キュー)
'''
逆順の両端キュー[|を得る]
'''

__X__ = list

__X__(両端キュー)
'''
@X(list|tuple|set)
@Y(リスト|タプル|セット)

両端キューを__Y__に変換する
'''

# カウンタ

collections.Counter()
'''
@alt(多重集合=[カウンタ|多重集合|計数器])

[空の|]多重集合[|を作る]
'''

collections.Counter(iterable)
'''
{iterableから|[|新しい]多重集合を}作る
iterableを多重集合に変換する
'''

aDict = {'A': 0, 'B': 1}

collections.Counter(aDict)
'''
{aDictから|多重集合を}作る
aDictを多重集合に変換する
'''

aCounter = collections.Counter(A=2, B=1)
aCounter2 = aCounter

aCounter.elements()
'''
@prefix(aCounter;カウンタ)
@alt(それぞれの|各|)
@alt(カウント=[カウント|[出現|]回数])
@alt(の回数|[回|]数|分の回数)
@alt(列挙する|リストとして得る)
@alt(項目|[要素|キー]|[文字列|値])

aCounterのそれぞれの項目を[、その|]カウントだけ列挙する
'''

aCounter.most_common()
'''
@alt(順に|順番に|方から)

{aCounterを|[高頻出|高頻度][|な]方から}列挙する
{aCounterを|多い順に}列挙する
'''

aCounter.most_common()[::-1]
'''
{aCounterを|少ない順に}列挙する
{aCounterを|[低頻出|低頻度][|な]方から}列挙する
'''

k = 10

aCounter.most_common(k)
'''
aCounterの[上位|ktop|Kトップ]を列挙する
'''

aCounter.most_common()[:-n-1:-1]
'''
aCounterの[下位|ボトム]を列挙する
'''

aCounter = collections.Counter([1, 1, 1, 1, 2, 2, 2, 3, 3])

aCounter.most_common()[0]
'''
@alt(最頻出|最も頻出)

aCounterの最頻出[な|の]項目[|を求める]
'''

aCounter.most_common()[1]
'''
aCounterから最頻出[な|の]項目の件数[|を求める]
'''

aCounter.update(iterable)
'''
@alt(追加する|増やす)

{aCounterを|iterableで_}更新する
{iterableをカウントして、|aCounterを}更新する
'''

aCounter.update(aDict)
'''
{aCounterを|aDictで_}更新する
'''

aCounter.subtract(iterable)
'''
@alt(引く|減らす)

{aCounterから|iterableをカウントして}引く
'''

aCounter.subtract(aDict)
'''
aCounterからaDictを引く
'''

aCounter[element] += 1
'''
aCounterの項目を[|一つ]増やす
'''

aCounter[element]
'''
aCounterの項目のカウント[|を得る]
'''

aCounter.total()
'''
@alt(トータル|全)
aCounterの[全数|全カウント][|を得る]
'''

aCounter.keys()
'''
aCounterの項目一覧[|を得る]
aCounterの項目を列挙する
'''

len(aCounter)
'''
aCounterの項目数[|を得る]
'''

aCounter.clear()
'''
aCounterを[リセット|クリア|ゼロに]する
'''

list(aCounter)
'''
aCounterのユニークな項目を列挙する
aCounterをリストに変換する
'''

set(aCounter)
'''
aCounterを[集合|セット]に変換する
'''

dict(aCounter)
'''
aCounterを辞書に変換する
'''

aCounter.items()
'''
aCounterのキーとカウントを列挙する
'''

pairs = [('A', 1)]

collections.Counter(dict(pairs))
'''
ペアリストpairsからカウンタを[作る|構築する]
'''

+aCounter
'''
aCounterからゼロカウントを取り除く
aCounterの正の[数|カウント][のみ|だけ]残す
'''

aCounter2 = collections.Counter(A=1, B=1)

aCounter & aCounter2
'''
@alt(インターセクション=[積集合|共通部分|[交わり|交差]|インターセクション|∩])
@alt(同士で|間で|の)

aCounter同士でインターセクション[|を求める]
２つのaCounterの共通する要素[|を求める]
aCounter同士でインターセクション演算する
'''

aCounter | aCounter2
'''
@alt(ユニオン|和集合|∪)

aCounter同士でユニオン[|を求める]
２つのaCounterのいずれかに含まれる要素[|を求める]
aCounter同士でユニオン演算する
'''

name = 'A'
name2 = 'B'

クラス名 = 'C'
プロパティ名 = ['A', 'B']

C = collections.namedtuple('クラス名', プロパティ名)
'''
名前付きタプルを定義する
'''

issubclass(C, tuple)
'''
@prefix(C;[クラス|型|クラス名])

C[が|は]名前付きタプルかどうか
'''

パラメータ = (1, 2, 3)

C._make(パラメータ)
'''
@alt(パラメータ|引数|データ)

{名前付きタプルを|パラメータから}インスタンス化する
'''

obj = C(1, 2, 3)

hasattr(obj, '_asdict') and hasattr(obj, '_fields')
'''
objが名前付きタプル[|型|のインスタンス]かどうか
'''

aNamedTupleObject = C(1, 2, 3)

aNamedTupleObject._asdict()
'''
名前付きタプルを辞書に変換する
'''

###

collections.ChainMap()
'''
@alt(チェーンマップ|階層化[マップ|辞書])

[空|ルート]のチェーンマップ[|を作る]
'''

collections.ChainMap(aDict)
'''
@alt(チェーンマップ|階層化[マップ|辞書])
@alt(階層化する|ネスト化する)

aDictをチェーンマップに変換する
aDictを階層化する
'''

aDict2 = {'C': 3}

collections.ChainMap(aDict, aDict2)
'''
@alt(チェーンする|階層的につなぐ|ネストする)

２つのaDictをチェーンする
２つのaDictを階層化する
'''
