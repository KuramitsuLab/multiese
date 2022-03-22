
# read

# 読み込む = [読み込む|読む]

pd.read_excel(filepath)
'''
@test(pd=missing;_)
@alt(読み込む|読む)
@alt(読み込んで|読んで)
{エクセルファイルfilepathを|[Pandasで|データフレームとして]}読み込む
文字列filepathからエクセル[データ]を読み込む
'''

pd.read_excel(filepath, sheet_name=n)
'''
@test(pd=missing;_)
エクセルファイルfilepathを[Pandasで|データフレームとして|]読み込む
{エクセルファイルfilepathから|n番目のシートを}[Pandasで|データフレームとして|]読み込む
{エクセルファイルfilepathから|nという[名前の|]シートを}[Pandasで|データフレームとして|]読み込む
{エクセルファイルfilepathから|nとシートを指定し}[Pandasで|データフレームとして|]読み込む
'''

pd.read_csv(filepath, sep=',')
'''
@test(pd=missing;_)
{テキストファイルfilepathを|カンマ区切りで|[Pandasで|データフレームとして|]}読み込む
{CSVファイルfilepathを|[Pandasで|データフレームとして|]}読み込む
文字列filepathから{CSVファイルを|[Pandasで|カンマ区切りで|データフレームとして|]}読み込む
'''

pd.read_csv(filepath, sep='\t')
'''
@test(pd=missing;_)
{テキストファイルfilepathを|タブ区切りで|[Pandasで|データフレームとして|]}読み込む
{TSVファイルfilepathを|[Pandasで|データフレームとして|]}読み込む
文字列filepathから{TSVファイルを|[Pandasで|タブ区切りで|データフレームとして|]}読み込む
'''

# を指定せず=[を指定せず|を指定しないで|を無視して|を使わず]

pd.read_csv(filepath, header=None)
'''
@test(pd=missing;_)
{CSVファイルfilepathを|ヘッダ[を指定せず|なしで]}読み込む
文字列filepathから{CSVファイルを|ヘッダ[を指定せず|なしで]}読み込む
'''

pd.read_csv(filepath, index_col=n)
'''
@test(pd=missing;_)
{CSVファイルfilepathを|n番目のカラムをインデックス[と|に]して}読み込む
文字列filepathから{CSVファイルを|n番目のカラムをインデックス[と|に]して}読み込む
'''

# SJIS = [SJIS|シフトJIS]

pd.read_csv(filepath, encoding='shift_jis')
'''
@test(pd=missing;_)
{CSVファイルfilepathを|[SJISで|文字化けしないように]}読み込む
文字列filepathから{CSVファイルを|[SJISで|文字化けしないように]}読み込む
'''

sns.load_dataset('iris')
'''
@test(pd=missing;_)
[アヤメ|アイリス]のデータセットを[データフレームとして|]ロードする
'''

# write

df.to_excel(filepath)
'''
@test(df=missing;_)
@alt(ファイル名|名前)
{dfを|エクセルファイルfilepathに}書き出す
{dfを|文字列filepathというファイル名で|エクセル[ファイル|形式|]として}書き出す
'''

df.to_csv(filepath)
'''
@test(df=missing;_)
{dfを|CSVファイルfilepathに}書き出す
{dfを|文字列filepathというファイル名で|CSV[ファイル|形式|]として}書き出す
'''

df.to_csv(filepath, header=None)
'''
@test(df=missing;_)
@alt(を付けずに|を付けないで|なしで|を無視して)
{dfを|CSVファイルfilepathに|ヘッダを付けずに}書き出す
{dfを|ヘッダを付けずに|文字列filepathというファイル名で|CSV[ファイル|形式|]として}書き出す
'''

df.to_csv(filepath, index=None)
'''
@test(df=missing;_)
{dfを|CSVファイルfilepathに|インデックスを付けずに}書き出す
{dfを|インデックスを付けずに|文字列filepathというファイル名で|CSV[ファイル|形式|]として}書き出す
'''

df.to_csv(filepath, encoding='utf_8_sig')
'''
@test(df=missing;_)
@alt(を付けて|を付きで|ありで)
[Excelで|]文字化けしないCSVファイルを書き出す
{dfを|CSVファイルfilepathに|[BOMを付けて|文字化けしないように]}書き出す
{dfを|文字化けしないようにに|文字列filepathに}書き出す
'''

