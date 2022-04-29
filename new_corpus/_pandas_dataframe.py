import numpy as np
import pandas as pd
'''
@test($$;type(pd))
@alt(表データ|データフレーム)
@alt(カラム|列)
@alt(インデックス|行)
@alt(欠損値|NaN|未入力値)
@prefix(df;データフレーム)
@prefix(ds;データ列)
@prefix(col;カラム;カラム)
@alt(変更する|増やす|減らす)
@alt(抽出する|取り出す|[選択する|選ぶ])
@alt(全ての|すべての|全)
@alt(の名前|名)
@alt(の一覧|一覧|[|の]リスト)
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

col, col2, col3 = 'A', 'B', 'C'
df = pd.DataFrame(data=[[1, 2, 3], [4, 5, 6]], columns=['A', 'B', 'C'])
df2 = df
ds, ds2 = df[col], df[col2]

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
dfからランダムに[|一行を]抽出する
dfをサンプリングする
'''

df.sample(n)
'''
dfから{ランダムに|n行を}抽出する
dfからn個、サンプリングする
'''

df.sample(n, replace=True)
'''
@alt(重複ありで|重複を認めて)
dfから{重複ありで|ランダムに|n行を}抽出する
'''

df[n:n2]
'''
dfのn行目からn2行目まで[を抽出する|]
'''

df[n:]
'''
dfのn行[|目][以降|より後ろ][を抽出する|]
'''

df[:n]
'''
dfのn行[|目][まで|より前][を抽出する|]
'''

df[col]
'''
dfのcol[を抽出する|]
'''

df[col].values
'''
{df[の|から]colを|配列として}抽出する
dfのcolを配列に変換する
'''

df[col].values.tolist()
'''
{df[の|から]colを|リストとして}抽出する
dfのcolをリストに変換する
'''

df[[col, col2]]
'''
df[の|から]colとcol2[を|のみ]だけ]抽出する
'''

df[[col, col2, col3]]
'''
df[の|から]col、col2、col3[を|のみ]だけ]抽出する
'''

alist = ['A', 'B']
df[alist]
'''
@test(alist=['A','B'];$$)
@alt(指定された|与えられた)
df[の|から]alistで指定されたカラム[を|のみ]だけ]抽出する
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
dfのカラム[一覧|概要][|を見る]
'''

df.columns
'''
dfのカラムの名前の一覧[を得る|]
'''

df.select_dtypes('object').columns
'''
@alt(カテゴリーデータ|[質的データ|数値データ以外])
dfからカテゴリデータのカラムの名前の一覧[を得る|]
'''

ty = int
df.select_dtypes(ty).columns
'''
@test(ty='object';$$)
dfからtyのカラムの名前の一覧[|を得る]
'''

df.index
'''
dfのインデックスの名前の一覧[|を得る]
'''

df.values
'''
dfを配列に変換する
'''

df.dtypes
'''
dfのデータ型の一覧[|を得る]
'''

df.select_dtypes(include=alist)
'''
@test(alist=['object'];$$)
dfからalist[で指定された|の]データ型のカラム[を|のみ|だけ]抽出する
'''

df.select_dtypes(exclude=alist)
'''
@test(alist=['object'];$$)
dfからalist[で指定された|の]データ型のカラム[を|のみ|だけ]除外する
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
@test(alist=['A', 'B'];$$)
@X(df;df[[col, col2]];df[alist])
@Y(df;dfのcolとcol2;dfのalist[|で指定された]カラム)
__Y__の[相関行列|各列間の相関係数][|を求める]
'''

__X__.corr(method='pearson')
'''
@test(alist=['A', 'B'];$$)
{ピアソン[[|積率]相関係数]で_|__Y__の相関行列}[|を求める]
'''

__X__.corr(method='kendall')
'''
@test(alist=['A', 'B'];$$)
{ケンドール[[|順位]相関係数|]で_|__Y__の相関行列}[|を求める]
'''

__X__.corr(method='spearman')
'''
@test(alist=['A', 'B'];$$)
{スピアマン[[|順位]相関係数|]で_|__Y__の相関行列}[|を求める]
'''

sns.heatmap(__X__.corr())
'''
@test(alist=['A', 'B'];$$)
@alt(描画する|グラフ化する)
{__Y__の相関行列を|ヒートマップで_}描画する
__Y__のヒートマップを描画する
'''


