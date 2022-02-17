import pandas as pd

import seaborn as sns

n = 1

filename='test.csv'
name, name2, name3 = 'A', 'B', 'C'
df = pd.DataFrame(data=[[1, 2, 3], [4, 5, 6]], columns=['A', 'B', 'C'])
df2 = df

# カラム = [カラム|列]
# データフレーム = [データフレーム|表|表データ]
# 設定する = [設定する|セットする|変更する|指定する|する]

pd.set_option('display.max_columns', n)
'''
[表示できる|表示される|表示する]最大カラム数を[変更する|増やす|減らす]
最大表示カラム数をnに設定する
[表示できる|表示される|表示する|表示]カラム数を[最大|]nカラムに設定する
データフレームが[最大|]nカラムまで表示できるようにする
'''

pd.set_option('display.max_rows', n)
'''
[表示できる|表示される|表示する]最大行数を[変更する|増やす|減らす]
最大表示行数をnに設定する
[表示できる|表示される|表示する|表示]行数を[最大|]n行に設定する
データフレームが[最大|]n行まで表示できるようにする
'''

pd.set_option('precision', n)
'''
小数点以下の表示精度を設定する
小数点以下[の表示精度|]をn桁に設定する
小数点以下n桁まで表示するように設定する
小数点以下n桁までデフォルトで表示する
'''

pd.set_option('expand_frame_repr', False)
'''
データフレームの折り返しをしないようにする
データフレームの折り返しを[オフ|無効]に設定する
'''

pd.set_option('max_colwidth', n)
'''
カラムの最大[表示]幅をnに設定する
'''

pd.set_option('colheader_justify', 'right')
'''
[カラム[の]]ヘッダーを右寄せに設定する
'''

pd.set_option('colheader_justify', 'left')
'''
[カラム[の]]ヘッダーを左寄せに設定する
'''

# read

# 読み込む = [読み込む|読む]

pd.read_excel(filename)
'''
{エクセルファイルfilenameを|[Pandasで|データフレームとして]}読み込む
文字列filenameからエクセル[データ]を読み込む
'''

pd.read_excel(filename, sheet_name=n)
'''
エクセルファイルfilenameを[Pandasで|データフレームとして|]読み込む
{エクセルファイルfilenameから|n番目のシートを}[Pandasで|データフレームとして|]読み込む
{エクセルファイルfilenameから|nという[名前の|]シートを}[Pandasで|データフレームとして|]読み込む
{エクセルファイルfilenameから|nとシートを指定し}[Pandasで|データフレームとして|]読み込む
'''

pd.read_csv(filename, sep=',')
'''
{テキストファイルfilenameを|カンマ区切りで|[Pandasで|データフレームとして|]}読み込む
{CSVファイルfilenameを|[Pandasで|データフレームとして|]}読み込む
文字列filenameから{CSVファイルを|[Pandasで|カンマ区切りで|データフレームとして|]}読み込む
'''

pd.read_csv(filename, sep='\t')
'''
{テキストファイルfilenameを|タブ区切りで|[Pandasで|データフレームとして|]}読み込む
{TSVファイルfilenameを|[Pandasで|データフレームとして|]}読み込む
文字列filenameから{TSVファイルを|[Pandasで|タブ区切りで|データフレームとして|]}読み込む
'''

# を指定せず=[を指定せず|を指定しないで|を無視して|を使わず]

pd.read_csv(filename, header=None)
'''
{CSVファイルfilenameを|ヘッダ[を指定せず|なしで]}読み込む
文字列filenameから{CSVファイルを|ヘッダ[を指定せず|なしで]}読み込む
'''

pd.read_csv('file.csv', index_col=n)
'''
{CSVファイルfilenameを|n番目のカラムをインデックス[と|に]して}読み込む
文字列filenameから{CSVファイルを|n番目のカラムをインデックス[と|に]して}読み込む
'''

# SJIS = [SJIS|シフトJIS]

pd.read_csv('file.csv', encoding='shift_jis')
'''
{CSVファイルfilenameを|[SJISで|文字化けしないように]}読み込む
文字列filenameから{CSVファイルを|[SJISで|文字化けしないように]}読み込む
'''

sns.load_dataset('iris')
'''
[アヤメ|アイリス]をデータフレームとして読み込む
'''

