from importlib import import_module
import io

import json
'''
@alt(形式|フォーマット)
JSONを使う
'''

json = import_module('json')
文字列 = "{'A':1}"
バイト列 = b"{'A':1}"
辞書 = {'A': 0}
ファイル入力 = io.StringIO(文字列)
ファイル出力 = io.StringIO(mode='w')
n = 0
'''
@alt(ファイル入力|入力ストリーム|入力)
@alt(ファイル出力|出力ストリーム|出力)
'''

with open('file.json') as f:
    data = json.load(f)
'''
@alt(読む|読み込む|ロードする)
@alt(構文解析する|パースする)

ファイルからJSON[形式のデータ|]を読む
JSON[形式の|]ファイルを構文解析する
'''

json.load(ファイル入力)
'''
ファイル入力からJSON[形式のデータ|]を読む
ファイル入力をJSONとして構文解析する
JSON[形式の|]ファイル入力を辞書に変換する
'''

data = json.loads(文字列)
'''
文字列からJSON[形式のデータ|]を読む
JSON[形式の|]文字列を構文解析する
JSON[形式の|]文字列を読む
JSON[形式の|]文字列を[辞書|オブジェクト|データ]に変換する
'''

json.loads(バイト列.decode('unicode-escape'))
'''
バイト列からJSON[形式のデータ|]を読む
JSON[形式の|]バイト列を構文解析する
'''

__X__ = 辞書
'''
@X(辞書|リスト|文字列|データ)
@Y(辞書|リスト|文字列|データ)
'''

json.dumps(__X__, ensure_ascii=False)
'''
__Y__をJSON[形式の|]文字列に変換する
__Y__をJSON[形式|]にエンコードする
'''

json.dumps(__X__, ensure_ascii=False, indent=n)
'''
{インデント[|幅]を指定して|__Y__を}JSON文字列に変換する
{__Y__を|インデント[|幅]を指定して}JSON[形式|]にエンコードする
'''

json.dumps(__X__, ensure_ascii=False, sort_keys=True)
'''
{__Y__を|ソートして}JSON[形式|]にエンコードする
'''

json.dump(__X__, ファイル出力, ensure_ascii=False)
'''
{__Y__を|JSON形式で_}ファイル出力に[保存する|出力する|ダンプする]
'''

with open('file.json', 'w') as f:
    json.dump(__X__, f, ensure_ascii=False)
'''
{__Y__を|JSON形式で_}[|指定した]ファイルに[保存する|出力する|ダンプする]
'''
