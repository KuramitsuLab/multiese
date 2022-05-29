import numpy as np
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
@prefix(value;[文字列|日付|])

表データを使う
表データをインポートする
'''

import seaborn as sns

n = 1
n2 = 3

excelfile = 'test.csv'
csvfile = 'file.csv'
tsvfile = 'file.tsv'
jsonfile = 'file.json'
jsonlfile = 'file.json'

column, column2, column3 = 'A', 'B', 'C'
df = pd.DataFrame(data=[[1, 2, 3], [4, 5, 6]], columns=['A', 'B', 'C'])
df2 = pd.DataFrame(data={'A': [1, 2], 'B': [2, 1]})
ds, ds2 = df[column], df[column2]

# 確認系

df.head()
'''
df[|の内容]を見る
dfの[先頭|最初][|を見る]
'''

df.head(n)
'''
dfの[先頭|最初|上]n行[|を抽出する]
dfの[先頭|最初|上]n行[|を見る]
'''

df.tail()
'''
dfの[末尾|最後][|を見る]
'''

df.tail(n)
'''
dfの[末尾|最後|下]n行を抽出する
'''

df.sample()
'''
{dfから|ランダムに|[|一行[を|、]]}抽出する
dfを[|ランダム]サンプリングする
'''

df.sample(n)
'''
{dfから|ランダムに|n行を}抽出する
dfからn行、[|ランダム]サンプリングする
'''

df.sample(n, replace=True)
'''
@alt(重複ありで|重複を認めて)

{dfから|重複ありで|ランダムに|n行を}サンプリングする
'''

start = 0
end = 2

df[start:end]
'''
{dfの行を|[範囲指定して|]}抽出する
dfのstart行目からend行目まで[|を]抽出する
'''

df[n:]
'''
dfのn行[|目][以降|より後ろ][|を]抽出する
'''

df[:n]
'''
dfのn行[|目][まで|より前][|を]抽出する
'''

df[column]
'''
@alt(指定された|与えられた|)

dfの指定されたcolumn[を抽出する|]
'''

df[column].values
'''
[dfの指定された|]columnを配列に変換する
{[dfの指定された|]columnを|配列として}抽出する
'''

df[column].values.tolist()
'''
[dfの指定された|]columnをリストに変換する
{[dfの指定された|]columnを|リストとして}抽出する
'''

df[[column]]
'''
dfからカラムを１つ[|のみ|だけ]選択する
df[から|の]指定された列[を|のみ|だけ]抽出する
'''

df[[column, column2]]
'''
dfからカラムを２つ[|のみ|だけ]選択する
df[から|の]指定された２[つの|]列[を|のみ|だけ]抽出する
'''

df[[column, column2, column3]]
'''
dfからカラムを３つ[|のみ|だけ]選択する
df[から|の]指定された３[つの|]列[を|のみ|だけ]抽出する
'''

column4 = 'A'

df[[column, column2, column3, column4]]
'''
dfからカラムを４つ[|のみ|だけ]選択する
df[から|の]指定された４[つの|]列[を|のみ|だけ]抽出する
'''

columns = ['A', 'B']
df[columns]
'''
@prefix(columns;[[カラムの名前|列名]一覧|[名前|列名]リスト])

dfから列名を複数指定して選択する
df[の|から]指定されたcolumnsの列[を|のみ|だけ][抽出する|選択する]
'''

df.loc[n]
'''
dfのn[行目|番目の行]を抽出する
dfのインデックスがnの行を抽出する
'''

# df.iloc[[1,2,4],[0,2]]   @@get @@it
# @type(df)内の1,2,4行目の0,2列目

df.info()
'''
[dfの|]カラム[の一覧|概要][|を見る]
[dfの|]カラムの種類[|を見る]
'''

df.columns
'''
[dfの|]カラムの名前の一覧[を得る|]
[dfの|]カラムの名前を列挙する
'''

df.columns = columns
'''
[dfの|]カラム名を指定されたcolumnsに置き換える
'''

df.select_dtypes('object').columns
'''
@alt(カテゴリーデータ|[質的データ|数値データ以外])

