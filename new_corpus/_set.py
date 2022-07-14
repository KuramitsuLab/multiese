# 集合

iterable = [0, 1, 2, 4]
セット = {1, 2, 3}
セット2 = {8, 9}
要素 = 1

set()
'''
@alt(集合_|セット)

空[の|]集合_[|を[得る|作る]]
'''

# 要素

要素 = 1

__X__ = 1
'''
@X(要素;数;文字列)
@Y([要素|項];[整数|数値];文字列)
'''

セット.add(__X__)
'''
{セットに|__Y__を}追加する
'''

セット.remove(__X__)
'''
@alt(取り除く|除く|除去する)

{セットから|__Y__を}取り除く
'''

セット.discard(__X__)
'''
{セットから|[エラー|例外]なく}__Y__を取り除く
'''

__X__ in セット
'''
__Y__[が|は]セットの[メンバー|要素][|に含まれる]かどうか
__Y__[が|は]セットに含まれるかどうか
__Y__[が|は]セットのいずれかどうか
__Y__ ∈ セット
'''

__X__ not in セット
'''
__Y__[が|は]セットの[メンバー|要素][でない|に含まれない]かどうか
__Y__[が|は]セットに含まれないかどうか
__Y__[が|は]セットのいずれでもないどうか
__Y__ ∉ セット
'''

リスト = [1, 0]

セット.update(リスト)
'''
{セットに|リストの要素を[全て|]}追加する
{セットに|iterableを}追加[更新|]する
'''

セット.clear()
'''
セットから[全[ての|]要素を|要素を全て][取り除く|消す]
セットを[空|空集合]にする
'''

セット.intersection_update(セット2)
'''
セットを[別のセットとの|][共通要素|インターセクション][だけ|のみ]に[更新|]する
'''

セット.difference_update(セット2)
'''
セットを[別のセットとの|]差分[だけ|のみ]に[更新|]する
セットからセットセット2[の要素|]を[全て|]取り除く
'''

セット.symmetric_difference_update(セット2)
'''
セットから別のセット2との共通要素を[全て|]取り除く
'''

セット.pop()
'''
セットから[任意の要素を|何でもいいから一つ]取り出す
'''

セット.union(セット2)
'''
二つの集合の[和集合|ユニオン|∪][|を求める|を得る]
'''

セット.intersection(セット2)
'''
二つの集合の[積集合|共通部分|[交わり|交差]|∩|インターセクション][|を求める|を得る]
二つの集合に共通する要素からなる集合[|を求める|を得る]
'''

aList = aList2 = []
list(set(aList) & set(aList2))
'''
二つのリストの[積集合|共通りスト|インターセクション][|を求める|を得る]
'''

セット.difference(セット2)
'''
二つの集合の[差集合|差][|を求める|を得る]
一方に含まれ、他方に含まれない集合[|を求める|を得る]
セットの補集合[|を求める|を得る]
セット ＼ セット2
'''

セット.symmetric_difference(セット2)
'''
二つの集合の[対称差集合|対称差][|を求める|を得る]
二つの集合のいずれか一方だけの集合[|を求める|を得る]
'''


セット.issubset(セット2)
'''
[|二つの関係が][部分集合|下位集合|サブセット|⊆]かどうか
セットの全ての要素が別のセット2に含まれるかどうか
'''

セット < セット2
'''
[|セットが]真[部分集合|下位集合|サブセット|⊂]かどうか
'''

セット.issuperset(セット2)
'''
[|セットが][上位集合|スーパーセット]かどうか
'''

セット >= セット2
'''
[|セットが][上位集合|スーパーセット]もしくは等しいかどうか
'''

セット.isdisjoint(セット2)
'''
二つのセット[が|は]共通の要素を持たないかどうか
[二|２]つのセット[が|は]交わりを持たないかどうか
二つのセット[が|は][互いに素|disjoint]かどうか
'''

len(セット)
'''
セットの[濃度|要素数][|を求める]
'''

len(セット) == 0
'''
セットが[空|空集合]かどうか
'''

len(セット) != 0
'''
セットが[空|空集合]でないかどうか
'''

セット.copy()
'''
セットの[浅い|]コピー[|を作る]
セットをコピーする
'''

frozenset(セット)
'''
セットの[イミュータブル|変更不能|更新不能]版
セットを[イミュータブルな|変更不能な|更新不能な][セット|集合]に変換する
セットを[イミュータブル|変更不能|更新不能]に変換する
'''

list(セット)
'''
セットをリストに変換する
'''

tuple(セット)
'''
セットを[タプル|組]に変換する
'''

リスト = [1, 2]
sorted(set(リスト), key=リスト.index)
'''
[順序を保持しながら|]リスト[の|から]重複を取り除く
'''
