import numpy as np
'''
@alt(配列|行列|ベクトル)
@alt(作る=[作る|作成する|初期化する])
@alt(求める=[求める|[計算|算出]する|[得る|調べる]])


@prefix(aArray;[配列|行列|ベクトル])
@prefix(aList;リスト)

@alt(要素ごと|各要素)

ベクトル[の|][演算|計算]を[する|行う]
行列[の|][演算|計算]を[する|行う]
numpyを[使う|入れる|インポートする]
'''

iterable = np.array([0, 1, 2, 3])
aArray = np.array([1, 2, 3, 4])
aArray2 = iterable
aList = [1, 2]
n = 3

要素数 = 3
行数 = 2
列数 = 2
初期値 = 0
行番号 = 0
列番号 = 0

N = 10
開始値 = 0
終了値 = 10
等差 = 2

__X__ = np.int
dtype = __X__
'''
@X(np.int;np.int8;np.uint8;np.int16;np.int32;bool;complex)
@Y(整数;８ビット整数;符号なし８ビット整数;３２ビット整数;[ブール|論理値];複素数)

option: [配列の|]データ型を指定する
option: [|データ型として]__Y__型を使う
'''

np.array(aList)
'''
aListを配列に変換する
{aListから|配列を}作る
'''

np.array(iterable)
'''
iterableを配列に変換する
{iterableから|配列を}作る
'''

np.zeros(要素数)
'''
{全要素を|0で}初期化した配列[|を作る]
ゼロ埋めされた配列[|を作る]
'''

np.zeros(要素数, dtype=__X__)
'''
{ゼロ埋めされた|__Y__型の}配列[|を作る]
'''

np.zeros(行数, 列数)
'''
{全要素を|０で}初期化した行列[|を作る]
ゼロ埋めされた行列[|を作る]
'''

np.zeros(行数, 列数, dtype=__X__)
'''
{{全要素を|０で}初期化した|__Y__型の}行列[|を作る]
'''

np.ones(要素数, dtype=np.int)
'''
{全要素を|1で}初期化した配列[|を作る]
要素が全て1の配列[|を作る]
'''

np.ones(行数, 列数, dtype=np.int)
'''
{全要素を|1で}初期化した行列[|を作る]
全要素が1の行列[|を作る]
'''

np.full(要素数, 初期値, dtype=np.int)
'''
{全要素を|初期値で}初期化した配列[|を作る]
要素が全て初期値の配列[|を作る]
'''

np.full((行数, 列数), 初期値, dtype=np.int)
'''
{全要素を|初期値で}初期化した行列[|を作る]
全要素が初期値の行列[|を作る]
'''

np.eye(行数, 列数)
'''
単位行列[|を作る]
'''

np.identity(n)
'''
[単位正方行列|正方単位行列][|を作る]
'''

np.empty(要素数, dtype=np.int)
'''
未初期化の配列[|を作る]
'''

np.empty((行数, 列数), dtype=np.int)
'''
未初期化の行列[|を作る]
'''

np.empty_like(aArray)
'''
aArrayと同じ大きさの[空配列|空の配列]を作る
'''

np.arange(N)
'''
[0から|]N未満までの配列[|を作る]
'''

np.arange(1, N+1)
'''
1からNまでの配列[|を作る]
'''

np.arange(開始値, 終了値, 等差)
'''
[連続した|連番の]配列の[自動|]作成する
等間隔の配列[を作る＼]
等差数列を配列に変換する
'''

np.linspace(最小値, 最大値, 要素数)
'''
[最大最小|範囲|区間]から配列[|を作る]
'''

np.random.random(N)
'''
乱数[で要素を埋めた|の]配列[|を作る]
'''

np.random.random((行数, 列数))
'''
乱数[の|で要素を埋めた]行列[|を作る]
'''

np.random.randint(開始値, 終了値, N)
'''
整数乱数[で要素を埋めた|の]配列[|を作る]
'''

np.random.randint(開始値, 終了値, (行数, 列数))
'''
整数乱数[で要素を埋めた|の]行列[|を作る]
'''


aArray.reshape(行数, 列数)
'''
aArray[の[次元|形状]|]を変形する
'''

aArray.reshape(-1, 1)
'''
aArrayを[2次元1列|縦ベクトル]に変形する
'''

aArray.reshape(1, -1)
'''
aArrayを[2次元1行|横ベクトル]に変形する
'''

np.zeros_like(aArray)
'''
@alt(ベースに=[元に|ベースに][|して])

[既存の|]aArrayをベースに全要素が0の配列[|を作る]
'''

np.ones_like(aArray)
'''
[既存の|]aArrayをベースに全要素が1の配列[|を作る]
'''

np.full_like(aArray, 初期値)
'''
[既存の|]aArrayをベースに全要素が初期値の配列[|を作る]
'''

指定の値 = 0

aArray[:, :] = 指定の値
'''
aArrayの全要素の値を変更する
aArrayの全要素を指定の値にする
'''

aArray[行番号, 列番号]
'''
[行列|aArray]の値[|を得る]
'''

aArray[行番号, 列番号] = 指定の値
'''
[行列|aArray]の値を変更する
'''

aArray[行番号]
'''
[行列|aArray]の行[|を選択する]
'''

