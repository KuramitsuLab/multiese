import pandas as pd
'''
@alt(表データ=[データフレーム|データフレーム|表[データ|]])
@alt(カラム=[列|列|カラム])
@alt(インデックス|行)
@alt(欠損値|NaN|未入力値)
@alt(抽出する|取り出す|[選択する|選ぶ])

@prefix(df;[データフレーム|表データ])
@prefix(ds;[データシリーズ|データフレームの[列|カラム]])
@prefix(column;[列|カラム];[列|カラム])
'''

columns = ['列A', '列B', '列C']
column, column2, column3 = '列A', '列B', '列C'
df = pd.DataFrame(data=[[1, 2, 3], [4, 5, 6]], columns=['列A', '列B', '列C'])
df2 = pd.DataFrame(data=[[1, 1, 1], [1, 1, 1]], columns=['列A', '列B', '列C'])
df3 = pd.DataFrame(data=[[9, 9, 9], [9, 9, 9]], columns=['列A', '列B', '列C'])
ds = df['列A']

# concat
pd.concat([df, df2])
'''
@alt(連結する|合体[させる|する]|[つなぐ|くっつける])
@alt(結合する|一つに[する|まとめる])

[２つの|]dfを連結する
'''

pd.concat([df, df2], axis=0)
'''
@alt(縦方向に|縦[|向き]に)

{[２つの|]dfを|縦方向に}連結する
{[２つの|]dfを|縦方向に}結合する
'''

pd.concat([df, df2], axis=1)
'''
@alt(横方向に|横[向き|]に)

{[２つの|]dfを|横方向に}連結する
{[２つの|]dfを|横方向に}結合する
'''

pd.concat([df, df2, df3], axis=0)
'''
{[３つ|複数]のdfを|縦方向に}連結する
{[３つ|複数]のdfを|縦方向に}結合する
'''

pd.concat([df, df2, df3], axis=1)
'''
{[３つ|複数]のdfを|横方向に}連結する
{[３つ|複数]のdfを|縦方向に}結合する
'''

pd.concat([df, ds], axis=1)
'''
dfとdsを[横方向に|]連結する
'''

df[df.columns[1:]]
'''
@alt(除く|消す)

[最初の|一番左[側]の|先頭の]を[除いた|外した]df[|を得る]
'''

df[df.columns[:-1]]
'''
[最後の|一番右[側]の|末尾の]カラムを[除いた|外した]df[|を得る]
'''

n = 1

pd.concat([df[df.columns[:n]], df[df.columns[n+1:]]], axis=1)
'''
[n番目の|1行だけ]カラムを[除いた|外した]df[|を得る]
'''

# マージ

pd.merge(df, df2)
'''
@alt(マージする|[一つにする|一つにまとめる]|合体させる)
@alt(ジョインする|結合する)

{２つのdfを|横方向に}マージする
２つのdfをジョインする
'''
'
pd.merge(df, df2, on='列A')
'''
{カラム名を指定して|[２つの|]dfを}ジョインする
'''

pd.merge(df, df2, left_on='列A', right_on='列B')
'''
{異なるカラムをキー[と|に]して|[|２つの]dfを}ジョインする
'''

__X__ = 'outer'
'''
@X('outer';'left';'right';'inner')
@Y([外部|全];左;右;内部)
'''

pd.merge(df, df2, on='列A', how=__X__)
'''
{カラム名を指定して|[２つの|]dfを}__Y__ジョインする
'''

pd.merge(df, df2, left_on='列A', right_on='列B', how=__X__)
'''
{異なるカラムをキー[と|に]して|[２つの|]dfを}__Y__ジョインする
'''


# ダミー処理

pd.get_dummies(df)
'''
@alt(ダミー変数|[ワンホット・ベクトル|ベクトル])

df[のカテゴリデータ|]をダミー変数に変換する
'''

pd.get_dummies(df['列A'])
'''
@alt(あるカラム|[指定した|指定された|]カラム)

dfのあるカラムをダミー変数にする
'''

pd.get_dummies(df['列A'], drop_first=True)
'''
@alt(除外する|除く|無視する)

{最初のカテゴリーを除外して|dfのあるカラムを}ダミー変数に変換する
'''

pd.get_dummies(df['列A'], dummy_na=True)
'''
@alt(NaN|欠損値)

{NaNも加えて|dfのあるカラムを}ダミー変数に変換する
'''