# write

# 書き出す = [書き出す|書き出す|保存する]
# ファイル名 = [名前|ファイル名]

df.to_excel(filename)
'''
{dfを|エクセルファイルfilenameに}書き出す
{dfを|文字列filenameというファイル名で|エクセル[ファイル|形式|]として}書き出す
'''

df.to_csv(filename)
'''
{dfを|CSVファイルfilenameに}書き出す
{dfを|文字列filenameというファイル名で|CSV[ファイル|形式|]として}書き出す
'''

df.to_csv(filename, header=None)
'''
@alt(を付けずに|を付けないで|なしで|を無視して)
{dfを|CSVファイルfilenameに|ヘッダを付けずに}書き出す
{dfを|ヘッダを付けずに|文字列filenameというファイル名で|CSV[ファイル|形式|]として}書き出す
'''

df.to_csv(filename, index=None)
'''
@alt(を付けずに|付けないで|なしで|を無視して)
{dfを|CSVファイルfilenameに|インデックスを付けずに}書き出す
{dfを|インデックスを付けずに|文字列filenameというファイル名で|CSV[ファイル|形式|]として}書き出す
'''

df.to_csv(filename, encoding='utf_8_sig')
'''
@alt(を付けて|を付きで|ありで)
[Excelで|]文字化けしないCSVファイルを書き出す
{dfを|CSVファイルfilenameに|[BOMを付けて|文字化けしないように]}書き出す
{dfを|文字化けしないようにに|文字列filenameに}書き出す
'''

df.to_csv(filename, encoding='shift_jis')
'''
{SJISで|CSVファイルを}書き出す
{dfを|CSVファイルfilenameに|SJISで}書き出す
{dfを|SJISで|文字列filenameに}書き出す
'''

df.to_csv(filename, sep='\t')
'''
{タブ区切りで|TSVファイルを}書き出す
{dfを|TSVファイルfilenameに}書き出す
{dfを|タブ区切りで|文字列filenameに}書き出す
'''

df.to_csv(filename, float_format='%.3f')
'''
保存するCSVファイルの小数点以下の桁数を設定するには
{dfを|CSVファイルfilenameに|小数点以下3桁まで}書き出す
{dfを|小数点以下3桁まで|文字列filenameに}書き出す
'''


# 確認系

df.head()
'''
dfの[先頭|最初|上]を見る
'''

df.head(n)
'''
dfの[先頭|最初|上]n行を取り出す
'''