aArray[:, 列番号]
'''
[行列|aArray]の列[|を選択する]
'''

# ユニーク

np.unique(aArray)
'''
[|aArrayの]ユニークな値を要素とする配列[|を得る]
'''

np.unique(aArray, return_counts=True)
'''
[|aArrayの]ユニークな要素ごとの[頻度|出現回数][|を得る]
'''


# 転置行列

[list(x) for x in list(zip(*aList))]
'''
２次元リストを転置する
２次元リストの転置行列[|を求める]
'''

aArray.T
'''
aArrayを転置する
[行列|aArray]の転置行列[|を求める]
'''

aArray + aArray2
'''
aArrayの和[|を求める]
aArrayの要素ごとに加算する
'''

aArray - aArray2
'''
aArrayの差[|を求める]
'''

aArray * n
'''
aArrayのスカラー倍[|を求める]
'''

np.multiply(aArray, aArray2)
'''
aArrayの要素ごとの[積|アダマール積][|を求める]
'''

np.dot(aArray, aArray2)
'''
aArrayの内積[|を求める]
'''

np.matmul(aArray, aArray2)
'''
[[行列|aArray]の|]行列積[|を求める]
'''

np.linalg.inv(aArray)
'''
[[行列|aArray]の|]逆行列[|を求める]
'''

np.linalg.pinv(aArray)
'''
[[行列|aArray]の|]ムーア・ペンローズの擬似逆行列[|を求める]
'''


np.linalg.det(aArray)
'''
[[行列|aArray]の|]行列式[|を求める]
'''

np.linalg.eig(aArray)
'''
FIXME
'''

# ユニバーサル関数

np.gcd(aArray, aArray2)
'''
aArray[間|]の要素ごとの最大公約数[|を求める]
'''

np.lcm(aArray, aArray2)
'''
aArray[間|]の要素ごとの最小公倍数[|を求める]
'''

aArray.shape
'''
aArrayの[形状|形][|を求める]
'''

aArray.dtype()
'''
aArrayの[データ型|型][|を求める]
aArray[が|は]何のデータ型か調べる
'''

aArray.ndim
'''
aArrayの[次元数|次元の数][|を求める]
aArray[は|が]何次元か調べる
'''

aArray.size
'''
aArrayの[要素数|個数][|を求める]
aArrayにはいくつ要素が[ある|含まれる|存在する]か調べる
'''


np.concatenate([aArray, aArray2], axis=0)
'''
[２つの|]配列を[列方向|縦方向]に連結する
'''

np.concatenate([aArray, aArray2], axis=1)
'''
[２つの|]配列を[行方向|横方向]に連結する
'''

np.sum(aArray)
'''
aArrayの[合計値|合計][|を求める]
'''

np.sum(aArray, axis=0)
'''
aArrayの列ごとの[合計値|合計][|を求める]
'''

np.sum(aArray, axis=1)
'''
aArrayの行ごとの[合計値|合計][|を求める]
'''

np.mean(aArray)
'''
aArrayの[平均値|平均][|を求める]
'''

np.mean(aArray, axis=0)
'''
aArrayの列ごとの[平均値|平均][|を求める]
'''

np.mean(aArray, axis=1)
'''
aArrayの行ごとの[平均値|平均][|を求める]
'''

np.min(aArray)
'''
aArrayの[最小値|最小][|を求める]
'''

np.min(aArray, axis=0)
'''
[行列|aArray]の列ごとの[最小値|最小][|を求める]
'''

np.min(aArray, axis=1)
'''
[行列|aArray]の行ごとの[最小値|最小][|を求める]
'''

np.max(aArray)
'''
aArrayの[最大値|最大][|を求める]
'''

np.max(aArray, axis=0)
'''
[行列|aArray]の列ごとの[最大値|最大][|を求める]
'''

np.max(aArray, axis=1)
'''
[行列|aArray]の行ごとの[最大値|最大][|を求める]
'''

np.std(aArray)
'''
aArrayの標準偏差[|を求める]
'''

np.std(aArray, axis=0)
'''
[行列|aArray]の列ごとの標準偏差[|を求める]
'''

np.std(aArray, axis=1)
'''
[行列|aArray]の行ごとの標準偏差[|を求める]
'''

np.var(aArray)
'''
aArrayの分散[|を求める]
'''

np.var(aArray, axis=0)
'''
[行列|aArray]の列ごとの分散[|を求める]
'''

np.var(aArray, axis=1)
'''
[行列|aArray]の行ごとの分散[|を求める]
'''

np.cumsum(aArray)
'''
aArrayの累積和[|を求める]
'''

np.cumprod(aArray)
'''
aArrayの累積積[|を求める]
'''

np.unique(aArray)
'''
aArrayから重複を除いた配列を作る
aArrayのユニークな要素[|を求める]
'''

u, counts = np.unique(aArray, return_counts=True)
'''
aArrayのユニークな要素とその個数[|を求める]
'''

u, indices = np.unique(aArray, return_index=True)
'''
aArrayのユニークな要素とその[位置|インデックス][|を求める]
'''

aArray.flatten()
'''
aArrayを[平坦化|フラット化|一次元化]する
aArrayを[平坦|フラット|一次元]にする
'''
