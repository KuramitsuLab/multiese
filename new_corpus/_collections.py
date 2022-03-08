# collections

import itertools
import typing

import collections
'''
@test(_;type(collections))
@alt(両端キュー|[双方向キュー|デック]|[キュー|スタック]|deque[|オブジェクト])
@alt(名前付きタプル|[構造体|簡易クラス])
[コレクション|両端キュー|カウンタ|名前付きタプル]を使う
'''

n = 1
iterable = [1, 2]

collections.deque()
'''
{[空の|]両端キューを|新たに}作る
'''

collections.deque(iterable)
'''
{iterableから|両端キューを|新たに}作る
iterableを両端キューに変換する
'''

collections.deque(maxlen=n)
'''
@alt(最大長|上限[|長||制限された長さ])
{最大長をnに[|制限]して|両端キューを|新たに}作る
{最大長nの両端キューを|新たに}作る
'''

collections.deque(iterable, maxlen=n)
'''
@alt(テイルフィルタ|tailフィルタ)
{最大長をnに[|制限]して|iterableから|両端キューを|[|新たに]}作る
{最大長nの両端キューを|iterableから|[|新たに]}作る
iterableのテイルフィルタを作る
'''

X = collections.deque()
'''
@test(_;X)
{[空の|]両端キューを|新たに}作って、Xに代入する
'''

X = collections.deque(iterable)
'''
@test(_;X)
{iterableから|両端キューを|新たに}作って、Xに代入する
'''

X = collections.deque(maxlen=n)
'''
@test(_;X)
{最大長をnに[|制限]して|両端キューを|新たに}作って、Xに代入する
{最大長nの両端キューを|新たに}作る
'''

X = collections.deque(iterable, maxlen=n)
'''
@test(_;X)
{最大長をnに[|制限]して|iterableから|両端キューを|[|新たに]}作って、Xに代入する
{最大長nの両端キューを|iterableから|[|新たに]}作って、Xに代入する
'''

deq = collections.deque()
element = 5

deq.appendleft(element)
'''
@prefix(deq;デック)
@test(deq = collections.deque();_;deq)
@alt(先頭|最初|左[|側])
@alt(追加する|[付け|つけ]加える)
@alt(エンキューする|enqueueする|データを入れる)
{deqの先頭に|elementを}追加する
{deqに|elementを}エンキューする
'''

deq.append(element)
'''
@test(deq = collections.deque();_;deq)
@alt(末尾|最後|右[|側])
@alt(プッシュする|詰む|スタックする)
{deqの末尾に|elementを}追加する
{deqに|elementを}プッシュする
'''

deq.extendleft(iterable)
'''
@prefix(deq;デック)
@test(deq = collections.deque();_;deq)
@alt(要素|[値|データ])
{deqの先頭に|iterableの[各|]要素を[|順に]}追加する
'''

deq.extend(iterable)
'''
@test(deq = collections.deque();_;deq)
{deqの末尾に|iterableの[各|]要素を[|順に]}追加する
'''

deq.insert(n, element)
'''
@test(deq = collections.deque();_;deq)
@alt(挿入する|[途中|]追加する)
{deqのn番目に|elementを}挿入する
'''

deq.popleft()
'''
@test(deq = collections.deque([1,2]);_;deq)
@alt(取り除く|取り出す|削除する)
@alt(デキューする|dequeue|要素を出す)
{deqの先頭から|要素を}取り除く
deqをデキューする
'''

deq.pop()
'''
@test(deq = collections.deque([1,2]);_;deq)
{deqの末尾から|要素を}取り除く
deq[を|から]ポップする
'''

deq.remove(element)
'''
@test(deq = collections.deque([1,2]);_;deq)
{deqから|最初のelementを}取り除く
'''

deq.clear()
'''
@test(deq = collections.deque([1,2]);_;deq)
@alt(空にする|クリアする|全て取り除く)
deqを空にする
'''

deq.rotate()
'''
@test(deq = collections.deque([1,2]);_;deq)
@alt(ローテートする|[持ち|]回す|ローテーションする)
@alt(順序|順[|番])
{deqの[要素|順序]を|[右に|]|[|一つ]}ローテートする
'''

deq.rotate(n)
'''
@test(deq = collections.deque([1,2]);_;deq)
{deqの[要素|順序]を|[右に|]|n個分}ローテートする
'''

deq.rotate(-n)
'''
@test(deq = collections.deque([1,2]);_;deq)
{deqの[要素|順序]を|左に|n個分}ローテートする
'''

deq.maxlen
'''
@test(deq = collections.deque([1,2],maxlen=2);_)
deqの最大長[|を得る]
'''

len(deq)
'''
@test(deq = collections.deque([1,2]);_)
deqの[大きさ|要素数|サイズ|長さ][|を求める]
'''

len(deq) == 0
'''
@test(deq = collections.deque([1,2]);_)
deqが_空[|である]かどうか
'''