df.to_csv(filepath, encoding='shift_jis')
'''
@test(df=missing;_)
{SJISで|CSVファイルを}書き出す
{dfを|CSVファイルfilepathに|SJISで}書き出す
{dfを|SJISで|文字列filepathに}書き出す
'''

df.to_csv(filepath, sep='\t')
'''
@test(df=missing;_)
{タブ区切りで|TSVファイルを}書き出す
{dfを|TSVファイルfilepathに}書き出す
{dfを|タブ区切りで|文字列filepathに}書き出す
'''

df.to_csv(filepath, float_format='%.3f')
'''
@test(pd=missing;_)
保存するCSVファイルの小数点以下の桁数を設定する
{dfを|CSVファイルfilepathに|小数点以下3桁まで}書き出す
{dfを|小数点以下3桁まで|文字列filepathに}書き出す
'''

# 確認系

df.head()
'''
@alt(を見る|を[確認する|調べる])
dfの内容を確認する
dfの[先頭|最初][|を見る]
'''

df.head(n)
'''
dfの[先頭|最初|上]n行を抽出する
'''

df.tail()
'''
dfの[末尾|最後][|を見る]
'''

df.tail(n)
'''
dfの[末尾|最後|下]n行を取り出す
'''

df.sample()
'''
dfからランダムに[|一行を]抽出する
'''

df.sample(n)
'''
dfから{ランダムに|n行を}抽出する
'''

df.sample(n, replace=True)
'''
dfから{重複[ありで|を認めて]|ランダムに|n行を}抽出する
'''

n2 = 3
df[n:n2]
'''
@alt(取り出す|抽出する|[選択する|選ぶ])
dfのn行目からn2行目までを取り出す
'''

df[n:]
'''
dfのn行[|目][以降|より後ろ]を取り出す
'''

df[:n]
'''
dfのn行[|目][まで|より前]を取り出す
'''

df[col]
'''
df[の|から|において]colを取り出す
'''

df[col].values
'''
@(に変換する|にする|化する)
{df[の|から]colを|配列として}取り出す
dfのcolを配列に変換する
'''

df[col].values.tolist()
'''
{df[の|から]colを|リストとして}取り出す
dfのcolをリストに変換する
'''

df[[col, col2]]
'''
df[の|から]colとcol2[を|のみ]だけ][選択する|取り出す]
'''

df[[col, col2, col3]]
'''
df[の|から]col、col2、col3[を|のみ]だけ][選択する|取り出す]
'''

alist = ['A', 'B']
df[alist]
'''
@test(alist=['A','B'];_)
@alt(指定された|与えられた)
df[の|から]alist[[|で指定された]カラム][を|のみ]だけ][選択する|取り出す]
'''

df.loc[n]
'''
dfのn[行目|番目の行]を取り出す
dfのインデックスがnの行を取り出す
'''

# df.iloc[[1,2,4],[0,2]]   @@get @@it
# @type(df)内の1,2,4行目の0,2列目

df.info()
'''
dfのカラム[一覧|概要][|を見る]
'''

df.columns
'''
@alt(を得る|を見る|を調べる)
@alt(の名前|名|)
@alt(の一覧|一覧|[|の]リスト)
dfのカラムの名前の一覧[|を得る]
'''

df.select_dtypes('object').columns
'''
@alt(カテゴリーデータ|[質的データ|数値データ以外])
dfからカテゴリデータのカラムの名前の一覧[|を得る]
'''

ty = int
df.select_dtypes(ty).columns
'''
@test(ty='object';_)
dfからty[|型]のカラムの名前の一覧[|を得る]
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
dfの[|カラムの]データ型一覧[|を得る]
'''

df.select_dtypes(include=alist)
'''
@test(alist=['object'];_)
dfからalist[で指定された|の]データ型のカラム[を|のみ|だけ]取り出す
'''

df.select_dtypes(exclude=alist)
'''
@test(alist=['object'];_)
dfからalist[で指定された|の]データ型のカラム[を|のみ|だけ]除外する
'''

