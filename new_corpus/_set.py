# 集合

iterable = [0, 1, 2, 4]
st = {1, 2, 3}
st2 = {8, 9}
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

st.add(element)
'''
@prefix(st;セット)
@test(st=set([1,2]);$$;st)
{stに|elementを}追加する
'''

st.update(iterable)
'''
@test(st=set([1,2]);$$;st)
{stに|iterableの要素を[全て|]}追加する
{stに|iterableを}追加[更新|]する
'''

st.remove(element)
'''
@alt(取り除く|除く|除去する)
@test(st=set([1,2]);$$;st)
{stから|elementを}取り除く
'''

st.discard(element)
'''
@test(st=set([1,2]);$$;st)
{stから|エラーなく}elementを取り除く
'''

st.clear()
'''
@test(st=set([1,2]);$$;st)
stから[全[ての|]要素を|要素を全て][取り除く|消す]
stを[空|空集合]にする
'''

st.intersection_update(st2)
'''
@test(st=set([1,2]);st2=set([1,3]);$$;st)
stをst2との[共通要素|インターセクション][だけ|のみ]に[更新|]する
'''

st.difference_update(st2)
'''
@test(st=set([1,2]);st2=set([1,3]);$$;st)
stからst2[の要素|]を[全て|]取り除く
'''

st.symmetric_difference_update(st2)
'''
@test(st=set([1,2]);st2=set([1,3]);$$;st)
stからst2との共通要素を[全て|]取り除く
'''

st.pop()
'''
@test(st=set([1,2]);$$)
stから[任意の要素を|何でもいいから一つ][取り出す|取り除く]
'''

st.union(st2)
'''
@test(st=set([1,2]);st2=set([1,3]);$$)
stとst2の[和集合|ユニオン][|を求める|を得る]
st ∪ st2
'''

st.intersection(st2)
'''
@test(st=set([1,2]);st2=set([1,3]);$$)
stとst2の[積集合|共通部分|[交わり|交差]|インターセクション][|を求める|を得る]
stとst2に共通する要素からなる集合[|を求める|を得る]
st ∩ st2
'''

alist = alist2 = []
list(set(alist) & set(alist2))
'''
alistとalist2の[積集合|共通りスト|インターセクション][|を求める|を得る]
'''

st.difference(st2)
'''
@test(st=set([1,2]);st2=set([1]);$$)
stとst2の[差集合|差][|を求める|を得る]
stに含まれ、st2に含まれない集合[|を求める|を得る]
stからst2を引いた[差集合|差][|を求める|を得る]
stにおけるst2の補集合[|を求める|を得る]
st ＼ st2
'''

st.symmetric_difference(st2)
'''
@test(st=set([1,2]);st2=set([1]);$$)
stとst2の[対称差集合|対称差][|を求める|を得る]
stとast2のいずれか一方だけの集合[|を求める|を得る]
'''

element in st
'''
@test(st=set([1,2]);$$)
elementが_stの[メンバー|要素][|に含まれる]かどうか
elementが_stに含まれるかどうか
element ∈ st
'''

element not in st
'''
@test(st=set([1,2]);$$)
elementが_stの[メンバー|要素][でない|に含まれない]かどうか
elementが_stに含まれないかどうか
element ∉ st
'''

st.issubset(st2)
'''
@test(st=set([1,2]);st2=set([1]);$$)
stが_st2の[部分集合|下位集合|サブセット]かどうか
stの全ての要素がst2に含まれるかどうか
st ⊆ st2
'''

st < st2
'''
@test(st=set([1,2]);st2=set([1]);$$)
stが_st2の真[部分集合|下位集合|サブセット]かどうか
st ⊂ st2
'''

st.issuperset(st2)
'''
@test(st=set([1,2]);st2=set([1]);$$)
stが_st2の[上位集合|スーパーセット]かどうか
st ⊇ st2
'''

st > st2
'''
@test(st=set([1,2]);st2=set([1]);$$)
stがst2の真[上位集合|スーパーセット]かどうか
st ⊃ st2
'''

st.isdisjoint(st2)
'''
@test(st=set([1,2]);st2=set([1]);$$)
stが_st2と共通の要素を持たないかどうか
stが_st2と交わりを持たないかどうか
stが_st2と互いに素かどうか
stとst2が_互いに素かどうか
'''

len(st)
'''
@test(st=set([1,2]);$$)
stの[濃度|要素数][|を求める]
'''

len(st) == 0
'''
@test(st=set([1,2]);$$)
stが[空|空集合]かどうか
'''

len(st) != 0
'''
@test(st=set([1,2]);$$)
stが[空|空集合]でないかどうか
'''

st.copy()
'''
@test(st=set([1,2]);$$)
stの浅いコピー[|を作る]
'''


frozenset(iterable)
'''
iterableのイミュータブルな集合_[|を得る|を作る]
iterableを[イミュータブルな|変更不能な|更新不能な]集合_に変換する
'''

frozenset(st)
'''
@test(st=set([1,2]);$$)
stの[イミュータブル|変更不能|更新不能]版
stを[イミュータブルな|変更不能な|更新不能な][セット|集合]に変換する
stを[イミュータブル|変更不能|更新不能]に変換する
'''

list(st)
'''
@test(st=set([1,2]);$$)
stをリストに変換する
'''

tuple(st)
'''
@test(st=set([1,2]);$$)
stを[タプル|組]に変換する
'''

alist = [1, 2]
sorted(set(alist), key=alist.index)
'''
alist[の|から]重複を取り除く
'''