df.describe(include='O')
'''
@alt(求める|[計算する|算出する]|[見る|確認する])
@alt(要約統計量|[記述統計量|基本統計量|代表値])
dfのカテゴリデータの要約統計量[|を求める]
'''

df.round()
'''
@alt(丸める|四捨五入する)
@alt(丸めて|四捨五入して)
@alt[まとめて|全て|]
df[の数値|]をまとめて[|整数に]丸める
'''

df.round(n)
'''
df[の数値|]をまとめて小数点以下n桁で丸める
'''

df.round(inplace=True)
'''
@alt(インプレイスする|更新する|置き換える)
df[の数値|]をまとめて[|整数に]丸めて、インプレイスする
'''

df.round(n, inplace=True)
'''
df[の数値|]をまとめて小数点以下n桁で丸めて、インプレイスする
'''

# 変更する
s, s2 = 'A', 'a'

df.rename(columns={col: s})
'''
@alt(リネームする|名前[|を]変更する)
@alt(付け直す|変更する)
dfのカラムの名前を付け直す
dfのカラムの名前をcolからsに付け直す
dfのcolをsにリネームする
'''

df.columns = [str(x).replace(s, s2) for x in df.columns]
'''
@alt(まとめて|一度に|)
dfのカラムの名前をまとめて、sをs2に置換する
'''

df.rename(index={s: s2})
'''
dfのインデックスの名前をまとめて、sからs2に付け直す
'''

df.set_index(col)
'''
dfのcolをインデックスに設定する
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

df[df[col] == x]
'''
@test(df=missing;$$)
@alt(を抽出する|[のみ|だけ]残す|を選択する)
@alt(フィルタする|消す|取り除く)
dfのcol[|の値]がx[の|である][行|データ]を抽出する
dfのcol[|の値]がxでない[行|データ]をフィルタする
'''

df[(df[col] == x) & (df[col2] == x2)]
'''
@test(df=missing;$$)
dfの[行|データ]を条件でフィルタするには
dfのcol[|の値]がx、かつcol2がx2である[行|データ]を抽出する
'''

df[df[col] < x]
'''
@test(df=missing;$$)
dfのcol[|の値]がx[より[小さい|少ない]|未満の][行|データ]を抽出する
'''

df[df[col] <= x]
'''
@test(df=missing;$$)
dfのcol[|の値]がx以下の[行|データ]を抽出する
'''

df[df[col] > x]
'''
@test(df=missing;$$)
dfのcol[|の値]がxより[大きい|多い][行|データ]を抽出する
'''

df[df[col] >= x]
'''
@test(df=missing;$$)
dfのcol[|の値]がx以上の[行|データ]を抽出する
'''

df[(x < df[col]) & (df[col] < x2)]
'''
@test(df=missing;$$)
dfのcol[|の値]がxより[大きく|多く]x2より[小さい|少ない][行|データ]を抽出する
'''

df[(x <= df[col]) & (df[col] < x2)]
'''
@test(df=missing;$$)
dfのcol[|の値]がx以上かつx2未満の[行|データ]を抽出する
'''

df[df[col].isin(alist)]
'''
@test(df=missing;$$)
dfのcol[|の値]がalistに含まれる[行|データ]を抽出する
'''

s = 'A'

df[df[col].str.contains(s)]
'''
@test(df=missing;$$)
dfのcol[|の文字列][が|で]sが含まれる[行|データ]を抽出する
'''

df[not df[col].str.contains(s)]
'''
@test(df=missing;$$)
dfのcol[|の文字列][が|で]sが含まれない[行|データ]を抽出する
'''

df[df[col].str.match(s)]
'''
@test(df=missing;$$)
dfのcol[|の文字列]が正規表現sにマッチする[行|データ]を抽出する
'''

df[not df[col].str.match(s)]
'''
@test(df=missing;$$)
dfのcol[|の文字列]が正規表現sにマッチしない[行|データ]を抽出する
'''

df[df[col].str.startswith(s)]
'''
@test(df=missing;$$)
dfのcol[|の文字列]がsで始まる[行|データ]を抽出する
'''

df[not df[col].str.startswith(s)]
'''
@test(df=missing;$$)
dfのcol[|の文字列]がsで始まらない[行|データ]を抽出する
'''

df[df[col].str.endswith(s)]
'''
@test(df=missing;$$)
dfのcol[|の文字列]がsで終わる[行|データ]を抽出する
'''

df[not df[col].str.endswith(s)]
'''
@test(df=missing;$$)
dfのcol[|の文字列]がsで終わらない[行|データ]を抽出する
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