df.tail()
'''
dfの[末尾|最後|下]を見る
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


df[start:end]
'''
dfのstart行目からend行目までを取り出す
'''

df[n:]
'''
dfのn行[|目][以降|より後ろ]を取り出す
'''

df[:n]
'''
dfのn行[|目][まで|より前]を取り出す
'''

# [取り出す|抽出する|選択する|選ぶ]

df[name]
'''
df[の|から]nameカラムを取り出す
df[の|から]文字列nameを取り出す
'''

df[name].values
'''
{df[の|から]nameカラムを|配列として}取り出す
{df[の|から]文字列nameを|配列として}取り出す
dfのnameカラムを配列に変換する
dfの文字列nameを配列に変換する
'''

df[name].values.tolist()
'''
{df[の|から]nameカラムを|リストとして}取り出す
{df[の|から]文字列nameを|リストとして}取り出す
dfのnameカラムをリストに変換する
dfの文字列nameをリストに変換する
'''

df[[name, name2]]
'''
df[の|から]nameカラム、name2カラムを取り出す
'''

df[[name, name2, name3]]
'''
df[の|から]nameカラム、name2カラム、name3カラムを取り出す
'''

df[ls]
'''
df[の|から]lsで指定されたカラムを取り出す
'''

df.loc[n]
'''
dfのn[行目|番目の行]を取り出す
dfのインデックスがnの行を取り出す
'''

df.iloc[[1,2,4],[0,2]]   @@get @@it
@type(df)内の1,2,4行目の0,2列目

df.info()
'''
dfの[カラム一覧|概要]を見る
'''

df.describe()
'''
@alt(要約統計量|統計情報|基礎統計量|統計的記述)
dfの要約統計量を見る
'''

df.describe(include='O')
'''
dfの[オブジェクトデータ|数値データ以外]の要約統計量を見る
'''

ds.describe()
'''
dsの要約統計量を見る
'''

df[name].describe()
'''
dfのnameカラムの要約統計量を見る
'''

__X__=df

__X__.mean()
'''
@X(df:ds:df[name])
@Y(df:ds:dfのnameカラム)
__Y__の平均値を求める
'''

__X__.median()
'''
__Y__の[中央値|中央値|第二四分位数|50パーセンタイル]を求める
'''

__X__.quantile(0.25)
'''
__Y__の[第一四分位数|25パーセンタイル]を求める
'''

__X__.quantile(0.75)
'''
__Y__の[第三四分位数|75パーセンタイル]を求める
'''

__X__.mode()
'''
__Y__の最頻値を求める
'''

__X__.freq()
'''
__Y__の最頻値の出現回数を求める
'''

__X__.std()
'''
__Y__の標準偏差を求める
'''

__X__.var()
'''
__Y__の分散を求める
'''

df.round()
'''
df[の数値|]を[全て|][|整数に][四捨五入する|丸める]
'''

df.round(n)
'''
df[の数値|]を[全て|]小数点以下n桁に[四捨五入する|丸める]
'''

ds.round()
'''
dsを[|整数に][四捨五入する|丸める]
'''

ds.round(n)
'''
dsを小数点以下n桁に[四捨五入する|丸める]
'''

ds.round().astype(int)
'''
dsを[丸めて|四捨五入して]整数[化する|に変換する]
'''

ds.round(-1).astype(int)
'''
dsを[10|十]の位で[丸めて|四捨五入して]整数[化する|に変換する]
'''

ds.round(-2).astype(int)
'''
dsを[100|百]の位で[丸めて|四捨五入して]整数[化する|に変換する]
'''

ds.round(-3).astype(int)
'''
dsを[1000|千]の位で[丸めて|四捨五入して]整数[化する|に変換する]
'''


df.columns
'''
dfのカラム[名[|の]|の名前|]一覧を得る
'''

df.select_dtypes('object').columns
'''
dfからカテゴリデータのカラム[名|]一覧を得る
'''

df.index
'''
dfのインデックス[名|]一覧を得る
'''

df.values
'''
dfを配列に変換する
'''

df.dtypes
'''
dfの[|カラムの]データ型[|の]一覧
'''

name_or_list=''
df.select_dtypes(include=name_or_list, exclude=name_or_list)
'''
dfから[|特定の|指定の]データ型のカラムを抽出する
'''

df.select_dtypes('object')
'''
dfからカテゴリデータ[のカラム]を抽出する
'''

df.select_dtypes('number')
'''
dfから量的データ[のカラム]を抽出する
'''

# df.shape  @@check @@it
# @type(df)の[行数や列数|行数と列数|形状]

df[name].value_counts()
'''

