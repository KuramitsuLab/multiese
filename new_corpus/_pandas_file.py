import numpy as np

import pandas as pd
'''
@alt(表データ|データフレーム)
@alt(カラム|列)
@alt(インデックス|行)
@alt(欠損値|NaN|未入力値)
@alt(変更する|増やす|減らす)
@alt(保存する|保存する|書き込む)
@alt(抽出する|取り出す)
@alt(読み込む|読む)
@alt(読み込んで|読んで)
@alt(全ての|すべての|全)
@alt(の名前|名)

@prefix(df;データフレーム)
@prefix(ds;[データ列|カラム])
@prefix(col;[列|カラム])
@prefix(value;[文字列|日付|値])

表データを使う
表データをインポートする
'''

import seaborn as sns

n = 1

filename = 'test.csv'
filename = 'file.csv'
filename = 'file.tsv'
filename = 'file.json'
filename = 'file.json'

col, col2, col3 = '列A', '列B', '列C'
df = pd.DataFrame(data=[[1, 2, 3], [4, 5, 6]], columns=['列A', '列B', '列C'])
df2 = df
ds, ds2 = df[col], df[col2]


# 設定

print(pd.__version__)
'''
Pandasのバージョンをプリントする
Pandasのバージョンを見る
'''

pd.set_option('display.max_columns', n)
'''
@alt(表示可能な|[表示できる|表示する|表示される])
[データフレームを表示するとき、|][表示可能な|][最大|]列数を変更する
[データフレームを表示するとき、|][表示可能な|]列数の最大値をnに設定する
[データフレームを表示するとき、|]{n列まで|データフレームを}表示可能なようにする
'''

pd.set_option('display.max_rows', n)
'''
[データフレームを表示するとき、|][表示可能な|][最大|]行数を変更する
[データフレームを表示するとき、|][表示可能な|][最大|]行数をnに設定する
[データフレームを表示するとき、|]{n行まで|データフレームを}表示できるようにする
'''

pd.set_option('precision', n)
'''
[データフレームを表示するとき、|]小数点以下の表示精度を設定する
[データフレームを表示するとき、|]小数点以下[の表示精度|]をn桁に設定する
[データフレームを表示するとき、|]小数点以下n桁まで表示可能なようにする
'''

pd.set_option('expand_frame_repr', False)
'''
[データフレームを表示するとき、|]折り返しをしない[|ようにする]
[データフレームを表示するとき、|]折り返しを[オフ|無効]に設定する
'''

pd.set_option('max_colwidth', n)
'''
[データフレームを表示するとき、|]カラムの最大幅をnに設定する
'''

pd.set_option('colheader_justify', 'right')
'''
[データフレームを表示するとき、|]ヘッダー行を右寄せに設定する
'''

pd.set_option('colheader_justify', 'left')
'''
[データフレームを表示するとき、|]ヘッダー行を左寄せに設定する
'''

# 読み込み系

pd.read_excel('file.xlsx')
'''
@prefix(filename;エクセルファイル)
@alt(エクセル|[エクセル|表計算|Excel][ファイル|])
@alt(読み込む|読む|ロードする)

{エクセルから|データフレームを}読み込む
{エクセルを|[データフレームとして|]}読み込む
'''

シート名 = 0

pd.read_excel('file.xlsx', sheet_name=シート名)
'''
{エクセルから|シート[の名前|]を指定して|[データフレームを|]}読み込む
{エクセルのシートを|[データフレームとして|]}読み込む
'''

pd.read_excel('file.xlsx', sheet_name=[0, 1])
'''
{エクセルから|複数のシートを[指定して|]|[データフレームとして|]}読み込む
{エクセルから|複数のシートを}読み込む
'''

pd.read_excel('file.xlsx', sheet_name=None)
'''
{エクセルから|全てのシートを}読み込む
'''

pd.read_csv('file.csv', sep=',')
'''
@alt(CSVファイル|CSV|カンマ区切りのファイル)

{CSVファイルから|データフレームを}読み込む
{CSVファイルを|[|データフレームとして]}読み込む
'''