len(deq) != 0
'''
@test(deq = collections.deque([1,2]);_)
deqが_空でないかどうか
'''

element in deq
'''
@test(deq = collections.deque([1,2]);_)
@alt(含まれてる|存在する|ある)
deqの中にelementが_含まれてるかどうか
'''

deq[0]
'''
@test(deq = collections.deque([1,2]);_)
deqの先頭[|の要素][|を得る]
'''

deq[-1]
'''
@test(deq = collections.deque([1,2]);_)
deqの末尾[|の要素][|を得る]
'''

deq[n]
'''
@test(deq = collections.deque([1,2]);_)
deqのn番目[|の要素][|を得る]
'''

collections.deque(itertools.islice(deq, n, n2))
'''
@test(deq = collections.deque([1,2,1,2,1,2]);_)
deqのn〜n2の[部分|]要素[|を得る]
deqのn番目からn2[番目[|まで]]の[部分|]要素[|を得る]
'''

deq.index(element)
'''
@test(deq = collections.deque([1,2]);_)
@alt(インデックス|位置)
deq中のelementのインデックス[|を得る]
'''

deq.count(element)
'''
@test(deq = collections.deque([1,2]);_)
@alt(数える|数える)
deq中のelement[の[数|出現数]を数える
'''

deq.reverse()
'''
@test(deq = collections.deque([1,2]);_;deq)
@alt(反転する|逆順にする|逆に並べ直す)
{deqの要素を|[インプレースに|]}反転する
'''

reversed(deq)
'''
@test(deq = collections.deque([1,2]);list(_))
逆順のdeqを得る
'''

__X__ = list
__X__(deq)
'''
@test(deq = collections.deque([1,2]);_)
@X(list|tuple)
@Y(リスト|タプル)
deqを__Y__に変換する
'''

# カウンタ


collections.Counter()
'''
@alt(多重集合|カウンタ|多重集合|計数[オブジェクト|ツール]|カウンタ)
{[|新しい][空の|]多重集合を|新たに}[作る|用意する]
'''

collections.Counter(iterable)
'''
{iterableから|[|新しい]多重集合を|新規に}作る
'''

amap = {'red': 4, 'blue': 2}
collections.Counter(amap)
'''
@test(amap={'A':2, 'B':1};_)
@prefix(amap;[辞書|カウンタ|マッピング])
{amapから|[|新しい]多重集合を|新規に}作る
'''

X = collections.Counter()
'''
@test(_;X)
{[|新しい][空の|]多重集合を|新たに}作って、Xに代入する
'''

X = collections.Counter(iterable)
'''
@test(_;X)
{iterableから|[|新しい]多重集合を|新規に}作って、Xに代入する
'''

X = collections.Counter(amap)
'''
@test(amap={'A':2, 'B':1};_;X)
{amapから|[|新しい]多重集合を|新規に}作って、Xに代入する
'''

c = collections.Counter()
c.elements()
'''
@test(c=collections.Counter(A=2,B=1);list(_))
@prefix(c;カウンタ)
@alt(それぞれの|各|)
@alt(カウント|出現)
@alt(の回数|[回|]数|分の回数)
@alt(列挙する|リストとして得る)
@alt(項目|[要素|キー]|[文字列|値])
cのそれぞれの項目を[、その|]カウントの回数だけ列挙する
'''

c.most_common()
'''
@test(c=collections.Counter(A=2,B=1);_)
@alt(順に|順番に|方から)
cをカウント[|の回数][が|の]多い順に列挙する
cを高頻出[|な]順に列挙する
'''

c.most_common()[::-1]
'''
@test(c=collections.Counter(A=2,B=1);_)
cをカウント[|の回数][が|の]少ない順に列挙する
cを低頻出[|な]順に列挙する
'''

c.most_common(n)
'''
@test(c=collections.Counter(A=2,B=1);_)
cを[上位n個|上位n位まで]カウント[|の回数][が|の]多い順に列挙する
cから高頻出[|な]項目をn個、リストとして得る
'''

c.most_common()[:-n-1:-1]
'''
@test(c=collections.Counter(A=2,B=1);_)
cを[下位n個|下位n位まで]カウント[|の回数][が|の]少ない順に列挙する
cから低頻出[|な]項目をn個、リストとして得る
'''

c.most_common(0)[0]
'''
@test(c=collections.Counter(A=2,B=1);_)
@alt(最頻出|最も頻出|最もカウント数の多い)
cから最頻出の項目を[得る|求める]
'''

c.most_common(0)[1]
'''
@test(c=collections.Counter(A=2,B=1);_)
cから最頻出の項目の回数を[得る|求める]
'''

c.update(iterable)
'''
@test(c=collections.Counter(iterable);_)
@alt(追加する|増やす)
{cに|iterable[|のカウント[|の回数]]を}追加する
'''

