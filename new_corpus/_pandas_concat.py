import pandas as pd
'''
@alt(表データ=[データフレーム|データフレーム|表[データ|]])
@alt(カラム=[列|列|カラム])
@alt(インデックス|行)
@alt(欠損値|NaN|未入力値)
@alt(抽出する|取り出す|[選択する|選ぶ])

@prefix(df;[データフレーム|表データ])
@prefix(ds;[データ列|データフレームの[列|カラム]])
@prefix(column;[列|カラム];[列|カラム])
'''

columns = ['A', 'B', 'C']
column, column2, column3 = 'A', 'B', 'C'
df = pd.DataFrame(data=[[1, 2, 3], [4, 5, 6]], columns=['A', 'B', 'C'])
df2 = pd.DataFrame(data=[[1, 1, 1], [1, 1, 1]], columns=['A', 'B', 'C'])
df3 = pd.DataFrame(data=[[9, 9, 9], [9, 9, 9]], columns=['A', 'B', 'C'])
ds = df['A']

# concat
pd.concat([df, df2])
'''
@alt(連結する|[つなぐ|くっつける]|合体させる|[一つにする|一つにまとめる])

{２つのdfを|縦方向に}連結する
'''

pd.concat([df, df2], axis=0)
'''
@alt(縦方向に|縦[|向き]に)

{２つのdfを|縦方向に}連結する
'''

pd.concat([df, df2], axis=1)
'''
@alt(横方向に|横[向き|]に)

{２つのdfを|横方向に}連結する
'''

pd.concat([df, df2, df3], axis=0)
'''
{[３つ|複数]のdfを|縦方向に}連結する
'''

pd.concat([df, df2, df3], axis=1)
'''
{[３つ|複数]のdfを|横方向に}連結する
'''

pd.concat([df, ds], axis=1)
'''
dfとdsを[横方向に|]連結する
'''

pd.concat([df, ds], axis=1)
'''
dfとdsを[横方向に|]連結する
'''

df[df.columns[1:]]
'''
@alt(除く|消す)

{dfから|[最初の|一番左[側]の|先頭の]カラムを}除く
'''

df[df.columns[:-1]]
'''
{dfから|[最後の|一番右[側]の|末尾の]カラムを}除く
'''

n = 1

pd.concat([df[df.columns[:n]], df[df.columns[n+1:]]], axis=1)
'''
{dfから|[n番目の|1行だけ]カラムを}除く
'''

# マージ

pd.merge(df, df2)
'''
@alt(マージする|[一つにする|一つにまとめる]|合体させる)
@alt(結合する|ジョインする)

{２つのdfを|横方向に}マージする
２つのdfを結合する
'''

pd.merge(df, df2, on=column)
'''
{columnをキー[に|と]して|２つのdfを}結合する
'''

pd.merge(df, df2, left_on='A', right_on='B')
'''
{列'A'と列'B'をキー[と|に]して|２つのdfを}結合する
{異なるカラムをキー[と|に]して|２つのdfを}結合する
'''

__X__ = 'outer'

pd.merge(df, df2, on=column, how=__X__)
'''
@X('outer';'left';'right';'inner')
@Y([外部|全];左;右;内部)

{columnをキー[に|と]して|２つのdfを}__Y__結合する
'''

pd.merge(df, df2, left_on=column, right_on=column2, how=__X__)
'''
{列'A'と列'B'をキー[と|に]して|２つのdfを}__Y__結合する
{異なるカラムをキー[と|に]して|２つのdfを}__Y__結合する
'''


# ダミー処理

pd.get_dummies(df)
'''
@alt(ダミー変数|[ワンホット・ベクトル|ベクトル])

dfのカテゴリデータをダミー変数に変換する
'''

pd.get_dummies(df[column])
'''
dfのcolumnをダミー変数に変換する
'''

iterable = [1, 2, 1, 3]
pd.get_dummies(iterable)
'''
iterableをダミー変数に変換する
'''

pd.get_dummies(df[column], drop_first=True)
'''
@alt(除外する|除く|無視する)

{最初のカテゴリーを除外して|dfのcolumnを}ダミー変数に変換する
'''

pd.get_dummies(df[column], dummy_na=True)
'''
@alt(NaN|欠損値)

{NaNも加えて|dfのcolumnを}ダミー変数に変換する
'''
