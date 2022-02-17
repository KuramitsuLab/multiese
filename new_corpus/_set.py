# 集合

iterable=[0,1,2,4]
st={1,2,3}
st2={8,9}
element=1

set()
'''
空の[セット|集合]
空集合
'''

set(iterable)
'''
iterableの[セット|集合]
iterableを[セット|集合]に変換する
'''

st.add(element)
'''
stにelementを追加する
'''

st.remove(element)
'''
stからelementを[取り除く|除去する]
'''

st.union(st2)
'''
stとst2の和集合
'''

st.intersection(st2)
'''
stとst2の[積集合|共通部分]
'''

st.intersection(st2)
'''
stとst2の[積集合|共通部分]
'''

st.difference(st2)
'''
stとst2の[差集合|差]
'''

st.symmetric_difference(st2)
'''
stとst2の[対称差集合|対称差]
'''

element in st
'''
element[が|は]stの要素かどうか
'''

st.issubset(st2)
'''
st[が|は]st2の部分集合かどうか
'''

st.issuperset(st2)
'''
st[が|は]st2の上位集合かどうか
'''

st.isdisjoint(st2)
'''
st[が|は]st2と互いに素かどうか
stとst2[が|は]互いに素かどうか
'''

frozenset(iterable)
'''
iterableのイミュータブルな[セット|集合]
iterableを[イミュータブルな|変更不能な|更新不能な][セット|集合]に変換する
'''

frozenset(st)
'''
stの[イミュータブル|変更不能|更新不能]版
stを[イミュータブルな|変更不能な|更新不能な][セット|集合]に変換する
stを[イミュータブル|変更不能|更新不能]に変換する
'''
