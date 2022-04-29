
a.index = a / 1
'''
@test(a=missing;$$;a.index)
@prefix(a;とても)
aとa2[を|が]好き
aとa2
'''

df.index = pd.to_datetime(df)
'''
@test(pd=df=ds=missing;$$;df.index)
[Pandasで、|]__Y__を日付データに変換し、[dfの|]インデックスにする
'''


# ピボットテーブル

df.pivot_table(index='Pclass', columns='Sex')   @ @let


@type(df)の{@type('Pclass', カラム)をインデックス}、{@type('Sex', カラム)をカラム}としたピボットテーブルを作成する
df.pivot_table(index='Pclass', columns='Sex', values='Age')   @ @let


@type(df)の@type('Age', カラム)について、{@type('Pclass')をインデックス}、{@type('Sex')をカラム}としたピボットテーブルを作成する
# ピボット操作
df.stack()
ピボット操作で@type(df)の{列を行に}[入れ替える | 変更する]
ピボット操作で@type(df)の{列を行と}逆にする

df.unstack()
ピボット操作で@type(df)の{行を列に}入れ替える
ピボット操作で@type(df)の{行を列と}逆にする







# ソートする=





df[df[col] == x]
'''
@test(df=missing;$$)
@alt(を抽出する|[のみ|だけ]残す|を選択する)
@alt(フィルタする|消す|取り除く)
dfのcol[|の値]がx[の|である][行|データ]を抽出する
dfのcol[|の値]がxでない[行|データ]をフィルタする
'''
