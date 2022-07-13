from importlib import import_module

copy = import_module('copy')

aDict = {'A': 1}
aDict2 = {'B': 0}
key = 'A'
key2 = 'B'
element = 1

{}
'''
@alt(辞書|辞書|[マップ|マッピング])
@alt(キー|項目名)
@alt(エントリ=[項目|エントリ|値])
@alt(得る|参照する|見る)
@alt(クリアする|消去する|空にする)

@prefix(key;[キー|項目名])
@prefix(element;要素)

空の辞書[|を作る]
'''

dict(name=element)
'''
変数名をキーとして、辞書[|を作る]
'''

aDict[key]
'''
aDictのkeyの値[|を得る]
'''

list(aDict)
'''
aDictのキーを列挙する
aDictのキー一覧[|を得る]
'''

len(aDict)
'''
aDictのエントリ数[|を得る]
'''

aDict.clear()
'''
aDict[の全[エントリ]|]をクリアする
'''

aDict.copy()
'''
aDictを[|浅く]コピーする
aDictの[浅い|]コピーを作る
'''

aDict.get(key)
'''
aDictからkeyの値[|を得る]
aDictのkeyに対応した値[|を得る]
'''

aDict.get(key, None)
'''
{aDictからkeyの値を|エラーなく}得る
'''

aDict.get(key, element)
'''
aDictからkeyの値か、もしくはelementを得る
'''

key in aDict
'''
@alt(存在する|ある|存在している)
@alt(定義済み|[|既に]定義されている)

{keyが|aDictに}存在するかどうか
{keyが|aDict上で}定義済みかどうか
'''

key not in aDict
'''
@alt(存在しない|ない|存在していない)
@alt(未定義|[まだ|]定義されていない)

{keyが|aDictに}存在するかどうか
{keyが|aDict上で}未定義かどうか
'''

aDict.items()
'''
aDictのキーとその[値|エントリ]を列挙する
aDictのキーとその[値|エントリ]をペアとして取り出す
'''

aDict.keys()
'''
aDictのキーを列挙する
aDictのキーの一覧[|を得る]
'''

aDict.values()
'''
aDictの[値|エントリ]を列挙する
aDictの[値]の一覧[|を得る]
'''

element in aDict.values()
'''
{element[が|は]|aDictの値として}含まれているかどうか
'''

element not in aDict.values()
'''
{element[が|は]|aDictの値に}含まれていないかどうか
'''

aDict[key] = element
'''
@test($$;aDict)
aDictのkeyをelementに[設定|変更|]する
aDictにelementをkeyとして加える
'''

aDict.setdefault(key, element)
'''
@alt(とき|時|場合)
{keyが|aDictに}存在しないとき、elementを追加する
'''


aDict.update(aDict2)
'''
@alt(追加更新する=[更新する|追加する|加えて、更新する])

aDictに[|別の]aDict2のエントリを追加更新する
'''

kwargs = dict(A=1, B=2)

aDict.update(**kwargs)
'''
{aDictに|キーワード引数で_}追加更新する
'''

aDict | aDict2
'''
@alt(合体する|結合する|マージする)

ふたつの辞書を合体する
'''

aDict.pop(key)
'''
@alt(ポップする|取り出す)

{aDictから|keyで指定されたエントリを}ポップする
'''

aDict.popitem()
'''
{aDictから|最後[の|に追加した]エントリを}ポップする
'''


{v: k for k, v in aDict.items()}
'''
aDictのキーと値を入れ替える
'''

aList = [1, 2, 3]
aList2 = [4, 5, 6]

dict(zip(aList, aList2))
'''
２つのリストから辞書[|を作る]
'''

dict(aDict)
'''
@alt(コピーする|複製する)
aDictを[浅く|]コピーする
aDictのコピー[|を作る]
'''

{k: copy.copy(v) for k, v in aDict.items()}
'''
aDictの[内部|値]もコピーする
'''