'''
# @type(df)の@type('weather', カラム)の[各要素の|それぞれのデータの|][出現頻度|出現回数]

# df['remarks'].unique()  @@check @@it
# @type(df)の@type('remarks', カラム)の[ユニーク値|一意の値|データの種類|ユニークな要素]

# df['remarks'].nunique()  @@check @@it
# @type(df)の@type('remarks', カラム)の[ユニークな要素の数|ユニークな要素の個数|ユニークな要素数|データの種類の数]


# 設定系

# 変更する
s,s2 = 'A','a'

df.rename(columns={name: s})
'''
dfのカラム[名|の名前]を変更する
dfのカラム[名|の名前]をnameカラムからsに変更する
'''

df.columns = [str(x).replace(s, s2) for x in df.columns]
'''
dfの全てのカラム名をsからs2に置き換える
'''

# df.rename(index={'ONE': 'Row_1'})
# @type(df)のインデックス名を'ONE'から'Row_1'にリネームする
# @type(df)の@type('ONE', インデックス)の名前を'Row_1'にリネームする

df.set_index(name)
'''
dfのnameカラムをインデックスに設定する
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
@X(df[name]|ds)
@Y(dfのnameカラム|ds)
@alt(日付型|タイムスタンプ型|timestamp型|datetime64型)
__Y__を日付型に変換する
'''

pd.to_datetime(__X__, format='%Y-%m-%d')
'''
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
__Y__の年
'''

__X__.dt.month
'''
__Y__の月
'''

__X__.dt.day
'''
__Y__の[日|日にち]
'''

__X__.dt.hour
'''
__Y__の[時|時刻]
'''

__X__.dt.minute
'''
__Y__の分
'''

__X__.dt.second
'''
__Y__の秒
'''

__X__.dt.weekday_name
'''
__Y__の曜日[名|の名前]
'''

__X__.dt.dayofweek
'''
__Y__の曜日
'''


# 演算処理系

df['temperature'].diff(periods=1)   @@let @@calc
@type(df)の@type('temperature', カラム)内の前後の行の差分

df.corr()   @@check @@it
@type(df)の[相関係数|相関]

df[['kcal', 'sales']].corr()   @@check
@type(df)の@type('kcal', カラム)と@type('sales', カラム)の相関係数


# 行列操作

df.T
@type(df)の[行と列|行列]を[入れ替える|入れかえる]
@type(df)を転置する


# フィルター
x = 1.0
x2 = 2.0

df[df[name] == x]
'''
@alt(を抽出する|[のみ|だけ]残す|を選択する)
@alt(フィルタする|消す|取り除く)
dfのnameカラム[|の値]がx[の|である][行|データ]を抽出する
dfのnameカラム[|の値]がxでない[行|データ]をフィルタする
'''

df[(df[name] == x) & (df[name2] == x2)]
'''
dfの[行|データ]を条件でフィルタするには
dfのnameカラム[|の値]がx、かつname2カラムがx2である[行|データ]を抽出する
'''

df[df[name] < x]
'''
dfのnameカラム[|の値]がx[より[小さい|少ない]|未満の][行|データ]を抽出する
'''

df[df[name] <= x]
'''
dfのnameカラム[|の値]がx以下の[行|データ]を抽出する
'''

df[df[name] > x]
'''
dfのnameカラム[|の値]がxより[大きい|多い][行|データ]を抽出する
'''

df[df[name] >= x]
'''
dfのnameカラム[|の値]がx以上の[行|データ]を抽出する
'''

df[(x < df[name]) & (df[name] < x2)]
'''
dfのnameカラム[|の値]がxより[大きく|多く]x2より[小さい|少ない][行|データ]を抽出する
'''

df[(x <= df[name]) & (df[name] < x2)]
'''
dfのnameカラム[|の値]がx以上かつx2未満の[行|データ]を抽出する
'''

value_list = ['A', 'B']
df[df[name].isin(value_list)]
'''
dfのnameカラム[|の値]がvalue_listに含まれる[行|データ]を抽出する
'''

s='A'

df[df[name].str.contains(s)]
'''
dfのnameカラム[|の文字列][が|で]sが含まれる[行|データ]を抽出する
'''

df[not df[name].str.contains(s)]
'''
dfのnameカラム[|の文字列][が|で]sが含まれない[行|データ]を抽出する
'''

df[df[name].str.match(s)]
'''
dfのnameカラム[|の文字列]が正規表現sにマッチする[行|データ]を抽出する
'''

df[not df[name].str.match(s)]
'''
dfのnameカラム[|の文字列]が正規表現sにマッチしない[行|データ]を抽出する
'''

df[df[name].str.startswith(s)]
'''
dfのnameカラム[|の文字列]がsで始まる[行|データ]を抽出する
'''

df[not df[name].str.startswith(s)]
'''
dfのnameカラム[|の文字列]がsで始まらない[行|データ]を抽出する
'''

df[df[name].str.endswith(s)]
'''
dfのnameカラム[|の文字列]がsで終わる[行|データ]を抽出する
'''

df[not df[name].str.endswith(s)]
'''
dfのnameカラム[|の文字列]がsで終わらない[行|データ]を抽出する
'''

__X__.str.len()
'''
__Y__の文字列長を列として得る
'''

# ドロップ・欠損値処理

## ドロップする = 

df.style.highlight_null()
@type(df)内の欠損値が[含まれる|ある][箇所|部分]に{色をつける}
@type(df)内の欠損値が含まれる[箇所|部分]を色付けする

df.drop(n)
'''
@alt(ドロップする|削除する|消す|落とす|取り除く)
dfのn行目をドロップする
'''

df.drop(name, axis=1)
'''
dfのnameカラムをドロップする
'''

df.drop([name, name2], axis=1)
'''
dfのnameカラムとname2カラムをドロップする
'''

df.dropna()
'''
df[|内|中]の欠損値が[存在する|ある]行をドロップする
'''

@type(df)内の[欠損値|欠損|NaN|未記入の値|未入力の値]が[存在する|ある]行をドロップする
@type(df)内の欠損値[を含む行|]をドロップする
{@type(df)の欠損値がある行を}ドロップする

__X__.fillna(x)
'''
@X(df[name]|ds)
@Y(dfのnameカラム|ds)
@alt(埋める|置き換える)
{__Y__の欠損値を|xで}埋める
__Y__の欠損値をxに設定する
'''

df.fillna(method='ffill')   @@let @@let_self @@inplace
@type(df)内の欠損値を直前の行の値で[埋める|補う]

df.fillna(df.mean())
'''
{__X__の欠損値を|平均値で}埋める
__Y__の欠損値を平均値に設定する
'''

df.replace('?', np.nan).dropna()   @@let @@let_self @@inplace
@type(df)内の'?'を{欠損値に[置換し|置き換え|変え]}{欠損値が存在する行をドロップする}

df.replace('?', np.nan)   @@let @@let_self @@inplace
{@type(df)内に存在する'?'を}欠損値[に|で]置換する
@type(df)の'?'を欠損値[に|で]置換する
{@type(df)内に存在する'?'を}欠損値[で埋める|とする|にする]
@type(df)の'?'を欠損値[で埋める|とする|にする]


# マージ

pd.merge(df1, df2)
'''
{dfとdf2を|[横方向に|横に|]}[マージする|結合する|結合|一つにまとめる|1つにする|一つにする|1つにまとめる|くっつける|合わせる]
'''

pd.merge(df, df2, on=name)
'''
dfとdf2をnameカラムをキー[に|と]して、結合する
'''



pd.merge(df1, df2, how='outer')   @@let
[全結合で|両方の列を使って|片方のテーブルにしかないデータも全て残して]@type(df1)と@type(df2)をマージする

pd.merge(df1, df2, left_index=True, right_on='index_num')   @@let
{{左側のデータのインデックス}と{[右側のデータの|]@type('index_num', カラム)}をキー}として、@type(df1)と@type(df2)をマージする

pd.merge(df1, df2, how='left')   @@let
[左外部結合で|左側のデータフレームに合わせて]@type(df1)と@type(df2)をマージする

pd.concat([df, df2])
'''
{dfとdf2を|[縦方向に|縦に|]}[連結する|結合する|つなぐ|マージする]
'''

# ピボットテーブル

df.pivot_table(index='Pclass', columns='Sex')   @@let
@type(df)の{@type('Pclass', カラム)をインデックス}、{@type('Sex', カラム)をカラム}としたピボットテーブルを作成する

df.pivot_table(index='Pclass', columns='Sex', values='Age')   @@let
@type(df)の@type('Age', カラム)について、{@type('Pclass')をインデックス}、{@type('Sex')をカラム}としたピボットテーブルを作成する


# ピボット操作

df.stack()
ピボット操作で@type(df)の{列を行に}[入れ替える|変更する]
ピボット操作で@type(df)の{列を行と}逆にする

df.unstack()
ピボット操作で@type(df)の{行を列に}入れ替える
ピボット操作で@type(df)の{行を列と}逆にする


# 重複

df.duplicated()

df.duplicated().sum()
'''
dfの重複した行数を求める
'''

df[df.duplicated()]
'''
dfの重複した行を抽出する
'''

df.duplicated(subset=name)
'''
dfのnameカラムに重複が
'''

df.duplicated(subset=['state', 'point'])     @@check
@type(df)内の@type('state', カラム)と@type('point', カラム)に重複[が|は]{あるのかどうか}判定する
@type(df)内の@type('state', カラム)と@type('point', カラム)に重複[が|は]{あるのかどうか}

df.drop_duplicates()
'''
dfから重複[した行|]をドロップする
'''

df.drop_duplicates(inplace=True)
'''
dfから重複[した行|]をドロップし[|て]、置き換える
'''

df.drop_duplicates(keep=False)   @@let @@let_self @@inplace
{重複した最後の行を残して}@type(df)内の重複している行をドロップする

df.drop_duplicates(subset='state')   @@let @@let_self @@inplace
@type(df)内の{@type('state')の重複した行}をドロップする
@type(df)内の{@type('state')に重複がある行}をドロップする


# ビン

pd.cut(df['birth_year'], data_bins)   @@let
{境界値を@type(data_bins, リスト)}として、@type(df)の@type('birth_year', カラム)を[ビン分割する|分割する]

pd.cut(df['birth_year'], bins_num)   @@let
{[ビン数|分割数]をbins_num}として、@type(df)の@type('birth_year')をビン分割する

pd.cut(df['birth_year'], bins_num, label=group_names)   @@let
{ビン数をbins_num}、{ビンの[ラベル|名前]を@type(group_names, リスト)}として、@type(df)の@type('birth_year')をビン分割する

pd.cut(df['birth_year'], bins_num, label=False)   @@let
{ビン数をbins_num}、{ビンのラベルを[0始まりの連番|インデックス|整数値]}として、@type(df)の@type('birth_year')をビン分割する

pd.qcut(df['birth_year'], 2)   @@let
@type(df)の@type('birth_year')を中央値でビン分割する

pd.qcut(df['birth_year'], 4)   @@let
@type(df)の@type('birth_year')を四分位数ごとでビン分割する

pd.qcut(df['birth_year'], bins_num)   @@let
{ビン数をbins_num}として、@type(df)の@type('birth_year')を[ビンに含まれる個数|要素数|要素の数]が等しくなるようにビン分割する


# グループ化

df.groupby(name).__X__
'''
@X(sum()|mean()|count()|max()|min()|var()|std()|agg(func))
@Y(合計|平均値|個数|最大値|最小値|分散|標準偏差|関数適用で要約)
dfのnameカラム[ごと|毎]の__Y__を求める
dfをnameカラムでグループ化し[|て]、__Y__を求める
'''

df.groupby([name, name2], as_index=False).__X__
'''
dfのnameカラムとname2カラム[ごと|毎]に__Y__を求める
dfをnameカラムとname2カラムでグループ化し[|て]、__Y__を求める
'''

df.groupby(name).size()
'''
dfをnameカラムでグループ化し[|て]、その個数を求める
'''

df.groupby(name)[name2].__X__
'''
dfをnameカラムでグループ化し[|て]、name2カラムの__Y__を求める
'''

df.groupby(name).describe()[name2]
'''
dfをnameカラム[|ごと|毎]でグループ化し、name2カラムの要約統計量を求める

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