df.drop(col, axis=1)
'''
@test(df=missing;$$)
dfのcolをドロップする
'''

df.drop(col, axis=1, inplace=True)
'''
@test(df=missing;$$)
@alt(_変更を反映する|入れ替える|更新する)
{dfのcolを|破壊的に}ドロップする
dfのcolをドロップして、更新する
'''

df.drop([col, col2], axis=1)
'''
@test(df=missing;$$)
dfのcolとcol2をドロップする
'''

df.drop(alist, axis=1)
'''
@test(df=missing;$$)
dfのalistで指定されたカラムをドロップする
'''

df.dropna()
'''
@test(df=missing;$$)
@alt(の中||の内)
dfの中の欠損値をドロップする
dfの中の欠損値が[ある|存在する]行をドロップする
'''

# 重複

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

df.duplicated(subset=col)
'''
@test(pd=df=df2=missing;$$)
dfの中で、colの重複を見る
dfの中で、colに重複があるか見る
dfのcolに重複があれば、マスクする
'''

df.duplicated(subset=[col1, col2])
'''
@test(pd=df=df2=missing;$$)
dfの中で、colとcol2の重複を見る
dfの中で、colとcol2に重複があるか見る
dfの中のcolとcol2に重複があれば、マスクする
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

df.drop_duplicates(subset=col)
'''
@test(pd=df=df2=missing;$$)
[dfの中で、|]colとcol2の重複をドロップする
dfの中のcolとcol2に重複があれば、ドロップする
'''

df.drop_duplicates(subset=[col, col2])
'''
@test(pd=df=df2=missing;$$)
[dfの中で、|]colとcol2の重複をドロップする
dfの中のcolとcol2に重複があれば、ドロップする
'''

# マージ

pd.merge(df, df2)
'''
@test(pd=df=df2=missing;$$)
@alt(マージする|[一つにする|一つにまとめる]|合体させる)
@alt(結合する|ジョインする)
@alt(横方向に|横[向き|]に)
{dfとdf2を|横方向に}マージする
dfとdf2を結合する
'''

pd.merge(df, df2, on=col)
'''
@test(pd=df=df2=missing;$$)
dfとdf2をcolをキー[に|と]して結合する
'''

pd.merge(df, df2, left_on=col, right_on=col2)
'''
@test(pd=df=df2=missing;$$)
dfのcolとdf2のcol2をキー[に|と]して結合する
'''

pd.merge(df, df2, on=col, how=__X__)
'''
@test(pd=df=df2=missing;$$)
@X('outer';'left';'right';'inner')
@Y([外部|全];左;右;内部)
dfとdf2をcolをキー[に|と]して__Y__結合する
'''

pd.merge(df, df2, left_on=col, right_on=col2, how=__X__)
'''
@test(pd=df=df2=missing;$$)
dfのcolとdf2のcol2をキー[に|と]して__Y__結合する
'''

pd.concat([df, df2])
'''
@test(pd=df=df2=missing;$$)
@alt(縦方向に|縦[|向き]に|)
{dfとdf2を|縦方向に}連結する
{dfとdf2を|縦方向に}繋ぐ
'''


# ダミー処理

pd.get_dummies(df)
'''
dfのカテゴリデータをダミー変数に変換する
'''

pd.get_dummies(df[col])
'''
dfのcolをダミー変数に変換する
'''

iterable = [1, 2, 1, 3]
pd.get_dummies(iterable)
'''
iterableをダミー変数に変換する
'''

pd.get_dummies(x, drop_first=True)
'''
{最初のカテゴリーを除外し[て、]|xを}ダミー変数に変換する
'''

pd.get_dummies(x, dummy_na=True)
'''
{NaNも加えて|xを}ダミー変数に変換する
'''

# ソートする

__X__ = col
df.sort_values(by=col)
'''
@test(df=missing;alist=['A'];$$)
@alt(ソートする|並べる|並べ直す|整列する)
@alt(ソートして|並べて|並べ直して|整列して)
@X(col;[col,col2];alist)
@Y(col;colとcol2;alist[で指定された|の]カラム)
@alt(によって|で|を用いて)
{df[|全体]を|__Y__によって}ソートする
'''

df.sort_values(by=__X__, inplace=True)
'''
@test(df=missing;alist=['A'];$$)
{df[|全体]を|__Y__によって}ソートして、更新する
{df[|全体]を|__Y__によって|破壊的に}ソートする
'''

df.sort_values(by=__X__, ascending=True)
'''
@test(df=missing;alist=['A'];$$)
@alt(昇順に|小さい順に)
{df[|全体]を|__Y__によって|昇順に}ソートする
'''

df.sort_values(by=__X__, ascending=False)
'''
@test(df=missing;alist=['A'];$$)
@alt(降順に|大きい順に)
{df[|全体]を|__Y__によって|降順に}ソートする
'''

df.sort_values(by=__X__, ascending=True, inplace=True)
'''
@test(df=missing;alist=['A'];$$)
{df[|全体]を|__Y__によって|昇順に}ソートして、更新する
{df[|全体]を|__Y__によって|昇順に|破壊的に}ソートする
'''

df.sort_values(by=__X__, ascending=False, inplace=True)
'''
@test(df=missing;alist=['A'];$$)
{df[|全体]を|__Y__によって|降順に|破壊的に}ソートする
'''

df.sort_values(by=__X__, na_position='first')
'''
@test(df=missing;alist=['A'];$$)
{df[|全体]を|__Y__によって}ソートして、NaNを先頭に[|来るように]する
'''

inplace = True
'''
@test($$;inplace)
オプションで、データ操作の結果を反映させる
オプションで、破壊的に操作する
'''

na_position = 'first'
'''
@test($$;na_position)
オプションで、欠損値を先頭に[|来るように]する
'''

ascending = False
'''
@test($$;ascending)
オプションで、降順にする
'''

ascending = True
'''
@test($$;ascending)
オプションで、昇順にする
'''

# ソート

df.sort_index()
'''
@test(df=missing;alist=['A'];$$)
{df[|全体]を|インデックスによって}ソートする
'''

df.sort_index(ascending=False)
'''
@test(df=missing;alist=['A'];$$)
{df[|全体]を|インデックスによって|降順で}ソートする
'''

# グループ化

df.groupby(col)
'''
@test(df=missing;$$)
@alt(グループ化する|集[約|計]する|まとめる)
@alt(グループ化した|集[約|計]した|まとめた)
@alt(グループ化して|集[約|計]して|まとめて)
@alt(毎に|ごとに|毎で|で)
@alt(各||各)
{dfを|各col毎に}グループ化する
'''

df.groupby(col, dropna=False)
'''
@test(df=missing;$$)
{dfを|欠損値を含めて|各col毎に}グループ化する
'''


def func(x): return 'A'


df.groupby(func)
'''
@test(df=missing;func=lamda x: 'A';$$)
dfをfuncで_グループ化する
'''

[(name, group) for name, group in df.groupby(col)]
'''
@test(df=missing;$$)
dfを各col毎にグループ化して、列挙する
'''

[(name, group) for name, group in df.groupby([col, col2])]
'''
@test(df=missing;$$)
dfをcolとcol2の組み合わせ毎にグループ化して、列挙する
'''

df.groupby(col).get_group(s)
'''
@test(df=missing;$$)
dfを各col毎にグループ化して、sという[|名前の]グループを得る
'''

df.groupby(col).size()
'''
@test(df=missing;$$)
dfを各col毎にグループ化して、各グループの[個数|大きさ]を求める
'''

df.groupby(col).size()[s]
'''
@test(df=missing;$$)
dfを各col毎にグループ化して、sというグループの[個数|大きさ]を求める
'''


df.groupby(col).__X__
'''
@test(df=missing;$$)
@X(sum()|mean()|count()|max()|min()|var()|std()|agg(func))
@Y(合計|平均値|個数|最大値|最小値|分散|標準偏差|関数適用した値)
dfの各col毎の__Y__[|を求める]
dfを各col毎に[グループ化して、|グループ化した]__Y__を求める
'''

df.groupby([col, col2], as_index=False).__X__
'''
@test(df=missing;$$)
dfの各colとcol2毎の__Y__[|を求める]
dfを各colとcol2の組み合わせ毎にグループ化して、__Y__[|を求める]
'''


df.groupby(col)[col2].__X__
'''
@test(df=missing;$$)
{dfを|各col毎に}グループ化して、col2の__Y__を求める
'''

df.groupby(col).describe()[col2]
'''
@test(df=missing;$$)
{dfを|各col毎に}グループ化して、col2の要約統計量を求める
'''
