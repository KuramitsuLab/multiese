# 集合

iterable = [0, 1, 2, 4]
aset = {1, 2, 3}
aset2 = {8, 9}
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

aset.add(element)
'''
@prefix(aset;セット)
@test(aset=set([1,2]);$$;aset)
{asetに|elementを}追加する
'''

aset.update(iterable)
'''
@test(aset=set([1,2]);$$;aset)
{asetに|iterableの要素を[全て|]}追加する
{asetに|iterableを}追加[更新|]する
'''

aset.remove(element)
'''
@alt(取り除く|除く|除去する)
@test(aset=set([1,2]);$$;aset)
{asetから|elementを}取り除く
'''

aset.discard(element)
'''
@test(aset=set([1,2]);$$;aset)
{asetから|エラーなく}elementを取り除く
'''

aset.clear()
'''
@test(aset=set([1,2]);$$;aset)
asetから[全[ての|]要素を|要素を全て][取り除く|消す]
asetを[空|空集合]にする
'''

aset.intersection_update(aset2)
'''
@test(aset=set([1,2]);aset2=set([1,3]);$$;aset)
asetをaset2との[共通要素|インターセクション][だけ|のみ]に[更新|]する
'''

aset.difference_update(aset2)
'''
@test(aset=set([1,2]);aset2=set([1,3]);$$;aset)
asetからaset2[の要素|]を[全て|]取り除く
'''

aset.symmetric_difference_update(aset2)
'''
@test(aset=set([1,2]);aset2=set([1,3]);$$;aset)
asetからaset2との共通要素を[全て|]取り除く
'''

aset.pop()
'''
@test(aset=set([1,2]);$$)
asetから[任意の要素を|何でもいいから一つ][取り出す|取り除く]
'''

aset.union(aset2)
'''
@test(aset=set([1,2]);aset2=set([1,3]);$$)
asetとaset2の[和集合|ユニオン][|を求める|を得る]
aset ∪ aset2
'''

aset.intersection(aset2)
'''
@test(aset=set([1,2]);aset2=set([1,3]);$$)
asetとaset2の[積集合|共通部分|[交わり|交差]|インターセクション][|を求める|を得る]
asetとaset2に共通する要素からなる集合[|を求める|を得る]
aset ∩ aset2
'''

alist = alist2 = []
list(set(alist) & set(alist2))
'''
alistとalist2の[積集合|共通りスト|インターセクション][|を求める|を得る]
'''

aset.difference(aset2)
'''
@test(aset=set([1,2]);aset2=set([1]);$$)
asetとaset2の[差集合|差][|を求める|を得る]
asetに含まれ、aset2に含まれない集合[|を求める|を得る]
asetからaset2を引いた[差集合|差][|を求める|を得る]
asetにおけるaset2の補集合[|を求める|を得る]
aset ＼ aset2
'''

aset.symmetric_difference(aset2)
'''
@test(aset=set([1,2]);aset2=set([1]);$$)
asetとaset2の[対称差集合|対称差][|を求める|を得る]
asetとaaset2のいずれか一方だけの集合[|を求める|を得る]
'''

element in aset
'''
@test(aset=set([1,2]);$$)
elementが_asetの[メンバー|要素][|に含まれる]かどうか
elementが_asetに含まれるかどうか
element ∈ aset
'''

element not in aset
'''
@test(aset=set([1,2]);$$)
elementが_asetの[メンバー|要素][でない|に含まれない]かどうか
elementが_asetに含まれないかどうか
element ∉ aset
'''

aset.issubset(aset2)
'''
@test(aset=set([1,2]);aset2=set([1]);$$)
asetが_aset2の[部分集合|下位集合|サブセット]かどうか
asetの全ての要素がaset2に含まれるかどうか
aset ⊆ aset2
'''

aset < aset2
'''
@test(aset=set([1,2]);aset2=set([1]);$$)
asetが_aset2の真[部分集合|下位集合|サブセット]かどうか
aset ⊂ aset2
'''

aset.issuperset(aset2)
'''
@test(aset=set([1,2]);aset2=set([1]);$$)
asetが_aset2の[上位集合|スーパーセット]かどうか
aset ⊇ aset2
'''

aset > aset2
'''
@test(aset=set([1,2]);aset2=set([1]);$$)
asetがaset2の真[上位集合|スーパーセット]かどうか
aset ⊃ aset2
'''

aset.isdisjoint(aset2)
'''
@test(aset=set([1,2]);aset2=set([1]);$$)
asetが_aset2と共通の要素を持たないかどうか
asetが_aset2と交わりを持たないかどうか
asetが_aset2と互いに素かどうか
asetとaset2が_互いに素かどうか
'''

len(aset)
'''
@test(aset=set([1,2]);$$)
asetの[濃度|要素数][|を求める]
'''

len(aset) == 0
'''
@test(aset=set([1,2]);$$)
asetが[空|空集合]かどうか
'''

len(aset) != 0
'''
@test(aset=set([1,2]);$$)
asetが[空|空集合]でないかどうか
'''

aset.copy()
'''
@test(aset=set([1,2]);$$)
asetの浅いコピー[|を作る]
'''


frozenset(iterable)
'''
iterableのイミュータブルな集合_[|を得る|を作る]
iterableを[イミュータブルな|変更不能な|更新不能な]集合_に変換する
'''

frozenset(aset)
'''
@test(aset=set([1,2]);$$)
asetの[イミュータブル|変更不能|更新不能]版
asetを[イミュータブルな|変更不能な|更新不能な][セット|集合]に変換する
asetを[イミュータブル|変更不能|更新不能]に変換する
'''

list(aset)
'''
@test(aset=set([1,2]);$$)
asetをリストに変換する
'''

tuple(aset)
'''
@test(aset=set([1,2]);$$)
asetを[タプル|組]に変換する
'''

alist = [1, 2]
sorted(set(alist), key=alist.index)
'''
alist[の|から]重複を取り除く
'''
