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
@prefix(aSet;セット)
@test(aSet=set([1,2]);$$;aSet)
{aSetに|elementを}追加する
'''

aSet.update(iterable)
'''
@test(aSet=set([1,2]);$$;aSet)
{aSetに|iterableの要素を[全て|]}追加する
{aSetに|iterableを}追加[更新|]する
'''

aSet.remove(element)
'''
@alt(取り除く|除く|除去する)
@test(aSet=set([1,2]);$$;aSet)
{aSetから|elementを}取り除く
'''

aSet.discard(element)
'''
@test(aSet=set([1,2]);$$;aSet)
{aSetから|エラーなく}elementを取り除く
'''

aSet.clear()
'''
@test(aSet=set([1,2]);$$;aSet)
aSetから[全[ての|]要素を|要素を全て][取り除く|消す]
aSetを[空|空集合]にする
'''

aSet.intersection_update(aSet2)
'''
@test(aSet=set([1,2]);aSet2=set([1,3]);$$;aSet)
aSetをaSet2との[共通要素|インターセクション][だけ|のみ]に[更新|]する
'''

aSet.difference_update(aSet2)
'''
@test(aSet=set([1,2]);aSet2=set([1,3]);$$;aSet)
aSetからaSet2[の要素|]を[全て|]取り除く
'''

aSet.symmetric_difference_update(aSet2)
'''
@test(aSet=set([1,2]);aSet2=set([1,3]);$$;aSet)
aSetからaSet2との共通要素を[全て|]取り除く
'''

aSet.pop()
'''
@test(aSet=set([1,2]);$$)
aSetから[任意の要素を|何でもいいから一つ][取り出す|取り除く]
'''

aSet.union(aSet2)
'''
@test(aSet=set([1,2]);aSet2=set([1,3]);$$)
aSetとaSet2の[和集合|ユニオン][|を求める|を得る]
aSet ∪ aSet2
'''

aSet.intersection(aSet2)
'''
@test(aSet=set([1,2]);aSet2=set([1,3]);$$)
aSetとaSet2の[積集合|共通部分|[交わり|交差]|インターセクション][|を求める|を得る]
aSetとaSet2に共通する要素からなる集合[|を求める|を得る]
aSet ∩ aSet2
'''

aList = aList2 = []
list(set(aList) & set(aList2))
'''
aListとaList2の[積集合|共通りスト|インターセクション][|を求める|を得る]
'''

aSet.difference(aSet2)
'''
@test(aSet=set([1,2]);aSet2=set([1]);$$)
aSetとaSet2の[差集合|差][|を求める|を得る]
aSetに含まれ、aSet2に含まれない集合[|を求める|を得る]
aSetからaSet2を引いた[差集合|差][|を求める|を得る]
aSetにおけるaSet2の補集合[|を求める|を得る]
aSet ＼ aSet2
'''

aSet.symmetric_difference(aSet2)
'''
@test(aSet=set([1,2]);aSet2=set([1]);$$)
aSetとaSet2の[対称差集合|対称差][|を求める|を得る]
aSetとaaSet2のいずれか一方だけの集合[|を求める|を得る]
'''

element in aSet
'''
@test(aSet=set([1,2]);$$)
elementが_aSetの[メンバー|要素][|に含まれる]かどうか
elementが_aSetに含まれるかどうか
element ∈ aSet
'''

element not in aSet
'''
@test(aSet=set([1,2]);$$)
elementが_aSetの[メンバー|要素][でない|に含まれない]かどうか
elementが_aSetに含まれないかどうか
element ∉ aSet
'''

aSet.issubset(aSet2)
'''
@test(aSet=set([1,2]);aSet2=set([1]);$$)
aSetが_aSet2の[部分集合|下位集合|サブセット]かどうか
aSetの全ての要素がaSet2に含まれるかどうか
aSet ⊆ aSet2
'''

aSet < aSet2
'''
@test(aSet=set([1,2]);aSet2=set([1]);$$)
aSetが_aSet2の真[部分集合|下位集合|サブセット]かどうか
aSet ⊂ aSet2
'''

aSet.issuperset(aSet2)
'''
@test(aSet=set([1,2]);aSet2=set([1]);$$)
aSetが_aSet2の[上位集合|スーパーセット]かどうか
aSet ⊇ aSet2
'''

aSet > aSet2
'''
@test(aSet=set([1,2]);aSet2=set([1]);$$)
aSetがaSet2の真[上位集合|スーパーセット]かどうか
aSet ⊃ aSet2
'''

aSet.isdisjoint(aSet2)
'''
@test(aSet=set([1,2]);aSet2=set([1]);$$)
aSetが_aSet2と共通の要素を持たないかどうか
aSetが_aSet2と交わりを持たないかどうか
aSetが_aSet2と互いに素かどうか
aSetとaSet2が_互いに素かどうか
'''

len(aSet)
'''
@test(aSet=set([1,2]);$$)
aSetの[濃度|要素数][|を求める]
'''

len(aSet) == 0
'''
@test(aSet=set([1,2]);$$)
aSetが[空|空集合]かどうか
'''

len(aSet) != 0
'''
@test(aSet=set([1,2]);$$)
aSetが[空|空集合]でないかどうか
'''

aSet.copy()
'''
@test(aSet=set([1,2]);$$)
aSetの浅いコピー[|を作る]
'''


frozenset(iterable)
'''
iterableのイミュータブルな集合_[|を得る|を作る]
iterableを[イミュータブルな|変更不能な|更新不能な]集合_に変換する
'''

frozenset(aSet)
'''
@test(aSet=set([1,2]);$$)
aSetの[イミュータブル|変更不能|更新不能]版
aSetを[イミュータブルな|変更不能な|更新不能な][セット|集合]に変換する
aSetを[イミュータブル|変更不能|更新不能]に変換する
'''

list(aSet)
'''
@test(aSet=set([1,2]);$$)
aSetをリストに変換する
'''

tuple(aSet)
'''
@test(aSet=set([1,2]);$$)
aSetを[タプル|組]に変換する
'''

aList = [1, 2]
sorted(set(aList), key=aList.index)
'''
aList[の|から]重複を取り除く
'''