__X__ = 'object'
df.select_dtypes(__X__)
'''
@X('object';'number';ty)
@Y(カテゴリデータ;数値データ;ty[|型])
dfから__Y__[のカラム][を|のみ|だけ]取り出す
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
@test(alist=['A', 'B'];_)
@X(df;df[[col, col2]];df[alist])
@Y(df;dfのcolとcol2;dfのalist[|で指定された]カラム)
__Y__の[相関行列|各列間の相関係数][|を求める]
'''

__X__.corr(method='pearson')
'''
@test(alist=['A', 'B'];_)
{ピアソン[[|積率]相関係数]で_|__Y__の相関行列}[|を求める]
'''

__X__.corr(method='kendall')
'''
@test(alist=['A', 'B'];_)
{ケンドール[[|順位]相関係数|]で_|__Y__の相関行列}[|を求める]
'''

__X__.corr(method='spearman')
'''
@test(alist=['A', 'B'];_)
{スピアマン[[|順位]相関係数|]で_|__Y__の相関行列}[|を求める]
'''

sns.heatmap(__X__.corr())
'''
@test(alist=['A', 'B'];_)
@alt(描画する|グラフ化する)
__Y__の相関行列をヒートマップで_描画する
'''


df.describe(include='O')
'''
@alt(求める|[計算する|算出する]|[見る|確認する])
@alt(要約統計量|[記述統計量|基本統計量|代表値])
dfのカテゴリデータの要約統計量[|を求める]
'''

__X__ = df

__X__.describe()
'''
@X(df|df[alist]|ds|df[col])
@Y(df|dfのalistカラム|ds|dfのcol)
@test(alist=['A','B'];_)

__Y__の要約統計量[|を求める]
'''

__X__.mean()
'''
@test(alist=['A','B'];_)
@alt(平均値|平均)
__Y__の平均値[|を求める]
'''

__X__.median()
'''
@test(alist=['A','B'];_)
@alt(中央値|メディアン|第二四分位数|50パーセンタイル)
__Y__の中央値[|を求める]
'''

__X__.quantile(0.25)
'''
@test(alist=['A','B'];_)
@alt(第一四分位数|25パーセンタイル|上位25%)
__Y__の第一四分位数[|を求める]
'''

__X__.quantile(0.75)
'''
@test(alist=['A','B'];_)
@alt(第三四分位数|75パーセンタイル|下位25%)
__Y__の第三四分位数
'''

__X__.quantile(n/100)
'''
@test(alist=['A','B'];_)
__Y__のn[分位数|パーセンタイル][|を求める]
'''

__X__.mode()
'''
@test(alist=['A','B'];_)
@alt(最頻値|モード)
__Y__の[最頻値|どの値が頻出か][|を求める]
'''

__X__.freq()
'''
@test(alist=['A','B'];_)
__Y__の最頻値の出現回数[|を求める]
'''

__X__.std()
'''
@test(alist=['A','B'];_)
@alt(標本標準偏差|標準偏差)
__Y__の標本標準偏差[|を求める]
'''

__X__.std(ddof=0)
'''
@test(alist=['A','B'];_)
__Y__の母標準偏差[|を求める]
'''

__X__.var()
'''
__Y__の分散[|を求める]
'''

__X__.kurt()
'''
__Y__の[歪度|正規分布に対する左右対称性][|を求める]
__Y__が_正規分布からどれだけ歪んでいるか求める
'''

