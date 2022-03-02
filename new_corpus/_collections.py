# collections

import collections
'''
[コレクション|collections][|モジュール]を[使う|インストールする]
'''
n = 1
iterable = [1, 2]

collections.deque()
'''
@alt(両端キュー|デック|deque[|オブジェクト])
{両端キューを|新たに}作る
'''

collections.deque(iterable)
'''
{iterableから|両端キューを|新たに}作る
iterableを|両端キューに変換する
'''

collections.deque(maxlen=n)
'''
@alt(両端キュー|デック|deque[|オブジェクト])
{最大長をnに[|制限]して|両端キューを|新たに}作る
{最大長nの両端キューを|新たに}作る
'''

deq = collections.deque()
element = 5

deq.appendleft(element)
'''
@prefix(deq;両端キュー)
@test(deq = collections.deque();_)
@alt(先頭|最初|左[|側])
{deqの先頭に|elementを}追加する
'''

deq.append(element)
'''
@test(deq = collections.deque();_)
@alt(末尾|最後|右[|側])
{deqの末尾に|elementを}追加する
'''

deq.insert(n, element)
'''
@alt(挿入する|[途中|]追加する)
{deqのn番目に|elementを}挿入する
'''

deq.popleft()
'''
@test(deq = collections.deque([1,2]);_)
@alt(取り除く|取り出す|削除する)
@alt(要素|値)
{deqの先頭から|要素を}取り除く
deqの先頭からポップする
'''

deq.pop()
'''
@test(deq = collections.deque([1,2]);_)
{deqの末尾から|要素を}取り除く
deq[|の末尾]からポップする
'''

deq.remove(element)
'''
@test(deq = collections.deque([1,2]);_)
{deqから|最初のelementを}取り除く
'''

deq.clear()
'''
@test(deq = collections.deque([1,2]);_)
@alt(空にする|クリアする|全て取り除く)
deqを空にする
'''

deq.rotate()
'''
@test(deq = collections.deque([1,2]);_)
@alt(ローテートする|[持ち|]回す)
@alt(順序|順[|番])
{deqの[要素|順序]を|[右に|]|[|一つ]}ローテートする
'''

deq.rotate(n)
'''
@test(deq = collections.deque([1,2]);_)
{deqの[要素|順序]を|[右に|]|n個分}ローテートする
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
deqの先頭の要素[|を得る]
'''

deq[-1]
'''
@test(deq = collections.deque([1,2]);_)
deqの末尾の要素[|を得る]
'''

deq[n]
'''
@test(deq = collections.deque([1,2]);_)
deqのn番目の要素[|を得る]
'''

deq.index(element)
'''
@test(deq = collections.deque([1,2]);_)
@alt(インデックス|位置)
deq中のelementのインデックス[|を得る]
'''

__X__ = list
__X__(deq.index)
'''
@test(deq = collections.deque([1,2]);_)
@X(list|tuple)
@Y(リスト|タプル)
deqを__Y__に変換する
'''

# カウンタ


collections.Counter()
'''
@alt(カウンタ|計数[オブジェクト|ツール])
{[|新しい][空の|]カウンタを|新たに}[作る|用意する]
'''

collections.Counter(iterable)
'''
{iterableから|[|新しい]カウンタを|新規に}作る
'''

amap = {'red': 4, 'blue': 2}
collections.Counter(amap)
'''
@test(amap={'A':2, 'B':1};X)
@prefix(amap;[辞書|カウンタ|マッピング])
{amapから|[|新しい]カウンタを|新規に}作る
'''

X = collections.Counter()
'''
@test(_;X)
{[|新しい][空の|]カウンタを|新たに}作って、Xに代入する
'''

X = collections.Counter(iterable)
'''
@test(_;X)
{iterableから|[|新しい]カウンタを|新規に}作って、Xに代入する
'''

X = collections.Counter(amap)
'''
@test(amap={'A':2, 'B':1};_;X)
{amapから|[|新しい]カウンタを|新規に}作って、Xに代入する
'''

c = collections.Counter()
c.elements()
'''
@test(c=collections.Counter(A=2,B=1);_)
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
cを[下位n個|下位n位まで]カウント[|の回数][が|の]少ない順に列挙する
cから低頻出[|な]項目をn個、リストとして得る
'''

c.most_common(1)[0]
'''
@test(c=collections.Counter(A=2,B=1);_)
@alt(最頻出|最も頻出|最もカウント数の多い)
cから最頻出の項目を[得る|求める]
'''

c.most_common(1)[1]
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
@test(c=collections.Counter(A=2,B=1);amap={'A':2, 'B':1}_)
cからamapを引く
'''

c[element] += 1
'''
c内のelement項目を[|一つ]増やす
'''

c[element]
'''
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
@test(c=collections.Counter(A=2,B=1);_)
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
