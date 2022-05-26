from importlib import import_module

import datetime
'''
[日付|時刻]を[使う|インポートする]
'''

import time
'''
@alt(タイムスタンプ|エポック[秒|タイム|]|UNIX[時間|時刻|タイム])

[時間|タイムスタンプ]を[使う|インポートする]
'''

datetime = import_module('datetime')
time = import_module('time')

year = 2022
month = 12
day = 24
hour = 23
minute = 59
second = 59

datetime.datetime.now()
'''
@alt(本日|今日|現在)
@alt(時刻|時間)
@alt(日時=[日付時刻|タイムスタンプ])
@prefix(aDatetime;日時データ)
@prefix(aDate;日付データ)
@prefix(timestamp;エポック秒)

本日の日時[|を求める]
'''

year = 2022
month = 12
day = 24

datetime.datetime(year=year, month=1, day=1)
'''
year年の日時[|をオブジェクト化する]
year年を日時に変換する
'''

datetime.datetime(year=year, month=month, day=1)
'''
year年day月の日時[|をオブジェクト化する]
year年day月を日時に変換する
'''

datetime.datetime(year=year, month=month, day=day)
'''
year年month月day日の日時[|をオブジェクト化する]
year年month月day日を日時に変換する
'''

datetime.datetime(year=year, month=month, day=day, hour=hour)
'''
year年month月day日hour時の日時[|をオブジェクト化する]
year年month月day日hour時を日時に変換する
'''

datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute)
'''
year年month月day日hour時minute分の日時[|をオブジェクト化する]
year年month月day日hour時minute分を日時に変換する
'''

datetime.datetime(year=year, month=month, day=day,
                  hour=hour, minute=minute, second=second)
'''
year年month月day日hour時minute分second秒の日時[|をオブジェクト化する]
year年month月day日hour時minute分second秒を日時に変換する
'''

年 = 2022
月 = 12
日 = 24
時 = 0
分 = 0
秒 = 0

datetime.datetime(年, 月, 日, 時, 分, 秒)
'''
[datetime|日時]をインスタンス化する
[年月日|日付]と[時刻|時間]から日時[|を作る]
'''


timestamp = 0

datetime.datetime.fromtimestamp(timestamp)
'''
timestamp[を|から]日時に変換する
'''

日付の書かれた文字列 = '2011-11-04'

datetime.datetime.fromisoformat(日付の書かれた文字列)
'''
@alt(ISO書式|ISO8601[|形式])
[ISO書式の|]文字列[を|から]日時に変換する
文字列[を|から][ISO書式で_|]日時に変換する
'''

dateString = '21/11/06 16:30'
format = '%d/%m/%y %H:%M'

datetime.datetime.strptime(日付の書かれた文字列, format)
'''
{文字列から|formatのパターンで_}日時に変換する
formatパターンの文字列を日時に変換する
'''

datetime.datetime.today()
'''
本日の[|ローカルな]日時[|を得る]
'''

aDatetime = datetime.datetime.fromisoformat('2022-12-24')
aDate = datetime.date.fromisoformat('2022-12-24')

aDatetime.timestamp()
'''
aDatetimeをエポック秒に変換する
aDatetimeを[浮動小数点数|数値]に変換する
'''

aDatetime.timetz()
'''
aDatetimeのタイムゾーン[|を得る]
'''

aDatetime.date()
'''
aDatetimeの日付[|を得る]
'''

aDatetime.time()
'''
aDatetimeの時刻[|を得る]
'''


# 日付

datetime.date(year=year, month=1, day=1)
'''
year年の日付[|をオブジェクト化する]
year年を日付に変換する
'''

datetime.date(year=year, month=month, day=1)
'''
year年month月の日付[|をオブジェクト化する]
year年month月を日付に変換する
'''

datetime.date(year=year, month=month, day=day)
'''
year年month月day日の日付[|をオブジェクト化する]
year年month月day日を日付に変換する
'''

datetime.date.today()
'''
本日の[|ローカルな]日付[|を得る]
'''

datetime.date.today() + datetime.timedelta(days=1)
'''
明日の日付[|を得る]
'''

datetime.date.today() - datetime.timedelta(days=1)
'''
昨日の日付[|を得る]
'''

__X__, __X__2 = aDatetime, aDatetime

__X__.year
'''
@X(aDatetime;aDate;datetime.datetime.today())
@Y(aDatetime;aDate;本日)
@alt(年数|年)
__Y__の年数[|を得る]
__Y__[が|は]何年か知る
'''