__X__.skew()
'''
__Y__の[尖度|正規分布に対する上下広がり][|を求める]
__Y__が_正規分布からどれだけ尖っているか求める
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

# ds の操作

__X__.round()
'''
@X(ds;df[col])
@Y(ds;dfのcol)
__Y__を[|整数に]丸める
'''

__X__.round(n)
'''
@X(ds;df[col])
@Y(ds;dfのcol)
__Y__を小数点以下n桁で丸める
'''

__X__.round(-1)
'''
__Y__を[10|十]の位で丸める
'''

__X__.round(-2)
'''
__Y__を[100|百]の位で丸める
'''

__X__.round(-3)
'''
__Y__を[1000|千]の位で丸める
'''

__X__.round().astype(int)
'''
@alt(丸めて|四捨五入して)
@alt(整数型|整数)
__Y__を丸めて、整数型にする
'''

__X__.round(-1).astype(int)
'''
__Y__を[10|十]の位で丸めて、整数型にする
'''

__X__.round(-2).astype(int)
'''
__Y__を[100|百]の位で丸めて、整数型にする
'''

__X__.round(-3).astype(int)
'''
__Y__を[1000|千]の位で丸めて、整数型にする
'''


__X__.value_counts()
'''
__Y__の各データ値の出現[|回]数[|を求める]
'''

__X__.unique()
'''
__Y__の[ユニーク|一意]な[値|要素][|を見る]
'''

__X__.nunique()
'''
__Y__の[ユニーク|一意]な[値の個数|要素数][|を見る]
'''

# 変更する
s, s2 = 'A', 'a'

df.rename(columns={col: s})
'''
@alt(リネームする|名前変更する)
dfのカラムの名前を[変更する|付け直す]
dfのカラムの名前をcolからsに[変更する|付け直す]
dfのcolをsにリネームする
'''

df.columns = [str(x).replace(s, s2) for x in df.columns]
'''
dfのカラム名をまとめて、sをs2に置換する
'''

df.rename(index={s: s2})
'''
dfのインデックスの名前をsからs2に[変更する|付け直す]
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

__X__ = df['A']

pd.to_datetime(__X__)
'''
@X(df[col]|ds)
@Y(dfのcol|ds)
@alt(日付型|タイムスタンプ型|timestamp型|datetime64型)
__Y__を日付型に変換する
'''

pd.to_datetime(__X__, format='%Y-%m-%d')
'''
@alt(フォーマット|書式)
{フォーマットを[指定して|使って]|__Y__を}日付型に変換する
'''

# エポック秒

pd.to_datetime(__X__, unit='s', utc=True)
'''
@alt(エポック秒|UNIX秒|UNIX時間|エポック)
エポック秒から日付型に変換する
__Y__のエポック秒から[日付型|timestamp型|datetime64型]に変換する
'''

__X__.tz_convert('Asia/Tokyo')
'''
__Y__のタイムゾーンを[日本|東京]に設定する
'''

__X__.tz_convert(s)
'''
__Y__のタイムゾーンをsに設定する
'''

__X__.dt.year
'''
__Y__の年[|を得る]
'''

__X__.dt.month
'''
__Y__の月[|を得る]
'''

__X__.dt.day
'''
__Y__の[日|日にち][|を得る]
'''

__X__.dt.hour
'''
__Y__の[時|時刻][|を得る]
'''

__X__.dt.minute
'''
__Y__の分[|を得る]
'''

__X__.dt.second
'''
__Y__の秒[|を得る]
'''

__X__.dt.weekday_name
'''
__Y__の曜日[名|の名前][|を得る]
'''

__X__.dt.dayofweek
'''
__Y__の曜日数[|を得る]
'''

# 演算処理系

# df['temperature'].diff(periods=1)   @ @let @ @calc

# @type(df)の@type('temperature', カラム)内の前後の行の差分


# 行列操作


# フィルター
x = 1.0
x2 = 2.0

df[df[col] == x]
'''
@alt(を抽出する|[のみ|だけ]残す|を選択する)
@alt(フィルタする|消す|取り除く)
dfのcol[|の値]がx[の|である][行|データ]を抽出する
dfのcol[|の値]がxでない[行|データ]をフィルタする
'''

df[(df[col] == x) & (df[col2] == x2)]
'''
dfの[行|データ]を条件でフィルタするには
dfのcol[|の値]がx、かつcol2がx2である[行|データ]を抽出する
'''

df[df[col] < x]
'''
dfのcol[|の値]がx[より[小さい|少ない]|未満の][行|データ]を抽出する
'''

df[df[col] <= x]
'''
dfのcol[|の値]がx以下の[行|データ]を抽出する
'''

df[df[col] > x]
'''
dfのcol[|の値]がxより[大きい|多い][行|データ]を抽出する
'''

df[df[col] >= x]
'''
dfのcol[|の値]がx以上の[行|データ]を抽出する
'''

df[(x < df[col]) & (df[col] < x2)]
'''
dfのcol[|の値]がxより[大きく|多く]x2より[小さい|少ない][行|データ]を抽出する
'''

df[(x <= df[col]) & (df[col] < x2)]
'''
dfのcol[|の値]がx以上かつx2未満の[行|データ]を抽出する
'''