dfからカテゴリデータのカラム名の一覧[を得る|]
dfからカテゴリデータのカラム名を列挙する
'''

型 = int
df.select_dtypes(型).columns
'''
dfから指定されたデータ型のカラム名の一覧[|を得る]
dfの指定されたデータ型のカラム名を列挙する
カラム名の一覧をデータ型でフィルタする
'''

df.index
'''
dfのインデックス[|の名前]の一覧[|を得る]
'''

df.values
'''
dfを配列に変換する
'''

df.dtypes
'''
dfのデータ型の一覧[|を得る]
'''

typeList = [int]

df.select_dtypes(include=typeList)
'''
@prefix(typeList;型リスト)

dfからtypeList[で指定された]データ型のカラム[を|のみ|だけ]抽出する
'''

df.select_dtypes(exclude=typeList)
'''
dfからtypeList[で指定された|の]データ型のカラム[を|のみ|だけ]除外する
'''

__X__ = 'object'

df.select_dtypes(__X__)
'''
@X('object';'number';ty)
@Y(カテゴリデータ;数値データ;ty[|型])
dfから__Y__[のカラム][を|のみ|だけ]抽出する
'''

df.shape
'''
dfの[各次元の[大きさ|サイズ]|シェイプ][を見る]
'''

df.T
'''
dfを転置する
dfの[行と列|行列]を[入れ替える|ひっくり返す]
'''

__X__ = df

__X__.corr()
'''
@test(aList=['A', 'B'];$$)
@X(df;df[[column, column2]];df[aList])
@Y(df;dfのcolumnとcolumn2;dfのaList[|で指定された]カラム)