pd.read_csv('file.tsv', sep='\t')
'''
@alt(TSVファイル|TSV|タブ区切りのファイル)

{TSVファイルから|データフレームを}読み込む
{TSVファイルを|[|データフレームとして]}読み込む
'''

sheet_name = ['A', 'B']
'''
option: [エクセル|]シートの名前を設定する
'''

index_col = 0
'''
option: [先頭の|最初の]カラムをインデックスに設定する
'''

index_col = n
'''
option: n番目のカラムをインデックスに設定する
'''

index_col = None
'''
option: インデックスを[自動的な|]連番に設定する
option: どのカラムもインデックスに[設定|]しない
'''

header = 0
'''
@alt(ヘッダ|カラムの名前)
option: [先頭の|最初の]行をヘッダに設定する
'''

header = None
'''
option: ヘッダを[自動的な|]連番に設定する
option: どの行もヘッダに[|設定]しない
'''

列名リスト = ['列A', '列B']

names = 列名リスト
'''
option: カラムの名前をリストで設定する
'''

usecols = names
'''
option: 読み込む行番号をnamesで指定する
'''

skiprows = names
'''
option: [読み込まない|スキップする|無視する]列番号をnamesで指定する
'''

skipfooter = n
'''
option: [読み込まない|スキップする|無視する]フッタをnに設定する
'''

pd.read_csv('file.csv', header=None)
'''
{CSVファイルを|[ヘッダ|カラム名][を指定せず|なしで]}読み込む
'''

pd.read_csv('file.csv', index_col=n)
'''
{CSVファイルのn行目を|インデックス[と|に]して}読み込む
{CSVファイルを|n番目のカラムをインデックス[と|に]して}読み込む
'''

pd.read_csv('file.csv', encoding='shift_jis')
'''
{filenameを|[SJISで|文字化けしないように]}読み込む
filenameから{CSVファイルを|[SJISで|文字化けしないように]}読み込む
'''

文字エンコーディング = 'utf-8'

pd.read_csv('file.tsv', sep='\t', encoding=文字エンコーディング)
'''
@alt(文字コード|文字エンコーディング)

{TSVファイルから|文字コードを指定して}[データフレームを|]読み込む
'''

pd.read_json(filename, orient='records', lines=True)
'''
@prefix(filename;JSONLファイル)

{JSONL[形式の|]ファイルから|データフレームを}読み込む
{filenameから|データフレームを}読み込む
{filenameを|[|データフレームとして]}読み込む
'''


#

# write

df.to_excel('file.xlsx')
'''
@alt(エクセルファイル|エクセル形式)
@alt(保存する|出力する|書き出す)

{dfを|エクセルファイルで}保存する
'''


df.to_csv('file.csv')
'''
@alt(CSVファイル|[CSV|カンマ区切り]形式)

dfを保存する
{dfを|CSVファイルで_}保存する
'''

df.to_csv('file.tsv', sep='\t')
'''
@alt(TSVファイル|[CSV|タブ区切り]形式)

{dfを|TSVファイルで_}保存する
'''

df.to_csv('file.csv', header=None)
'''
@alt(ヘッダを付けず|[ヘッダ|カラム名]なしで)

{dfを|[CSVファイルに|]|ヘッダを付けず}保存する
'''

df.to_csv('file.csv', index=None)
'''
@alt(インデックスを付けず|インデックスなしで)
{dfを|[CSVファイルに|]|インデックスを付けず}保存する
'''

df.to_csv('file.csv', encoding='utf_8_sig')
'''
@alt(BOM付きで|BOMを付けて|[Windowsで|]文字化けしないように)
{dfを|[CSVファイルに|]|BOM付きで}保存する
'''

df.to_csv('file.csv', encoding='shift_jis')
'''
@test(df=missing;filename='file.txt';$$)
{dfを|[CSVファイルに|]|SJISで}保存する
'''

df.to_csv('file.csv', float_format='%.3f')
'''
保存するCSVファイルの小数点以下の桁数を設定する
{dfを|[CSVファイルに|]|小数点以下3桁まで}保存する
'''