value_list = ['A', 'B']
df[df[col].isin(value_list)]
'''
dfのcol[|の値]がvalue_listに含まれる[行|データ]を抽出する
'''

s = 'A'

df[df[col].str.contains(s)]
'''
dfのcol[|の文字列][が|で]sが含まれる[行|データ]を抽出する
'''

df[not df[col].str.contains(s)]
'''
dfのcol[|の文字列][が|で]sが含まれない[行|データ]を抽出する
'''

df[df[col].str.match(s)]
'''
dfのcol[|の文字列]が正規表現sにマッチする[行|データ]を抽出する
'''

df[not df[col].str.match(s)]
'''
dfのcol[|の文字列]が正規表現sにマッチしない[行|データ]を抽出する
'''

df[df[col].str.startswith(s)]
'''
dfのcol[|の文字列]がsで始まる[行|データ]を抽出する
'''

df[not df[col].str.startswith(s)]
'''
dfのcol[|の文字列]がsで始まらない[行|データ]を抽出する
'''

df[df[col].str.endswith(s)]
'''
dfのcol[|の文字列]がsで終わる[行|データ]を抽出する
'''

df[not df[col].str.endswith(s)]
'''
dfのcol[|の文字列]がsで終わらない[行|データ]を抽出する
'''

__X__.str.len()
'''
__Y__の文字列長を列として得る
'''

# ドロップ・欠損値処理

# ドロップする =

df.style.highlight_null()
'''
@alt(付け|つけ)
dfの欠損値が[含まれる|ある][箇所|部分][に[色を付ける]|を[色付けする]]
'''

df.drop(n)
'''
@alt(ドロップする|削除する|消す|[落とす|取り除く])
@alt(ドロップして|[削除し|消し|取り除い][て|、])
dfのn行目をドロップする
'''

df.drop(col, axis=1)
'''
dfのcolをドロップする
'''

df.drop(col, axis=1, inplace=True)
'''
@alt(_変更を反映する|入れ替える|更新する)
dfのcolをドロップして_変更を反映する
'''

df.drop([col, col2], axis=1)
'''
dfのcolとcol2をドロップする
'''

df.dropna()
'''
@alt(_の|[内|中]の|において)
df_の欠損値が[ある|存在する]行をドロップする
'''

df.dropna(how='all')
'''
dfから全ての値が欠損値[になっている|である]行[のみ|だけ]をドロップする
'''

__X__.fillna(x)
'''
@X(df[col]|ds)
@Y(dfのcol|ds)
@alt(埋める|置き換える)
{__Y__の欠損値を|xで}埋める
__Y__の欠損値をxに設定する
'''


__X__.fillna(method='ffill')
'''
__Y__の欠損値を直前の行の値で[埋める|補う]
'''


@type(df)内の欠損値を直前の行の値で[埋める | 補う]
__X__.fillna(__X__.mean())
'''
{__X__の欠損値を|平均値で}埋める
__Y__の欠損値を平均値に設定する
'''


__X__.replace(s, np.nan)
'''
__Y__ _のsを欠損値に[置換する|置き換える]
'''

__X__.replace(value, np.nan).dropna()
'''
__Y__ _のvalueのある行をドロップする
'''


# マージ

pd.merge(df1, df2)
'''
{dfとdf2を|[横方向に|横に|]}[マージする|結合する|結合|一つにまとめる|1つにする|一つにする|1つにまとめる|くっつける|合わせる]
'''

pd.merge(df, df2, on=col)
'''
dfとdf2をcolをキー[に|と]して、結合する
'''


pd.merge(df1, df2, how='outer')   @ @let
[全結合で | 両方の列を使って | 片方のテーブルにしかないデータも全て残して]@type(df1)と@type(df2)をマージする

pd.merge(df1, df2, left_index=True, right_on='index_num')   @ @let
{{左側のデータのインデックス}と{[右側のデータの |]@type('index_num', カラム)}をキー}として、@ type(df1)と@type(df2)をマージする

pd.merge(df1, df2, how='left')   @ @let
[左外部結合で | 左側のデータフレームに合わせて]@type(df1)と@type(df2)をマージする

