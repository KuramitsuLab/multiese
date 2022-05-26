import numpy as np

import pandas as pd
'''
@test($$;type(pd))
@alt(表データ|データフレーム)
@alt(カラム|列)
@alt(インデックス|行)
@alt(どの程度|どれだけ)
@alt(欠損値|NaN|未入力値)
@alt(変更する|増やす|減らす)
@alt(保存する|保存する|書き込む)
@alt(抽出する|取り出す)
@alt(読み込む|読む)
@alt(読み込んで|読んで)
@alt(全ての|すべての|全)
@alt(の名前|名)
@alt(丸める|四捨五入する)
@alt(丸めて|四捨五入して)
@alt(含まれる|ある|存在する|含まれる)
@alt(含まれない|ない|存在しない|含まれない)
@prefix(df;データフレーム)
@prefix(ds;データ列;カラム)
@prefix(col;カラム;カラム)
@prefix(value;[文字列|日付|])
データ列を使う
データ列をインポートする
'''

df = pd.DataFrame(data={'A': [1, 2, 3], 'B': [2, 1, 0]})
ds = df['A']
col = 'A'


__X__ = df

__X__.describe()
'''
@test(df=ds=missing;aList=['A','B'];$$)
@X(df|df[aList]|ds|df[col])
@Y(df|dfのaListカラム|ds|dfのcol)
@alt(要約統計量|[記述統計量|基本統計量|代表値])
__Y__の要約統計量[|を求める]
'''

__X__.mean()
'''
@test(df=ds=missing;aList=['A','B'];$$)
@alt(平均値|平均)
__Y__の平均値[|を求める]
'''

__X__.median()
'''
@test(df=ds=missing;aList=['A','B'];$$)
@alt(中央値|メディアン|第二四分位数|50パーセンタイル)
__Y__の中央値[|を求める]
'''

__X__.quantile(0.25)
'''
@test(df=ds=missing;aList=['A','B'];$$)
@alt(第一四分位数|25パーセンタイル|上位25%)
__Y__の第一四分位数[|を求める]
'''

__X__.quantile(0.75)
'''
@test(df=ds=missing;aList=['A','B'];$$)
@alt(第三四分位数|75パーセンタイル|下位25%)
__Y__の第三四分位数
'''

percent = 50

__X__.quantile(percent/100)
'''
@test(df=ds=missing;aList=['A','B'];$$)
__Y__のpercent[分位数|パーセンタイル][|を求める]
'''

__X__.mode()
'''
@test(df=ds=missing;aList=['A','B'];$$)
@alt(最頻値|モード)
__Y__の最頻値[|を求める]
__Y__のどの値が[頻出|最も現れる]か見る
'''

__X__.std()
'''
@test(df=ds=missing;aList=['A','B'];$$)
@alt(標本標準偏差|標準偏差)
__Y__の標本標準偏差[|を求める]
'''

__X__.std(ddof=0)
'''
@test(df=ds=missing;aList=['A','B'];$$)
__Y__の母標準偏差[|を求める]
'''

__X__.var()
'''
@test(df=ds=missing;aList=['A','B'];$$)
__Y__の分散[|を求める]
__Y__[が|は]どの程度、分散しているか見る
'''

__X__.kurt()
'''
@test(df=ds=missing;aList=['A','B'];$$)
__Y__の[歪度|正規分布に対する左右対称性][|を求める]
__Y__[が|は]正規分布からどの程度、歪んでいるか見る
'''

__X__.skew()
'''
@test(df=ds=missing;aList=['A','B'];$$)
__Y__の[尖度|正規分布に対する上下広がり][|を求める]
__Y__[が|は]正規分布からどの程度、尖っているか見る
'''

# ds の操作
# @X(ds;df[col])
# @Y(ds;dfのcol)

__X__.round()
'''
@test(df=ds=missing;aList=['A','B'];$$)
__Y__を[|整数に]丸める
'''

n = 2
__X__.round(n)
'''
@test(df=ds=missing;aList=['A','B'];$$)
__Y__を小数点以下n桁で丸める
'''

__X__.round(-1)
'''
@test(df=ds=missing;aList=['A','B'];$$)
__Y__を[10|十]の位で丸める
'''

__X__.round(-2)
'''
@test(df=ds=missing;aList=['A','B'];$$)
__Y__を[100|百]の位で丸める
'''

__X__.round(-3)
'''
@test(df=ds=missing;aList=['A','B'];$$)
__Y__を[1000|千]の位で丸める
'''

__X__.round().astype(int)
'''
@test(df=ds=missing;aList=['A','B'];$$)
@alt(整数型|整数)
__Y__を丸めて、整数型にする
'''

