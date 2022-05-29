# 集合

iterable = [0, 1, 2, 4]
aSet = {1, 2, 3}
aSet2 = {8, 9}
element = 1

set()
'''
@alt(集合_|セット)

空[の|]集合_[|を[得る|作る]]
'''

set(iterable)
'''
iterable[の|から]集合_[|を[得る|作る]]
iterableから重複を取り除く
iterableを集合_に変換する
'''

aSet.add(element)
'''
@prefix(aSet;[集合|セット])
@prefix(element;[要素|値])

{aSetに|elementを}追加する
'''

aSet.update(iterable)
'''
{aSetに|iterableの要素を[全て|]}追加する
{aSetに|iterableを}追加[更新|]する
'''

aSet.remove(element)
'''
@alt(取り除く|除く|除去する)

{aSetから|elementを}取り除く
'''

aSet.discard(element)
'''

{aSetから|エラーなく}elementを取り除く
'''

aSet.clear()
'''
aSetから[全[ての|]要素を|要素を全て][取り除く|消す]
aSetを[空|空集合]にする
'''

aSet.intersection_update(aSet2)
'''
二つの集合の[共通要素|インターセクション][だけ|のみ]に[更新|]する
'''

aSet.difference_update(aSet2)
'''
aSetから別のaSet2[の要素|]を[全て|]取り除く
'''

aSet.symmetric_difference_update(aSet2)
'''
aSetから別のaSet2との共通要素を[全て|]取り除く
'''

aSet.pop()
'''
aSetから[任意の要素を|何でもいいから一つ][取り出す|取り除く]
'''

aSet.union(aSet2)
'''
二つの集合の[和集合|ユニオン|∪][|を求める|を得る]
'''

aSet.intersection(aSet2)
'''
二つの集合の[積集合|共通部分|[交わり|交差]|∩|インターセクション][|を求める|を得る]
二つの集合に共通する要素からなる集合[|を求める|を得る]
'''

aList = aList2 = []
list(set(aList) & set(aList2))
'''
二つのリストの[積集合|共通りスト|インターセクション][|を求める|を得る]
'''

aSet.difference(aSet2)
'''
二つの集合の[差集合|差][|を求める|を得る]
一方に含まれ、他方に含まれない集合[|を求める|を得る]
aSetの補集合[|を求める|を得る]
aSet ＼ aSet2
'''

aSet.symmetric_difference(aSet2)
'''
二つの集合の[対称差集合|対称差][|を求める|を得る]
二つの集合のいずれか一方だけの集合[|を求める|を得る]
'''

element in aSet
'''
element[が|は]aSetの[メンバー|要素][|に含まれる]かどうか
element[が|は]aSetに含まれるかどうか
element ∈ aSet
'''

element not in aSet
'''
@test(aSet=set([1,2]);$$)
element[が|は]aSetの[メンバー|要素][でない|に含まれない]かどうか
element[が|は]aSetに含まれないかどうか
element ∉ aSet
'''

aSet.issubset(aSet2)
'''
[|二つの関係が][部分集合|下位集合|サブセット|⊆]かどうか
aSetの全ての要素が別のaSet2に含まれるかどうか
'''

aSet < aSet2
'''
[|二つの関係が]真[部分集合|下位集合|サブセット|⊂]かどうか
'''

aSet.issuperset(aSet2)
'''
[|二つの関係が][上位集合|スーパーセット]かどうか
'''

aSet > aSet2
'''
[|二つの関係が]真[上位集合|スーパーセット]かどうか
[|二つの関係が][上位集合|スーパーセット]もしくは等しいかどうか
'''

aSet.isdisjoint(aSet2)
'''
@test(aSet=set([1,2]);aSet2=set([1]);$$)
二つの集合[が|は]共通の要素を持たないかどうか
二つの集合[が|は]aSet2と交わりを持たないかどうか
二つの集合[が|は]aSet2と互いに素かどうか
二つの集合[が|は]互いに素かどうか
'''

len(aSet)
'''
aSetの[濃度|要素数][|を求める]
'''

len(aSet) == 0
'''
aSetが[空|空集合]かどうか
'''

len(aSet) != 0
'''
aSetが[空|空集合]でないかどうか
'''

aSet.copy()
'''
aSetの浅いコピー[|を作る]
'''


frozenset(iterable)
'''
iterableのイミュータブルな集合_[|を得る|を作る]
iterableを[イミュータブルな|変更不能な|更新不能な]集合_に変換する
'''

frozenset(aSet)
'''
aSetの[イミュータブル|変更不能|更新不能]版
aSetを[イミュータブルな|変更不能な|更新不能な][セット|集合]に変換する
aSetを[イミュータブル|変更不能|更新不能]に変換する
'''

list(aSet)
'''
aSetをリストに変換する
'''

tuple(aSet)
'''
aSetを[タプル|組]に変換する
'''

aList = [1, 2]
sorted(set(aList), key=aList.index)
'''
aList[の|から]重複を取り除く
'''