pd.concat([df, df2])
'''
{dfとdf2を|[縦方向に|縦に|]}[連結する|結合する|つなぐ|マージする]
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


# 重複

df.duplicated()
'''
dfの重複した行数のマスク[|を得る]
'''

df.duplicated().sum()
'''
dfの重複した行数[|を
'''

df[df.duplicated()]
'''
dfの重複した行を抽出する
'''

df.duplicated(subset=col)
'''
dfのcolに重複が
'''

df.duplicated(subset=['state', 'point'])     @ @check


@type(df)内の@type('state', カラム)と@type('point', カラム)に重複[が | は]{あるのかどうか}判定する
@type(df)内の@type('state', カラム)と@type('point', カラム)に重複[が | は]{あるのかどうか}
df.drop_duplicates()
'''
dfから重複[した行|]をドロップする
'''

df.drop_duplicates(inplace=True)
'''
dfから重複[した行|]をドロップして、インプレイスする
'''

df.drop_duplicates(keep=False)
'''
{dfから重複[した行|]|重複した最後の行を残して}をドロップする
'''

df.drop_duplicates(subset=col)
'''
dfのcol[が重複した|に重複のある]行をドロップする
'''

df.drop_duplicates(subset=[col, col2])
'''
dfのcolとcol2[が[|両方とも]重複した|に重複のある]行をドロップする
'''

# ビン

pd.cut(df['birth_year'], data_bins)   @ @let
{境界値を@type(data_bins, リスト)}として、@ type(df)の@type('birth_year', カラム)を[ビン分割する | 分割する]

pd.cut(df['birth_year'], bins_num)   @ @let
{[ビン数 | 分割数]をbins_num}として、@ type(df)の@type('birth_year')をビン分割する

pd.cut(df['birth_year'], bins_num, label=group_names)   @ @let
{ビン数をbins_num}、{ビンの[ラベル | 名前]を@type(group_names, リスト)}として、@ type(df)の@type('birth_year')をビン分割する

pd.cut(df['birth_year'], bins_num, label=False)   @ @let
{ビン数をbins_num}、{ビンのラベルを[0始まりの連番 | インデックス | 整数値]}として、@ type(df)の@type('birth_year')をビン分割する

pd.qcut(df['birth_year'], 2)   @ @let


@type(df)の@type('birth_year')を中央値でビン分割する
pd.qcut(df['birth_year'], 4)   @ @let


@type(df)の@type('birth_year')を四分位数ごとでビン分割する
pd.qcut(df['birth_year'], bins_num)   @ @let
{ビン数をbins_num}として、@ type(df)の@type('birth_year')を[ビンに含まれる個数 | 要素数 | 要素の数]が等しくなるようにビン分割する


# グループ化

df.groupby(col)
'''
@alt(グループ化する|集[約|計]する|まとめる)
@alt(グループ化した|集[約|計]した|まとめた)
@alt(グループ化して|集[約|計]して|まとめて)
@alt(毎|ごと)
dfを[|各]col[で|毎に]グループ化する
'''

df.groupby(col, dropna=False)
'''
dfを{NaNを含めて|[|各]col[で|毎に]}グループ化する
'''


def func(x): return 'A'


df.groupby(func)
'''
@test(func=lamda x: 'A';_)
dfをfuncでグループ化する
'''

[(name, group) for name, group in df.groupby(col)]
'''
dfを[|各]col[で|毎に]グループ化して、列挙する
'''

[(name, group) for name, group in df.groupby([col, col2])]
'''
dfをcolとcol2の組み合わせ[で|毎に]グループ化して、列挙する
'''

df.groupby(col).get_group(s)
'''
dfを[|各]col[で|毎に]グループ化して、sという[|名前の]グループを得る
'''

df.groupby(col).size()
'''
dfを[|各]col[で|毎に]グループ化して、各グループの[個数|大きさ]を求める
'''

df.groupby(col).size()[s]
'''
dfを[|各]col[で|毎に]グループ化して、sというグループの[個数|大きさ]を求める
'''


df.groupby(col).__X__
'''
@X(sum()|mean()|count()|max()|min()|var()|std()|agg(func))
@Y(合計|平均値|個数|最大値|最小値|分散|標準偏差|関数適用した値)
dfの[|各]col毎の__Y__[|を求める]
dfを[|各]col[で|毎に][グループ化して、|グループ化した]__Y__を求める
'''

df.groupby([col, col2], as_index=False).__X__
'''
dfの[|各]colとcol2毎の__Y__[|を求める]
dfを[|各]colとcol2の組み合わせ[で|毎に]グループ化して、__Y__[|を求める]
'''


df.groupby(col)[col2].__X__
'''
dfを[|各]col[で|毎に]グループ化して、col2の__Y__を求める
'''

df.groupby(col).describe()[col2]
'''
dfを[|各]col[で|毎に]でグループ化して、col2の要約統計量を求める
'''


# ソートする=

__X__ = col
df.sort_values(by=col)
'''
@test(alist=['A'];_)
@alt(ソートする|[並べる|並べ直す|整列する])
@alt(ソートして|[並べて|並べ直して|整列して])
@X(col;[col,col2];alist)
@Y(col;colとcol2;alist[で指定された|の]カラム)
{df[|全体]を|__Y__[で|によって]}ソートする
'''

df.sort_values(by=__X__, inplace=True)
'''
{df[|全体]を|__Y__[で|によって]}ソートして、インプレイスする
'''

df.sort_values(by=__X__, ascending=True)
'''
{df[|全体]を|__Y__[で|によって]|[昇順に|小さい順に]}ソートする
'''

df.sort_values(by=__X__, ascending=False)
'''
{df[|全体]を|__Y__[で|によって]|[降順に|大きい順に]}ソートする
'''

df.sort_values(by=__X__, ascending=True, inplace=True)
'''
{df[|全体]を|__Y__[で|によって]|[昇順に|小さい順に]}ソートして、インプレイスする
'''

df.sort_values(by=__X__, ascending=False, inplace=True)
'''
{df[|全体]を|__Y__[で|によって]|[降順に|大きい順に]}ソートして、インプレイスする
'''

df.sort_values(by=__X__, na_position='first')
'''
df[|全体]を{__Y__[で|によって|を用いて]}ソートして、NaNは先頭に[|来るように]する
'''

# ソート

df.sort_index()
'''
df[|全体]をインデックス[で|によって]ソートする
'''

df.sort_index(ascending=False)
'''
df[|全体]をインデックス[を使って|によって][降順で|大きい順で]ソートする
'''


# null判定

__X__.isna()
'''
@X(df;ds;df[col])
@Y(df;ds;dfのcol)
__Y__[|内|中]の欠損値を[|全て]ブール値に変換する
'''

__X__.isna().sum()
'''
__Y__[|内|中]の欠損値の合計[|を得る]
'''

value = 1
__X__.isin([value])
'''
__Y__[|内|中]にvalueが含まれるとき、真に変換する
'''

__X__.isin([value]).sum()
'''
__Y__[|内|中]に[含まれる|存在する]valueの[個数|合計][|を得る]
__Y__[|内|中]に[含まれる|存在する]value[の個数]をカウントする
'''


# ダミー処理

pd.get_dummies(df)
'''
df内のカテゴリデータをダミー変数[に変換|化]する
'''

pd.get_dummies(df[col])
'''
dfのcolをダミー変数[化|に変換]する
'''

iterable = [1, 2, 1, 3]
pd.get_dummies(iterable)
'''
iterableをダミー変数[化|に変換]する
'''

pd.get_dummies(x, drop_first=True)
'''
{最初のカテゴリーを除外し[て、]|xを}ダミー変数[に変換|化]する
'''

pd.get_dummies(x, dummy_na=True)
'''
{NaNも加えて|xを}ダミー変数[に変換|化]する
'''

__X__.astype(object)
'''
@X(df[col]|ds)
@Y(dfのcol|ds)
__Y__をカテゴリデータに変換する
'''

__X__.map({s: 1, s2: 0})
'''
__Y__を[0と1|1と0]に[マップする|変換する]
'''

__X__.unique().tolist()
'''
__Y__からユニークな[要素|値]を抽出し、リスト化する
'''

set(ds.unique().tolist()+ds2.unique().tolist())
'''
dsとds2から重複を取り除く
'''


df[col] = df[col2].astype(ty)
'''
@alt(に代入する|[と|に]する)
dfのcol2をtyに変換し、[|新たに|dfの]colに代入する
'''
