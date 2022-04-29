import json
'''
@test($$;type(json))
@alt(形式|フォーマット)
JSONを使う
'''

json.loads(s)
'''
@test(json=missing;$$)
JSON[形式の|]sを辞書に変換する
JSON[形式の|]sをデータに変換する
JSON[形式の|]sを[読み込む|ロードする]
'''

json.loads(b.decode('unicode-escape'))
'''
@test(json=missing;b=b'{}';$$)
@prefix(b;バイト列;)
JSON形式のbを辞書に変換する
JSON[形式の|]sをデータに変換する
'''

json.load(fin)
'''
@test(json=missing;fin=sys.stdin;$$)
JSON[ファイル|形式]のfinを辞書に変換する
JSON[ファイル|形式]のfをデータに変換する
'''

data = json.load(fin)
'''
@test(json=missing;fin=sys.stdin;$$;data)
JSON[ファイル|形式]のfinを読み込んで、dataとする
'''

json.dumps(adict, ensure_ascii=False)
'''
@test(json=missing;$$)
adictをJSON形式の文字列に変換する
'''

json.dumps(adict, ensure_ascii=False, indent=n)
'''
@test(json=missing;$$)
{[インデント|改行]付きで|adictを}文字列に変換する
adictを{インデント幅nの|JSON形式の}文字列に変換する
インデント幅nで、adictをJSON形式の文字列に変換する
'''

json.dumps(adict, ensure_ascii=False, sort_keys=True)
'''
@test(json=missing;$$)
adictを[ソートして|並べ直して]JSON形式の文字列に変換する
'''

json.dump(adict, fout, ensure_ascii=False)
'''
@test(json=missing;fout=sys.stdout;$$)
adictをJSON形式でfoutに保存する
'''
