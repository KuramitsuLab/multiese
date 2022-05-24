from importlib import import_module


copy = import_module('copy')

aDict = {'A': 1}
aDict2 = {'B': 0}
key = 'A'
key2 = 'B'
element = 1

{}
'''
空の辞書[|を作る]
'''

dict(name=element)
'''
変数名をキーとして、辞書[|を作る]
'''

aDict[key]
'''
@alt(得る|参照する|見る)
aDictのkeyの値[|を得る]
'''

list(aDict)
'''
@alt(キー|項目名)
aDictのキー一覧[|を得る]
'''

len(aDict)
'''
@alt(エントリ|項目)
aDictのエントリ数[|を得る]
'''

aDict.clear()
'''
@alt(クリアする|消去する|空にする)
aDictの全[エントリ]をクリアする
'''

aDict.copy()
'''
aDictを[|浅く]コピーする
aDictの[浅い|]コピーを行う
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
@alt(の一覧|一覧)
aDictの[エントリ|キーとその値]の一覧
'''

aDict.keys()
'''
aDictのキーの一覧
'''

aDict.values()
'''
aDictの[値]の一覧
'''

element in aDict.values()
'''
{elementが|aDictの値に}含まれているかどうか
'''

element not in aDict.values()
'''
{elementが|aDictの値に}含まれていないかどうか
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
@test($$;aDict)
alt(追加更新する|追加する|加えて、更新する)
aDictにaDict2のエントリを追加更新する
'''

kwargs = dict(A=1, B=2)

aDict.update(**kwargs)
'''
@test(kwargs={'B':2};$$;aDict)
aDictにキーワード引数kwargsを追加更新する
'''

aDict | aDict2
'''
@alt(合体する|結合する|マージする)
ふたつの辞書を合体する
aDictとaDict2を合体する
'''

aDict.pop(key)
'''
aDictからkeyを取り除く
'''

aDict.popitem()
'''
aDictから最後に追加したエントリを取り出す
'''


{v: k for k, v in aDict.items()}
'''
aDictのキーと値を入れ替える
'''

aList = [1, 2, 3]
aList2 = [4, 5, 6]

dict(zip(aList, aList2))
'''
aListとaList2から辞書[|を作成する]
'''

dict(aDict)
'''
@alt(コピーする|複製する)
aDictを[浅く|]コピーする
aDictのコピー[を[得る|作る]]
'''

{k: copy.copy(v) for k, v in aDict.items()}
'''
@test(import copy;$$)
aDictを値を含めてコピーする
'''