# ソートする=

df.sort_values(name)
'''
df[|全体]をnameカラム[で|によって]ソートする
'''

df.sort_values(name, inplace=True)
'''
dfをnameカラム[で|によって]ソートし[|て]、置き換える
'''

df.sort_values(name, ascending=True)
'''
dfを{nameカラム[で|によって]|[昇順に|小さい順に]}ソートする
'''

df.sort_values(name, ascending=False)
'''
dfを{nameカラム[で|によって]|[降順に|大きい順に]}ソートする
'''

df.sort_values(name, na_position='first')
'''
dfを{nameカラム[で|によって|を用いて]}ソートし[|て]、NaNは先頭に[|来るように]する
'''

df.sort_values([name, name2])
'''
df[|全体]をnameカラムとname2カラム[で|によって]ソートする
'''


# null判定

__X__.isna()
'''
__Y__[|内|中]の欠損値を[|全て]ブール値に変換する
'''

__X__.isna().sum()
'''
__Y__[|内|中]の欠損値の合計を得る
'''

__X__.isin([x])
'''
__Y__[|内|中]にxが含まれるとき、真に変換する
'''

__X__.isin([x]).sum()
'''
__Y__[|内|中]に[含まれる|存在する]xの[個数|合計]を得る
__Y__[|内|中]に[含まれる|存在する]x[の個数]をカウントする
'''


# ダミー処理

pd.get_dummies(df)
'''
@alt(カテゴリデータ|質的データ|非数値データ)
df[|内のカテゴリデータ]をダミー変数[に変換|化]する
'''

pd.get_dummies(df[name])
'''
dfのnameカラムをダミー変数[化|に変換]する
'''

iterable=[1, 2, 1, 3]
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
@X(df[name]|ds)
@Y(dfのnameカラム|ds)
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