__X__.month
'''
@alt(月数|月)
__Y__の月数[|を得る]
__Y__[が|は]何月か知る
'''

__X__.day
'''
@alt(日数|日)
__Y__の日数[|を得る]
__Y__[が|は]何日か知る
'''

__X__.weekday()
'''
__Y__の曜日を[整数で|]得る
__Y__[が|は]何曜日か知る
'''

__X__.weekday() == 0
'''
__Y__が月曜日かどうか
'''

__X__.weekday() == 1
'''
__Y__が火曜日かどうか
'''

__X__.weekday() == 2
'''
__Y__が水曜日かどうか
'''

__X__.weekday() == 3
'''
__Y__が木曜日かどうか
'''

__X__.weekday() == 4
'''
__Y__が金曜日かどうか
'''

__X__.weekday() == 5
'''
__Y__が土曜日かどうか
'''

__X__.weekday() == 6
'''
__Y__が日曜日かどうか
'''

__X__.timetuple()
'''
__Y__をタプルに変換する
'''

__X__.isoformat()
'''
__Y__をISO[|8601][形式|書式]の文字列に変換する
'''

__X__.strftime("%d/%m/%y")
'''
@test(s="%A, %d. %B %Y %I:%M%p";$$)
{__Y__を|sでフォーマットして}文字列に変換する
__Y__をsで_フォーマットする
'''

__X__.hour
'''
@X(aDatetime;datetime.date.today())
@Y(aDatetime;現在)
@alt(時間数|時間|時刻)
__Y__の時間数[|を得る]
__Y__[が|は]何時か知る
'''

__X__.minute
'''
@alt(分数|分)
__Y__の分数[|を得る]
__Y__[が|は]何分か知る
'''

__X__.second
'''
@alt(秒数|秒)
__Y__の秒数[|を得る]
__Y__[が|は]何秒か知る
'''

# タイム

int(time.time() * 1000)
'''
現在のミリ秒
'''

int(time.time())
'''
現在のタイムスタンプ
'''

aDatetime = datetime.datetime(2022, 1, 1, 12, 30)
aDate = datetime.date(2022, 7, 4)

n = 1

__X__ + datetime.timedelta(weeks=n)
'''
@X(aDatetime|aDate)
@Y(aDatetime|aDate)
@alt(前に進める|前にする|、進める)
@alt(加算する|[加える|足す])
__Y__ををn週間後に進める
__Y__にn週間[分、|を]加算する
'''

__X__ - datetime.timedelta(weeks=n)
'''
@alt(に戻す|にする)
@alt(減算する|[減らす|引く])
__Y__をn週間前に戻す
__Y__からn週間[分、|を]減算する
'''

__X__ + datetime.timedelta(days=n)
'''
__Y__ををn日後に進める
__Y__にn日[分、|を]加算する
'''

__X__ - datetime.timedelta(days=n)
'''
__Y__をn日前に戻す
__Y__からn日[分、|を]減算する
'''

__X__ + datetime.timedelta(hours=n)
'''
__Y__ををn時間後に進める
__Y__にn時間[分、|を]加算する
'''

__X__ - datetime.timedelta(hours=n)
'''
__Y__をn時間前に戻す
__Y__からn時間[分、|を]減算する
'''

__X__ + datetime.timedelta(minutes=n)
'''
__Y__ををn分後に進める
__Y__にn分[分、|を]加算する
'''

__X__ - datetime.timedelta(minutes=n)
'''
__Y__をn分前に戻す
__Y__からn分、減算する
'''

__X__ + datetime.timedelta(seconds=n)
'''
__Y__ををn秒後に進める
__Y__にn秒[分、|を]加算する
'''

__X__ - datetime.timedelta(seconds=n)
'''
__Y__をn秒前に戻す
__Y__からn秒[分、|を]減算する
'''

__X__2 = aDatetime
__X__ < __X__2
'''
__Y__[が|は]__Y__2より[前|先|早い]かどうか
'''

__X__ > __X__2
'''
__Y__[が|は]__Y__2より[後ろ|あと|遅い]かどうか
'''

__X__ == __X__2
'''
__Y__[が|は]__Y__2と同時かどうか
'''

__X__ - __X__2
'''
__Y__と__Y__2の時間差[|を求める]
'''

(__X__ - __X__2).total_seconds()
'''
__Y__と__Y__2の時間差を秒数で求める
__Y__と__Y__2の時間差[が|は]何秒か知る
'''

(__X__ - __X__2).total_seconds()//60
'''
__Y__と__Y__2の時間差を秒数で求める
__Y__と__Y__2の時間差[が|は]何分か知る
'''
