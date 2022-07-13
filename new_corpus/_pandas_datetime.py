import pandas as pd
'''
@test($$;type(pd))
@alt(全ての|すべての|全)
@alt(の名前|名)
@alt(見る|知る|調べる)

@alt(日付データ|タイムスタンプ[型|]|Pandasの日付型|datetime64型)
@prefix(value;[文字列|日付|])
'''

dateList = [pd.to_datetime('12-12-12'), pd.to_datetime('12-12-12')]
df = pd.DataFrame(data={'列A': dateList, '列B': [1, 2]})
col = '列A'
ds = df[col]

日付を表現した文字列 = '11-01-01'


pd.to_datetime(日付を表現した文字列)
'''
[日付を表現した|]文字列を日付データに変換する
'''

__X__ = df['列A']
'''
@X(df['列A'];ds)
@Y([列|カラム];データ列)
'''

pd.to_datetime(__X__)
'''
__Y__を[全て|]日付データに変換する
'''

pd.to_datetime(__X__, format='%Y-%m-%d')
'''
@alt(フォーマット|書式)

{フォーマットで_|__Y__を}日付データに変換する
'''

# エポック秒

pd.to_datetime(__X__, unit='s', utc=True)
'''
@alt(エポック秒|UNIX秒|UNIX時間|数値時刻)

エポック秒の__Y__から日付データに変換する
__Y__のエポック秒を日付データに変換する
'''

__X__ = df['列A']
'''
@X(df['列A'];ds)
@Y(dfのあるカラム;データシリーズ)
'''

__X__.tz_convert('Asia/Tokyo')
'''
__Y__のタイムゾーンを[日本|東京]に設定する
__Y__のタイムゾーンを設定する
'''

df.set_index('列A', inplace=True)
'''
dfのあるカラムをインデックスにする
'''

df.index = pd.DatetimeIndex(__X__)
'''
日付データの__Y__を[dfの|]インデックスにする
'''

df.index = pd.DatetimeIndex(pd.to_datetime(__X__))
'''
__Y__を[dfの|]日付インデックスにする
__Y__を日付データに変換し、[dfの|]インデックスにする
'''

__X__.dt.year
'''
__Y__の年[|度][|を得る]
__Y__[が|は]何年か見る
'''

__X__.dt.month
'''
__Y__の月[|を得る]
__Y__[が|は]何月か見る
'''

__X__.dt.day
'''
__Y__の[日|日にち][|を得る]
__Y__[が|は]何日か見る
'''

__X__.dt.hour
'''
__Y__の[時|時刻][|を得る]
__Y__[が|は]何時か見る
'''

__X__.dt.minute
'''
__Y__の分[|を得る]
__Y__[が|は]何分か見る
'''

__X__.dt.second
'''
__Y__の秒[|を得る]
__Y__[が|は]何秒か見る
'''

__X__.dt.weekday_name
'''
__Y__の曜日[の名前|][|を得る]
__Y__[が|は]何曜日か見る
'''

__X__.dt.dayofweek
'''
__Y__の曜日数[|を得る]
__Y__の曜日[が|は]何日目か見る
'''
