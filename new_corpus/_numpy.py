import numpy as np
'''
ベクトル[の|][演算|計算]を[する|行う]
行列[の|][演算|計算]を[する|行う]
numpyを[使う|入れる|インポートする]
@prefix(aArray;配列)
'''

iterable = np.array([0, 1, 2, 3])
aArray = np.array([1, 2, 3, 4])
aArray2 = iterable
aList = [1, 2]

np.array(aList)
'''
aListから配列を[作る]
'''

np.array(iterable)
'''
iterableから配列を作る
'''

aArray.shape()
'''
aArrayの[形状|形]を調べる
'''

aArray.dtype()
'''
aArrayの[データ型|型]を調べる
'''

np.ndim(aArray)
'''
aArrayの[次元数|次元の数]を調べる
'''

np.arange(10)
'''
0から9までの配列を作る
'''

aArray.reshape(3, 3)
'''
aArrayを3×3の多次元配列に変形する
'''

np.concatenate([aArray, aArray2])
'''
aArrayと@aArray2を[列方向|縦方向]に連結する
'''

np.concatenate([aArray, aArray2], axis=0)
'''
aArrayと@aArray2を[列方向|縦方向]に連結する
'''

np.concatenate([aArray, aArray2], axis=1)
'''
aArrayと@aArray2を[行方向|横方向]に連結する
'''

np.sum(aArray)
'''
aArrayの[合計値|合計]を調べる
'''

np.sum(aArray, axis=0)
'''
aArrayの列ごとの[合計値|合計]を調べる
'''

np.sum(aArray, axis=1)
'''
aArrayの行ごとの[合計値|合計]を調べる
'''

np.mean(aArray)
'''
aArrayの[平均値|平均]を調べる
'''

np.mean(aArray, axis=0)
'''
aArrayの列ごとの[平均値|平均]を調べる
'''

np.mean(aArray, axis=1)
'''
aArrayの行ごとの[平均値|平均]を調べる
'''

np.min(aArray)
'''
aArrayの[最小値|最小]を調べる
'''

np.min(aArray, axis=0)
'''
aArrayの列ごとの[最小値|最小]を調べる
'''

np.min(aArray, axis=1)
'''
aArrayの行ごとの[最小値|最小]を調べる
'''

np.max(aArray)
'''
aArrayの[最大値|最大]を調べる
'''

np.max(aArray, axis=0)
'''
aArrayの列ごとの[最大値|最大]を調べる
'''

np.max(aArray, axis=1)
'''
aArrayの行ごとの[最大値|最大]を調べる
'''

np.std(aArray)
'''
aArrayの標準偏差を調べる
'''

np.std(aArray, axis=0)
'''
aArrayの列ごとの標準偏差を調べる
'''

np.std(aArray, axis=1)
'''
aArrayの行ごとの標準偏差を調べる
'''

np.var(aArray)
'''
aArrayの分散を調べる
'''

np.var(aArray, axis=0)
'''
aArrayの列ごとの分散を調べる
'''

np.var(aArray, axis=1)
'''
aArrayの行ごとの分散を調べる
'''

np.eye(3)
'''
3×3の単位行列を作る
'''

np.identity(3)
'''
3×3の単位行列を作る
'''

np.empty(5)
'''
要素数5の[空配列|空の配列]を作る
'''

np.empty((2, 3))
'''
2×3の[空配列|空の配列]を作る
'''

np.empty_like(aArray)
'''
aArrayと同じ大きさの[空配列|空の配列]を作る
'''

np.gcd(aArray, aArray2)
'''
aArrayと@aArray2の要素ごとの最大公約数を調べる
'''

np.lcm(aArray, aArray2)
'''
aArrayと@aArray2の要素ごとの最小公倍数を調べる
'''

np.unique(aArray)
'''
aArrayから重複を除いた配列を作る
aArrayのユニークな要素を調べる
'''

u, counts = np.unique(aArray, return_counts=True)
'''
aArrayのユニークな要素とその個数を調べる
'''

u, indices = np.unique(aArray, return_index=True)
'''
aArrayのユニークな要素とその位置を調べる
'''

np.cumsum(aArray)
'''
aArrayの累積和を調べる
'''

np.cumprod(aArray)
'''
aArrayの累積積を調べる
'''

aArray.flatten()
'''
aArrayを[一次元にする|一次元化|平坦化]
'''
