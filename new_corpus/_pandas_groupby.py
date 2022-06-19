import pandas as pd
'''
@alt(表データ=[データフレーム|データフレーム|表[データ|]])
@alt(カラム=[列|列|カラム])
@alt(インデックス|行)
@alt(欠損値|NaN|未入力値)
@alt(変更する|増やす|減らす)
@alt(抽出する|取り出す|[選択する|選ぶ])
@alt(全ての|すべての|全)
@alt(の名前|名)
@alt(の一覧|一覧|[|の]リスト)

@prefix(df;[データフレーム|表データ])
@prefix(ds;[データ列|データフレームの[列|カラム]])
@prefix(column;[列|カラム];[列|カラム])
@prefix(value;[文字列|日付])
'''
columns = ['A', 'B', 'C']
column, column2, column3 = 'A', 'B', 'C'
df = pd.DataFrame(data=[[1, 2, 3], [4, 5, 6]], columns=['A', 'B', 'C'])
#df2 = pd.DataFrame(data={'A': [1, 2], 'B': [2, 1]})
#ds, ds2 = df[column], df[column2]


def func(x): return 'A'


関数 = func

# グループ化

__X__ = 'A'

df.groupby(__X__)
'''
@X(column;'A';['A', 'B'];columns;関数)
@Y(列;'A'列;[２つの[列|列|カラム]|'A'列と'B'列];[複数の列|列名リスト];関数)

@alt(グループ化する=[グループ化する|集[約|計]する|[グループ分け|分類]する])
@alt(グループ化した|集[約|計]した|まとめた)
@alt(表グループ=[グループ|表])

@alt(ごと|毎|)
@alt(それぞれの|各|)

{dfを|__Y__[の値|][によって|で]}グループ化する
{dfを|__Y__[|の値][によって|で]}まとめた表グループ[|を得る]
'''

df.groupby(__X__).describe()
'''
{dfを|__Y__[の値|][によって|で]}グループ化し、[要約|記述|基本]統計量を求める
'''


df.groupby(column, dropna=False)
'''
{dfを|欠損値を含めて|column[の値|]で}グループ化する
'''

dropna = True
'''
option: 欠損値[は無視する|を含めない]
'''

dropna = True
'''
option: 欠損値[も無視しない|[も|を]含める]
'''

[(name, group) for name, group in df.groupby(__X__)]
'''
{dfを|__Y__[の値|][によって|ごとに|で]}グループ化して、列挙する
'''

df.groupby(column).get_group(s)
'''
dfを各column毎にグループ化して、sという[|名前の]グループを得る
'''

df.groupby(column).size()
'''
{dfを|column[|の値]で_}グループ化して、それぞれのグループごとの件数を知る
'''

df.groupby(column).size()[s]
'''
dfを各column毎にグループ化して、sというグループの[個数|大きさ]を求める
'''

df.groupby(column).__X__
'''
@X(sum()|mean()|count()|max()|min()|var()|std())
@Y(合計|平均値|個数|最大値|最小値|分散|標準偏差)

dfのそれぞれのグループごとの__Y__[|を求める]
{dfを|column[|の値][によって|ごとに|で]}グループ化して、[それぞれのグループごとの|]__Y__を求める
'''

df.groupby([column, column2], as_index=False).__X__
'''
@test(df=missing;$$)
dfを各columnとcolumn2の組み合わせ毎にグループ化して、__Y__を求める
'''

df.groupby(column)[column2].__X__
'''
dfをグループ化し、それぞれの列に対し__Y__を求める

{dfを|各column毎に}グループ化して、column2の__Y__を求める
'''

df.groupby(column).describe()[column2]
'''
{dfを|columnで}グループ化して、column2の要約統計量を求める
'''
