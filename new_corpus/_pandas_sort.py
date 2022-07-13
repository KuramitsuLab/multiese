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
columns = ['列A', '列B', '列C']
column, column2, column3 = '列A', '列B', '列C'
df = pd.DataFrame(data=[[1, 2, 3], [4, 5, 6]], columns=['列A', '列B', '列C'])

# ソートする

__X__ = '列A'
'''
@X('列A';['列A', '列B'])
@Y([ある|指定した]カラム;[２つ|複数]のカラム)
'''

df.sort_values(by=__X__)
'''
@alt(ソートする|並べる|並べ直す|整列する)
@alt(によって|で|を用いて|をキーにして)

{dfを|__Y__によって}ソートする
'''

df.sort_values(by=__X__, ascending=True)
'''
@alt(昇順に|小さい順に)
{dfを|__Y__によって|昇順に}ソートする
'''

df.sort_values(by=__X__, ascending=False)
'''
@alt(降順に|大きい順に)
{dfを|__Y__によって|降順に}ソートする
'''

df.sort_values(by=__X__, ascending=True, inplace=True)
'''
{dfを|__Y__によって|昇順に}ソートして、更新する
{dfを|__Y__によって|昇順に|破壊的に}ソートする
'''

df.sort_values(by=__X__, ascending=False, inplace=True)
'''
{dfを|__Y__によって|降順に|破壊的に}ソートする
'''

df.sort_values(by=__X__, na_position='first')
'''
{dfを|__Y__によって}ソートして、NaNを先頭に[|来るように]する
'''

inplace = True
'''
option: [値を置き換える|更新する]
option: 破壊的に操作する
'''

na_position = 'first'
'''
option: 欠損値を先頭に[|来るように]する
'''

ascending = False
'''
option: 降順にする
'''

ascending = True
'''
option: 昇順にする
'''

# 連携
n = 10

df.sort_values('キーとなる列')
'''
dfをソートする
'''

df.sort_values('キーとなる列').head(n)
'''
@alt(上位|上の方)

dfをソートして、上位[n件|]を取り出す
'''

df.sort_values('キーとなる列').tail(n)
'''
@alt(下位|下の方)

dfをソートして、下位[n件|]を取り出す
'''

df.sort_values('キーとなる列').reset_index()
'''
dfをソートして、新しいインデックスを[加える|振り直す]
'''

df.sort_values('キーとなる列').reset_index(drop=True)
'''
dfをソートして、インデックスを振り直す
'''

# ソートインデックス

df.sort_index()
'''
{df[|全体]を|インデックスによって}ソートする
'''

df.sort_index(ascending=True)
'''
{df[|全体]を|インデックスによって|昇順に}ソートする
'''

df.sort_index(ascending=False)
'''
{df[|全体]を|インデックスによって|降順で}ソートする
'''

df['列A'].value_counts().sort_index().index
'''
FIXME: カテゴリーデータを出現頻度順にソートする
'''
