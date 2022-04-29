import numpy as np

import pandas as pd
'''
@test($$;type(pd))
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
@prefix(ds;データ列;カラム)
@prefix(col;カラム;カラム)
@prefix(value;[文字列|日付|])
表データを使う
表データをインポートする
'''

import seaborn as sns

n = 1

excelfile = 'test.csv'
csvfile = 'file.csv'
tsvfile = 'file.tsv'
jsonfile = 'file.json'
jsonlfile = 'file.json'

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
@test(pd=missing;$$)
@alt(表示可能な|[表示できる|表示する|表示される])
[データフレームを表示するとき、][表示可能な|][最大|]列数を変更する
[データフレームを表示するとき、][表示可能な|]列数の最大値をnに設定する
[データフレームを表示するとき、]{n列まで|データフレームを}表示可能なようにする
'''

pd.set_option('display.max_rows', n)
'''
@test(pd=missing;$$)
[データフレームを表示するとき、|][表示可能な|][最大|]行数を変更する
[データフレームを表示するとき、|][表示可能な|][最大|]行数をnに設定する
[データフレームを表示するとき、|]{n行まで|データフレームを}表示できるようにする
'''

pd.set_option('precision', n)
'''
@test(pd=missing;$$)
[データフレームを表示するとき、|]小数点以下の表示精度を設定する
[データフレームを表示するとき、|]小数点以下[の表示精度|]をn桁に設定する
[データフレームを表示するとき、|]小数点以下n桁まで表示可能なようにする
'''

pd.set_option('expand_frame_repr', False)
'''
@test(pd=missing;$$)
[データフレームを表示するとき、|]折り返しをしない[|ようにする]
[データフレームを表示するとき、|]折り返しを[オフ|無効]に設定する
'''

pd.set_option('max_colwidth', n)
'''
@test(pd=missing;$$)
[データフレームを表示するとき、|]カラムの最大幅をnに設定する
'''

pd.set_option('colheader_justify', 'right')
'''
@test(pd=missing;$$)
[データフレームを表示するとき、|]ヘッダー行を右寄せに設定する
'''

pd.set_option('colheader_justify', 'left')
'''
@test(pd=missing;$$)
[データフレームを表示するとき、|]ヘッダー行を左寄せに設定する
'''

# 読み込み系

excelfile = 'file.xlsx'
pd.read_excel(excelfile)
'''
@test(pd=missing;excelfile='file.xlsx';$$)
@prefix(excelfile;エクセルファイル)
@alt(エクセル|エクセル[ファイル|データ])
[|Pandasで_]{エクセルから|データフレームを}読み込む
[|Pandasで_]{excelfileを|[データフレームとして|]}読み込む
[|Pandasで_]{excelfileからエクセルを読み込む
'''

pd.read_excel(excelfile, sheet_name=n)
'''
@test(pd=missing;excelfile='file.xlsx';$$)
[|Pandasで_]{excelfileから|n番目のシートを}[データフレームとして|]読み込む
[|Pandasで_]{excelfileから|nという[名前の|]シートを}[データフレームとして|]読み込む
[|Pandasで_]{excelfileの|n番目のシートを}[データフレームとして|]読み込む
'''

pd.read_excel(excelfile, sheet_name=[n, n2])
'''
@test(pd=missing;excelfile='file.xlsx';$$)
[|Pandasで_]{excelfileから|複数のシートを}読み込む
[|Pandasで_]{excelfileから|nとn2のシートを}読み込む
'''

pd.read_excel(excelfile, sheet_name=None)
'''
@test(pd=missing;excelfile='file.xlsx';$$)
[|Pandasで_]{excelfileから|全てのシートを}読み込む
'''

pd.read_csv(csvfile, sep=',')
'''
@test(pd=missing;csvfile='file.csv';$$)
@prefix(csvfile;CSVファイル)
@alt(CSVファイル|CSV|カンマ区切りのファイル)
[|Pandasで_]{CSVファイルから|データフレームを}読み込む
[|Pandasで_]{csvfileから|データフレームを}読み込む
[|Pandasで_]{csvfileを|[|データフレームとして]}読み込む
'''

pd.read_csv(tsvfile, sep='\t')
'''
@test(pd=missing;tsvfile='file.tsv';$$)
@prefix(tsvfile;TSVファイル)
@alt(TSVファイル|TSV|タブ区切りのファイル)
[|Pandasで_]{TSVファイルから|データフレームを}読み込む
[|Pandasで_]{tsvfileから|データフレームを}読み込む
[|Pandasで_]{tsvfileを|[|データフレームとして]}読み込む
'''

sheet_name = alist
'''
@test($$;sheet_name)
オプションで、[読み込む|エクセルの|]シートの名前をalistに設定する
'''

index_col = 0
'''
@test($$;index_col)
@alt(の_|)
オプションで、[先頭の_|最初の]カラムをインデックスに設定する
'''

index_col = n
'''
@test($$;index_col)
オプションで、n番目のカラムをインデックスに設定する
'''

index_col = None
'''
@test($$;index_col)
オプションで、インデックスを[自動的な|]連番に設定する
オプションで、どのカラムもインデックスに[設定|]しない
'''

header = 0
'''
@test($$;header)
@alt(ヘッダ|カラムの名前)
オプションで、[先頭の|最初の]行をヘッダに設定する
'''

header = None
'''
@test($$;header)
オプションで、ヘッダを[自動的な|]連番に設定する
オプションで、どの行もヘッダに[|設定]しない
'''

header = alist
'''
@test($$;header)
オプションで、ヘッダをalistに設定する
'''

names = alist
'''
@test($$;names)
オプションで、alistをカラムの名前に設定する
'''

usecols = alist
'''
@test($$;usecols)
オプションで、読み込む行番号をalistで指定する
'''

skiprows = alist
'''
@test($$;skiprows)
オプションで、[読み込まない|スキップする|無視する]列番号をalistで指定する
'''

skipfooter = n
'''
@test($$;skipfooter)
オプションで、[読み込まない|スキップする|無視する]フッタをnに設定する
'''

pd.read_csv(csvfile, header=None)
'''
@test(pd=missing;csvfile='file.csv';$$)
[|Pandasで_]{csvfileを|ヘッダ[を指定せず|なしで]}読み込む
'''

pd.read_csv(csvfile, index_col=n)
'''
@test(pd=missing;csvfile='file.csv';$$)
[|Pandasで_]{CSVファイルcsvfileを|n番目のカラムをインデックス[と|に]して}読み込む
[|Pandasで_]文字列csvfileから{CSVファイルを|n番目のカラムをインデックス[と|に]して}読み込む
'''

pd.read_csv(csvfile, encoding='shift_jis')
'''
@test(pd=missing;csvfile='file.csv';$$)
[|Pandasで_]{csvfileを|[SJISで|文字化けしないように]}読み込む
[|Pandasで_]csvfileから{CSVファイルを|[SJISで|文字化けしないように]}読み込む
'''

__X__ = 'utf-8'
pd.read_csv(tsvfile, sep='\t', encoding=__X__)
'''
@test(pd=missing;tsvfile='file.tsv';$$)
@X('utf-8';'shift_jis')
@Y('UTF8';シフトJIS)
[|Pandasで_]{TSV[形式の|]ファイルから|データフレームを}読み込む
[|Pandasで_]{tsvfileから|データフレームを}読み込む
[|Pandasで_]{tsvfileを|[|データフレームとして]}読み込む
'''

pd.read_json(jsonlfile, orient='records', lines=True)
'''
@test(pd=missing;jsonlfile='file.jsonl';$$)
@prefix(jsonlfile;JSONLファイル)
[|Pandasで_]{JSONL[形式の|]ファイルから|データフレームを}読み込む
[|Pandasで_]{jsonlfileから|データフレームを}読み込む
[|Pandasで_]{jsonlfileを|[|データフレームとして]}読み込む
'''


#

# write

df.to_excel(excelfile)
'''
@test(df=missing;excelfile='file.xsl';$$)
@alt(ファイル名|名前)
{dfを|excelfileに}保存する
{dfを|エクセル[ファイル|形式|]で_|excelfileに}保存する
'''

df.to_csv(csvfile)
'''
@test(df=missing;csvfile='file.txt';$$)
{dfを|csvfileに}保存する
{dfを|CSV[ファイル|形式|]で_|csvfileに}保存する
'''

df.to_csv(tsvfile, sep='\t')
'''
@test(df=missing;tsvfile='file.tsv';$$)
{dfを|tsvfileに}保存する
{dfを|タブ区切りで_|tsvfileに}保存する
{dfを|TSV[ファイル|形式|]で_|csvfileに}保存する
'''

df.to_csv(csvfile, header=None)
'''
@test(df=missing;csvfile='file.txt';$$)
@alt(ヘッダを付けずに|ヘッダなしで)
{dfを|csvfileに|ヘッダを付けずに}保存する
'''

df.to_csv(csvfile, index=None)
'''
@test(df=missing;csvfile='file.txt';$$)
@alt(インデックスを付けずに|インデックスなしで)
{dfを|csvfileに|インデックスを付けずに}保存する
'''

df.to_csv(csvfile, encoding='utf_8_sig')
'''
@test(df=missing;csvfile='file.txt';$$)
@alt(BOM付きで|BOMを付けて|[Windowsで|]文字化けしないように)
{dfを|csvfileに|BOM付きで}保存する
'''

df.to_csv(csvfile, encoding='shift_jis')
'''
@test(df=missing;csvfile='file.txt';$$)
{dfを|csvfileに|SJISで}保存する
'''

df.to_csv(csvfile, float_format='%.3f')
'''
@test(pd=missing;csvfile='file.txt';$$)
保存するCSVファイルの小数点以下の桁数を設定する
{dfを|csvfileに|小数点以下3桁まで}保存する
'''