c.update(amap)
'''
@test(c=collections.Counter(A=2,B=1);amap={'A':2, 'B':1};_)
{cに|amapを}追加する
'''

c.subtract(iterable)
'''
@test(c=collections.Counter(iterable);_)
@alt(引く|減らす)
{cから|iterable[|のカウント[|の回数]]を}引く
'''

c.subtract(amap)
'''
@test(c=collections.Counter(A=2,B=1);amap={'A':2, 'B':1};_)
cからamapを引く
'''

c[element] += 1
'''
@test(c=collections.Counter(iterable);_;c[element])
c内のelement項目を[|一つ]増やす
'''

c[element]
'''
@test(c=collections.Counter(iterable);_)
c内のelement項目のカウント[|の回数][|を得る]
'''

c.total()
'''
@test(c=collections.Counter(A=2,B=1);_)
@alt(トータル|全)
cのトータルカウント[|の回数][|を得る]
cの全数[|を得る]
'''

c.keys()
'''
@test(c=collections.Counter(A=2,B=1);_)
cの項目一覧[|を得る]
'''

len(c)
'''
@test(c=collections.Counter(A=2,B=1);_)
cの項目数[|を得る]
'''

c.clear()
'''
@test(c=collections.Counter(A=2,B=1);_;c)
cを[リセット|クリア|ゼロに]する
'''

list(c)
'''
@test(c=collections.Counter(A=2,B=1);_)
cのユニークな項目を列挙する
cをリストに変換する
'''

set(c)
'''
@test(c=collections.Counter(A=2,B=1);_)
cを[集合|セット]に変換する
'''

dict(c)
'''
@test(c=collections.Counter(A=2,B=1);_)
cを辞書に変換する
'''

c.items()
'''
@test(c=collections.Counter(A=2,B=1);_)
cをペアリストに変換する
'''

pairs = [('A', 1)]
collections.Counter(dict(pairs))
'''
@test(pairs=[('A',1)];_)
ペアリストpairsからカウンタを[作る|構築する]
'''

+c
'''
@test(c=collections.Counter(A=2,B=1);_)
cから0[以下の|]カウントを取り除く
cの正の[数|カウント][のみ|だけ]残す
'''

c2 = c
c & c2
'''
@test(c=collections.Counter(A=2,B=1);c2=c;_)
@alt(インターセクション|積集合|共通部分|[交わり|交差]|インターセクション)
cとc2のインターセクション[|を求める|を得る]
cとc2に共通する要素からなる多重集合[|を求める|を得る]
c∩c2 
'''

c | c2
'''
@test(c=collections.Counter(A=2,B=1);c2=c;_)
@alt(ユニオン|和集合)
cとc2のユニオン[|を求める|を得る]
c∪c2 
'''

alist3 = ['A', 'B']
collections.namedtuple(s, alist3)
'''
sの名前を持ち、alist3のプロパティ[を持った|のある]名前付きタプルを[定義する|作る]
'''

collections.namedtuple(s, s2)
'''
sの名前を持ち、s2のプロパティ[を持った|のある]名前付きタプルを[定義する|作る]
'''

C = collections.namedtuple('P', 'x y z', defaults=[0])
issubclass(C, tuple)
'''
@test(C=collections.namedtuple('C', 'x y z w');_)
クラスCが_名前付きタプルかどうか
'''

C._make(iterable)  # issubclass(C, tuple)
'''
@test(C=collections.namedtuple('C', 'x y z w');_)
@alt(のインスタンス|[オブジェクト])
{iterableから|クラスCのインスタンスを|新たに}作る
iterableをクラスCのインスタンスに変換する
'''

obj = C(1, 2, 3)
hasattr(obj, '_asdict') and hasattr(obj, '_fields')
'''
@test(C=collections.namedtuple('C', 'x y');obj=C(1,2);_)
objが名前付きタプル[|型|のインスタンス]かどうか
'''

obj._asdict()  # isinstance(obj, NamedTuple)
'''
@test(C=collections.namedtuple('C', 'x y');obj=C(1,2);_)
[名前付きタプル|]objを辞書に変換する
'''

obj._fields  # isinstance(obj, NamedTuple)
'''
@test(C=collections.namedtuple('C', 'x y');obj=C(1,2);_)
[名前付きタプル|]objのフィールド名の一覧[|を得る]
'''

collections.ChainMap()
'''
@alt(チェーンマップ|階層化された[マッピング|辞書])
[空|ルート]のチェーンマップを作成する
'''

collections.ChainMap(adict)
'''
@alt(チェーンマップ|[階層化された|ネストされた][マッピング|辞書])
@alt(階層化する|ネスト化する)
adictをチェーンマップに変換する
adictを階層化する
'''

collections.ChainMap(adict, adict2)
'''
@alt(チェーンする|階層的につなぐ|ネストする)
adictとadict2をチェーンする
'''