__X__.round(-1).astype(int)
'''
@test(df=ds=missing;aList=['A','B'];$$)
__Y__を[10|十]の位で丸めて、整数型にする
'''

__X__.round(-2).astype(int)
'''
@test(df=ds=missing;aList=['A','B'];$$)
__Y__を[100|百]の位で丸めて、整数型にする
'''

__X__.round(-3).astype(int)
'''
@test(df=ds=missing;aList=['A','B'];$$)
__Y__を[1000|千]の位で丸めて、整数型にする
'''

x = 0.0

__X__.fillna(x)
'''
@test(df=ds=missing;aList=['A','B'];$$)
@alt(埋める|補う|[置換する|置き換える])
{__Y__の欠損値を|xで}埋める
__Y__の欠損値をxに設定する
'''

__X__.fillna(__X__.mean())
'''
@test(df=ds=missing;aList=['A','B'];$$)
{__Y__の欠損値を|平均値で}埋める
__Y__の欠損値を平均値に設定する
'''

__X__.fillna(__X__.mode().iloc[0])
'''
@test(df=ds=missing;aList=['A','B'];$$)
{__Y__の欠損値を|最頻値で}埋める
__Y__の欠損値を最頻値に設定する
'''

__X__.fillna(__X__.median())
'''
@test(df=ds=missing;aList=['A','B'];$$)
{__Y__の欠損値を|中央値で}埋める
__Y__の欠損値を中央値に設定する
'''

__X__.fillna(__X__.max())
'''
@test(df=ds=missing;aList=['A','B'];$$)
{__Y__の欠損値を|最大値で}埋める
__Y__の欠損値を最大値に設定する
'''

__X__.fillna(__X__.min())
'''
@test(df=ds=missing;aList=['A','B'];$$)
{__Y__の欠損値を|最小値で}埋める
__Y__の欠損値を最小値に設定する
'''

__X__.fillna(method='ffill')
'''
@test(df=ds=missing;aList=['A','B'];$$)
@alt(直前の値|前の[行の|]値)
{__Y__の欠損値を|直前の値で}埋める
__Y__の欠損値を直前の値に設定する
'''

__X__.fillna(method='bfill')
'''
@test(df=ds=missing;aList=['A','B'];$$)
@alt(直後の値|後の[行の|]値)
{__Y__の欠損値を|直後の値で}埋める
__Y__の欠損値を直後の値に設定する
'''

s = ''

__X__.replace(s, np.nan)
'''
@test(df=ds=missing;aList=['A','B'];$$)
__Y__のsを欠損値に変換する
__Y__のsを欠損値に変換する
'''

__X__.replace('', np.nan).dropna()
'''
@test(df=ds=missing;aList=['A','B'];$$)
__Y__ の空文字を欠損値に変換し、ドロップする
__Y__ の空文字をドロップする
'''

ValueMap = {1: 2, 2: 1}

__X__.replace(ValueMap)
'''
@test(df=ds=missing;aList=['A','B'];$$)
@alt(置き換える|置換する|変更する)
{__Y__[の値|]を|ValueMapで|まとめて}置き換える
'''

pattern = '.*'
repl = '\\1'

__X__.replace(pattern, repl, regex=True)
'''
@test(df=ds=missing;pattern='.*';repl='\1';aList=['A','B'];$$)
@alt(置き換える|置換する|変更する)
{__Y__[の値|]を|正規表現[pattern|]で|まとめて|[replに|]}置き換える
'''

# null判定

__X__.isna()
'''
@test(df=ds=missing;value=1;$$)
__Y__の値[が|は]欠損値かどうか
'''

__X__.isna().sum()
'''
@test(df=ds=missing;value=1;$$)
@alt(合計|[|個]数)
@alt(数える|カウントする|求める)
__Y__の中の欠損値の合計を数える
__Y__の中にいくつ欠損値が含まれるか数える
'''

value, value2 = 1, 2

__X__.isin([value])
'''
@test(df=ds=missing;value=1;$$)
@prefix(value;[文字列|日付データ|])
__Y__の中にvalueが含まれるかどうか
'''

__X__.isin([value]).sum()
'''
@test(df=ds=missing;value=1;$$)
__Y__の中に含まれるvalueの合計を数える
__Y__の中にいくつvalueが含まれるか数える
'''

__X__.isin([value, value2])
'''
@test(df=ds=missing;value=value2=1;$$)
__Y__の中にvalueとvalue2が含まれるかどうか
'''

__X__.isin([value, value2]).sum()
'''
@test(df=ds=missing;value=value2=1;$$)
__Y__の中に含まれるvalueとvalue2の合計を数える
__Y__の中にvalueとvalue2がいくつ含まれるか数える
'''
