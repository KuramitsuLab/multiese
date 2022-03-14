import copy
adict = {'A': 1}
key = 'A'
element = 1

{}
'''
空の辞書[|を作る]
'''

dict(name=element)
'''
変数名をキーとして、辞書[|を作る]
'''

adict[key]
'''
@alt(得る|参照する|見る)
adictのkeyの値[|を得る]
'''

list(adict)
'''
@alt(キー|項目名)
adictのキー一覧[|を得る]
'''

len(adict)
'''
@alt(エントリ|項目)
adictのエントリ数[|を得る]
'''

adict.clear()
'''
@alt(クリアする|消去する|空にする)
adictの全[エントリ]をクリアする
'''

adict.copy()
'''
adictを[|浅く]コピーする
adictの[浅い|]コピーを行う
'''

adict.get(key)
'''
adictからkeyの値[|を得る]
adictのkeyに対応した値[|を得る]
'''

adict.get(key, None)
'''
{adictからkeyの値を|エラーなく}得る
'''

adict.get(key, element)
'''
{adictからkeyの値か、もしくはelementを得る
'''

key in adict
'''
@alt(存在する|ある|存在している)
@alt(定義済み|[|既に]定義されている)
{keyが|adictに}存在するかどうか
{keyが|adict上で}定義済みかどうか
'''

key not in adict
'''
@alt(存在しない|ない|存在していない)
@alt(未定義|[まだ|]定義されていない)
{keyが|adictに}存在するかどうか
{keyが|adict上で}未定義かどうか
'''

adict.items()
'''
@alt(の一覧|一覧)
adictの[エントリ|キーとその値]の一覧
'''

adict.keys()
'''
adictのキーの一覧
'''

adict.values()
'''
adictの[値]の一覧
'''

element in adict.values()
'''
{elementが|adictの値に}含まれているかどうか
'''

element not in adict.values()
'''
{elementが|adictの値に}含まれていないかどうか
'''

adict[key] = element
'''
@test(_;adict)
adictのkeyをelementに[設定|変更|]する
adictにelementをkeyとして加える
'''

adict.setdefault(key, element)
'''
@alt(とき|時|場合)
{keyが|adictに}存在しないとき、elementを追加する
'''

adict.update(adict2)
'''
@test(_;adict)
alt(追加更新する|追加する|加えて、更新する)
adictにadict2のエントリを追加更新する
'''

adict.update(**kwargs)
'''
@test(kwargs={'B':2};_;adict)
adictにキーワード引数kwargsを追加更新する
'''

adict | adict2
'''
@alt(合体する|結合する|マージする)
ふたつの辞書を合体する
adictとadict2を合体する
'''

adict.pop(key)
'''
adictからkeyを取り除く
'''

adict.popitem()
'''
adictから最後に追加したエントリを取り出す
'''


{v: k for k, v in adict.items()}
'''
adictのキーと値を入れ替える
'''

dict(zip(alist, alist2))
'''
alistとalist2から辞書[|を作成する]
'''

dict(adict)
'''
@alt(コピーする|複製する)
adictを[浅く|]コピーする
adictのコピー[を[得る|作る]]
'''

{k: copy.copy(v) for k, v in adict.items()}
'''
@test(import copy;_)
adictを値を含めてコピーする
'''
