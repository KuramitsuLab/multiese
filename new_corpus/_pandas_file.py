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

col, col2, col3 = 'A', 'B', 'C'
df = pd.DataFrame(data=[[1, 2, 3], [4, 5, 6]], columns=['A', 'B', 'C'])
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

filename = 'file.xlsx'
pd.read_excel(filename)
'''
@prefix(filename;エクセルファイル)
@alt(エクセル|エクセル[ファイル|データ])

{エクセルから|データフレームを}読み込む
{|filenameを|[データフレームとして|]}読み込む
{|filenameから|エクセルを}読み込む
'''

pd.read_excel(filename, sheet_name=n)
'''
@test(pd=missing;filename='file.xlsx';$$)
{filenameから|n番目のシートを}[データフレームとして|]読み込む
{filenameから|nという[名前の|]シートを}[データフレームとして|]読み込む
{filenameの|n番目のシートを}[データフレームとして|]読み込む
'''

pd.read_excel(filename, sheet_name=[n, n2])
'''
@test(pd=missing;filename='file.xlsx';$$)
{filenameから|複数のシートを}読み込む
{filenameから|nとn2のシートを}読み込む
'''

pd.read_excel(filename, sheet_name=None)
'''
@test(pd=missing;filename='file.xlsx';$$)
{filenameから|全てのシートを}読み込む
'''

pd.read_csv(filename, sep=',')
'''
@test(pd=missing;filename='file.csv';$$)
@prefix(filename;CSVファイル)
@alt(CSVファイル|CSV|カンマ区切りのファイル)
{CSVファイルから|データフレームを}読み込む
{filenameから|データフレームを}読み込む
{filenameを|[|データフレームとして]}読み込む
'''

pd.read_csv(filename, sep='\t')
'''
@test(pd=missing;filename='file.tsv';$$)
@prefix(filename;TSVファイル)
@alt(TSVファイル|TSV|タブ区切りのファイル)
{TSVファイルから|データフレームを}読み込む
{filenameから|データフレームを}読み込む
{filenameを|[|データフレームとして]}読み込む
'''

names = ['A', 'B']
sheet_name = names
'''
@test($$;sheet_name)
option: [読み込む|エクセルの|]シートの名前をnamesに設定する
'''

index_col = 0
'''
@test($$;index_col)
@alt(の_|)
option: [先頭の_|最初の]カラムをインデックスに設定する
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
@test($$;header)
option: ヘッダを[自動的な|]連番に設定する
option: どの行もヘッダに[|設定]しない
'''

header = names
'''
@test($$;header)
option: ヘッダをnamesに設定する
'''

names = names
'''
@test($$;names)
option: namesをカラムの名前に設定する
'''

usecols = names
'''
@test($$;usecols)
option: 読み込む行番号をnamesで指定する
'''

skiprows = names
'''
@test($$;skiprows)
option: [読み込まない|スキップする|無視する]列番号をnamesで指定する
'''

skipfooter = n
'''
@test($$;skipfooter)
option: [読み込まない|スキップする|無視する]フッタをnに設定する
'''

pd.read_csv(filename, header=None)
'''
@test(pd=missing;filename='file.csv';$$)
{filenameを|ヘッダ[を指定せず|なしで]}読み込む
'''

pd.read_csv(filename, index_col=n)
'''
@test(pd=missing;filename='file.csv';$$)
{CSVファイルfilenameを|n番目のカラムをインデックス[と|に]して}読み込む
文字列filenameから{CSVファイルを|n番目のカラムをインデックス[と|に]して}読み込む
'''

pd.read_csv(filename, encoding='shift_jis')
'''
@test(pd=missing;filename='file.csv';$$)
{filenameを|[SJISで|文字化けしないように]}読み込む
filenameから{CSVファイルを|[SJISで|文字化けしないように]}読み込む
'''

__X__ = 'utf-8'
pd.read_csv(filename, sep='\t', encoding=__X__)
'''
@test(pd=missing;filename='file.tsv';$$)
@X('utf-8';'shift_jis')
@Y('UTF8';シフトJIS)

{TSV[形式の|]ファイルから|データフレームを}読み込む
{filenameから|データフレームを}読み込む
{filenameを|[|データフレームとして]}読み込む
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

df.to_excel(filename)
'''
@alt(ファイル名|名前)

{dfを|filenameに}保存する
{dfを|エクセル[ファイル|形式|]で_|filenameに}保存する
'''

df.to_csv(filename)
'''
{dfを|filenameに}保存する
{dfを|CSV[ファイル|形式|]で_|filenameに}保存する
'''

df.to_csv(filename, sep='\t')
'''
{dfを|filenameに}保存する
{dfを|タブ区切りで_|filenameに}保存する
{dfを|TSV[ファイル|形式|]で_|filenameに}保存する
'''

df.to_csv(filename, header=None)
'''
@alt(ヘッダを付けずに|ヘッダなしで)
{dfを|filenameに|ヘッダを付けずに}保存する
'''

df.to_csv(filename, index=None)
'''
@alt(インデックスを付けずに|インデックスなしで)
{dfを|filenameに|インデックスを付けずに}保存する
'''

df.to_csv(filename, encoding='utf_8_sig')
'''
@test(df=missing;filename='file.txt';$$)
@alt(BOM付きで|BOMを付けて|[Windowsで|]文字化けしないように)
{dfを|filenameに|BOM付きで}保存する
'''

df.to_csv(filename, encoding='shift_jis')
'''
@test(df=missing;filename='file.txt';$$)
{dfを|filenameに|SJISで}保存する
'''

df.to_csv(filename, float_format='%.3f')
'''
@test(pd=missing;filename='file.txt';$$)
保存するCSVファイルの小数点以下の桁数を設定する
{dfを|filenameに|小数点以下3桁まで}保存する
'''