__Y__の[相関行列|各列間の相関係数][|を求める]
'''

__X__.corr(method='pearson')
'''
@test(aList=['A', 'B'];$$)
{ピアソン[[|積率]相関係数]で_|__Y__の相関行列}[|を求める]
'''

__X__.corr(method='kendall')
'''
@test(aList=['A', 'B'];$$)
{ケンドール[[|順位]相関係数|]で_|__Y__の相関行列}[|を求める]
'''

__X__.corr(method='spearman')
'''
@test(aList=['A', 'B'];$$)
{スピアマン[[|順位]相関係数|]で_|__Y__の相関行列}[|を求める]
'''

sns.heatmap(__X__.corr())
'''
@test(aList=['A', 'B'];$$)
@alt(描画する|グラフ化する)
{__Y__の相関行列を|ヒートマップで_}描画する
__Y__のヒートマップを描画する
'''

df.round()
'''
@alt(丸める|四捨五入する)
@alt(丸めて|四捨五入して)
@alt[まとめて|全て|]
@alt(インプレイスする|更新する|置き換える)
df[の数値|]をまとめて[|整数に]丸める
'''

df.round(n)
'''
df[の数値|]をまとめて小数点以下n桁で丸める
'''

# 変更する
name = 'A'
name2 = 'B'
s = 'A'
s2 = 'a'

df.rename(columns={column: name})
'''
@alt(リネームする|名前[|を]変更する)
@alt(付け直す|変更する)
dfのカラムの名前を付け直す
dfのカラムの名前をcolumnからsに付け直す
dfのcolumnをsにリネームする
'''

df.columns = [str(x).replace(s, s2) for x in df.columns]
'''
@alt(まとめて|一度に|)
{dfのカラムの名前を|まとめて}sをs2に置換する
'''

df.rename(index={name: name2})
'''
dfのインデックスの名前をまとめて、nameからname2に付け直す
'''

df.set_index(column)
'''
dfのcolumnをインデックスに設定する
'''

df.reset_index()
'''
dfのインデックスを[リセットする|振り直す]
'''

# df.reset_index(drop=True)
# @type(df)の[元の|もともとの|元々あった|もともとあった]インデックスをリセットする
# {@type(df)のインデックスを[リセットして|振り直して]、}元のインデックスを削除する
# {元のインデックスを[削除し、|削除してから、]}@type(df)のインデックスをリセットする


# datetime


# 演算処理系

# df['temperature'].diff(periods=1)   @ @let @ @calc

# @type(df)の@type('temperature', カラム)内の前後の行の差分


# 行列操作


# フィルター
x = 1.0
x2 = 2.0

df[df[column] == x]
'''
@test(df=missing;$$)
@alt(を抽出する|[のみ|だけ]残す|を選択する)
@alt(フィルタする|消す|取り除く)
dfのcolumn[|の値]がx[の|である][行|データ]を抽出する
dfのcolumn[|の値]がxでない[行|データ]をフィルタする
'''

df[(df[column] == x) & (df[column2] == x2)]
'''
@test(df=missing;$$)
dfの[行|データ]を条件でフィルタするには
dfのcolumn[|の値]がx、かつcolumn2がx2である[行|データ]を抽出する
'''

df[df[column] < x]
'''
@test(df=missing;$$)
dfのcolumn[|の値]がx[より[小さい|少ない]|未満の][行|データ]を抽出する
'''

df[df[column] <= x]
'''
@test(df=missing;$$)
dfのcolumn[|の値]がx以下の[行|データ]を抽出する
'''

df[df[column] > x]
'''
@test(df=missing;$$)
dfのcolumn[|の値]がxより[大きい|多い][行|データ]を抽出する
'''

df[df[column] >= x]
'''
@test(df=missing;$$)
dfのcolumn[|の値]がx以上の[行|データ]を抽出する
'''

df[(x < df[column]) & (df[column] < x2)]
'''
@test(df=missing;$$)
dfのcolumn[|の値]がxより[大きく|多く]x2より[小さい|少ない][行|データ]を抽出する
'''

df[(x <= df[column]) & (df[column] < x2)]
'''
@test(df=missing;$$)
dfのcolumn[|の値]がx以上かつx2未満の[行|データ]を抽出する
'''

df[df[column].isin(aList)]
'''
@test(df=missing;$$)
dfのcolumn[|の値]がaListに含まれる[行|データ]を抽出する
'''

df = pd.DataFrame(data={'A': ['A', 'B'], 'B': ['B', 'A']})
column = 'A'
column2 = 'B'

df[df[column].str.contains(s)]
'''
@test(df=missing;$$)
dfのcolumn[|の文字列][が|で]sが含まれる[行|データ]を抽出する
'''

df[not df[column].str.contains(s)]
'''
@test(df=missing;$$)
dfのcolumn[|の文字列][が|で]sが含まれない[行|データ]を抽出する
'''

df[df[column].str.match(s)]
'''
@test(df=missing;$$)
dfのcolumn[|の文字列]が正規表現sにマッチする[行|データ]を抽出する
'''

df[not df[column].str.match(s)]
'''
@test(df=missing;$$)
dfのcolumn[|の文字列]が正規表現sにマッチしない[行|データ]を抽出する
'''

df[df[column].str.startswith(s)]
'''
@test(df=missing;$$)
dfのcolumn[|の文字列]がsで始まる[行|データ]を抽出する
'''

df[not df[column].str.startswith(s)]
'''
@test(df=missing;$$)
dfのcolumn[|の文字列]がsで始まらない[行|データ]を抽出する
'''

df[df[column].str.endswith(s)]
'''
@test(df=missing;$$)
dfのcolumn[|の文字列]がsで終わる[行|データ]を抽出する
'''

df[not df[column].str.endswith(s)]
'''
@test(df=missing;$$)
dfのcolumn[|の文字列]がsで終わらない[行|データ]を抽出する
'''

# ドロップ・欠損値処理

df.style.highlight_null()
'''
@test(df=missing;$$)
@alt(付け|つけ)
dfの欠損値が[含まれる|ある][箇所|部分][に[色を付ける]|を[色付けする]]
'''

df.drop(n, axis=0)
'''
@test(df=missing;$$)
@alt(ドロップする|削除する|消す|[落とす|取り除く]|ドロップする)
@alt(ドロップして|[削除し|消し|取り除い][て|、])
dfのn行目をドロップする
'''

df.drop(n, axis=0, inplace=True)
'''
@test(df=missing;$$)
@alt(更新する|入れ替える|インプレイスする)
@alt(破壊的に|インプレイスで)
{dfのn行目を|破壊的に}ドロップする
dfのn行目をドロップして、更新する
'''

df.drop(column, axis=1)
'''
@test(df=missing;$$)
dfのcolumnをドロップする
'''

df.drop(column, axis=1, inplace=True)
'''
@test(df=missing;$$)
@alt(_変更を反映する|入れ替える|更新する)
{dfのcolumnを|破壊的に}ドロップする
dfのcolumnをドロップして、更新する
'''

df = pd.DataFrame(data={'A': ['A', 'B'], 'B': ['B', 'A']})
column = 'A'
column2 = 'B'

df.drop([column, column2], axis=1)
'''
@test(df=missing;$$)
dfのcolumnとcolumn2をドロップする
'''

df = pd.DataFrame(data={'A': ['A', 'B'], 'B': ['B', 'A']})
column = 'A'
column2 = 'B'
columns = ['A', 'B']

df.drop(columns, axis=1)
'''
dfのcolumnsで指定されたカラムをドロップする
'''

df.dropna()
'''
@alt(の中||の内)
dfの中の欠損値をドロップする
dfの中の欠損値が[ある|存在する]行をドロップする
'''

# 重複

df = pd.DataFrame(data={'A': [1, 1], 'B': [1, 1]})
column = 'A'
column2 = 'B'
columns = ['A', 'B']


df.duplicated()
'''
@test(pd=df=df2=missing;$$)
@alt(重複した|重複する)
dfの重複を見る
dfに重複があるか見る
dfが重複しているかどうか
dfの重複した行をマスクする
dfの重複した行数のマスク[|を得る]
'''

df.duplicated().sum()
'''
@test(pd=df=df2=missing;$$)
dfの重複した行[|数]を数える
dfの中で何行、重複するか見る
'''

df[df.duplicated(keep=False)]
'''
@test(pd=df=df2=missing;$$)
[dfの|]重複した行[のみ|だけ|][を抽出する|]
'''

df[not df.duplicated(keep=False)]
'''
@test(pd=df=df2=missing;$$)
[dfの|]重複していない行[のみ|だけ|][を抽出する|]
'''

df.duplicated(subset=column)
'''
@test(pd=df=df2=missing;$$)
dfの中で、columnの重複を見る
dfの中で、columnに重複があるか見る
dfのcolumnに重複があれば、マスクする
'''

df.duplicated(subset=[column, column2])
'''
@test(pd=df=df2=missing;$$)
dfの中で、columnとcolumn2の重複を見る
dfの中で、columnとcolumn2に重複があるか見る
dfの中のcolumnとcolumn2に重複があれば、マスクする
'''

df.drop_duplicates()
'''
@test(pd=df=df2=missing;$$)
dfから重複をドロップする
dfから重複した[行|データ]をドロップする
'''

df.drop_duplicates(inplace=True)
'''
@test(pd=df=df2=missing;$$)
{dfから|破壊的に|重複を}ドロップする
dfから重複した[行|データ]をドロップして、更新する
{dfから|破壊的に|重複した[行|データ]を}ドロップする
'''

df.drop_duplicates(keep=False)
'''
@test(pd=df=df2=missing;$$)
dfから重複を残さず、ドロップする
dfから重複した[行|データ]を残さず、ドロップする
'''

df.drop_duplicates(subset=column)
'''
@test(pd=df=df2=missing;$$)
[dfの中で、|]columnとcolumn2の重複をドロップする
dfの中のcolumnとcolumn2に重複があれば、ドロップする
'''

df.drop_duplicates(subset=[column, column2])
'''
[dfの中で、|]columnとcolumn2の重複をドロップする
dfの中のcolumnとcolumn2に重複があれば、ドロップする
'''

