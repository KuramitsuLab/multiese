import pandas as pd
'''
@test($$;type(pd))
@alt(全ての|すべての|全)
@alt(の名前|名)
@alt(丸める|四捨五入する)
@alt(丸めて|四捨五入して)
@prefix(df;データフレーム)
@prefix(ds;データ列)
@prefix(col;カラム;カラム)
@alt(日付データ|タイムスタンプ[型|]|Pandasの日付型|datetime64型)
@prefix(value;[文字列|日付|])
データ列を使う
データ列をインポートする
'''

pd.to_datetime(x)
'''
@test(pd=df=ds=missing;$$)
[Pandasで、|]xを日付データに変換する
'''

__X__ = df['A']
pd.to_datetime(__X__)
'''
@test(pd=df=ds=missing;$$)
@X(df[col];ds;s)
@Y(dfのcoll;ds;s)
[Pandasで、|]__Y__を日付データに変換する
'''

pd.to_datetime(__X__, format='%Y-%m-%d')
'''
@test(pd=df=ds=missing;$$)
@alt(フォーマット|書式)
[Pandasで、|]{フォーマットで_|__Y__を}日付データに変換する
'''

pd.to_datetime(__X__, format=fmt)
'''
@test(pd=df=ds=missing;fmt='%Y';$$)
[Pandasで、|]{フォーマットfmtで_|__Y__を}日付データに変換する
'''

# エポック秒

pd.to_datetime(__X__, unit='s', utc=True)
'''
@test(pd=df=ds=missing;$$)
@alt(エポック秒|UNIX秒|UNIX時間|数値時刻)
[Pandasで、|]エポック秒の__Y__から日付データに変換する
[Pandasで、|]__Y__のエポック秒から日付データに変換する
'''

__X__.tz_convert('Asia/Tokyo')
'''
@X(df[col]|ds)
@Y(dfのcol|ds)
@test(pd=df=ds=missing;$$)
__Y__のタイムゾーンを[日本|東京]に設定する
'''

__X__.tz_convert(s)
'''
@test(pd=df=ds=missing;$$)
__Y__のタイムゾーンをsに設定する
'''

df.set_index(col, inplace=True)
'''
@test(pd=df=ds=missing;$$)
[Pandasで、|]dfのcolをインデックスにする
'''

df.index = pd.DatetimeIndex(__X__)
'''
@test(pd=df=ds=missing;$$;df.index)
[Pandasで、|]日付データの__Y__を[dfの|]インデックスにする
'''

df.index = pd.DatetimeIndex(pd.to_datetime(__X__))
'''
@test(pd=df=ds=missing;$$;df.index)
[Pandasで、|]__Y__を日付データに変換し、[dfの|]インデックスにする
'''

__X__.dt.year
'''
@test(pd=df=ds=missing;$$)
__Y__の年[|を得る]
__Y__が_何年か見る
'''

__X__.dt.month
'''
@test(pd=df=ds=missing;$$)
__Y__の月[|を得る]
__Y__が_何月か見る
'''

__X__.dt.day
'''
@test(pd=df=ds=missing;$$)
__Y__の[日|日にち][|を得る]
__Y__が_何日か見る
'''

__X__.dt.hour
'''
@test(pd=df=ds=missing;$$)
__Y__の[時|時刻][|を得る]
__Y__が_何時か見る
'''

__X__.dt.minute
'''
@test(pd=df=ds=missing;$$)
__Y__の分[|を得る]
__Y__が_何分か見る
'''

__X__.dt.second
'''
@test(pd=df=ds=missing;$$)
__Y__の秒[|を得る]
__Y__が_何秒か見る
'''

__X__.dt.weekday_name
'''
@test(pd=df=ds=missing;$$)
__Y__の曜日[の名前|][|を得る]
__Y__が_何曜日か見る
'''

__X__.dt.dayofweek
'''
@test(pd=df=ds=missing;$$)
__Y__の曜日数[|を得る]
__Y__の曜日が_何日目か見る
'''
