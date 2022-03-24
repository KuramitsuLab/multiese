import numpy as np
'''
ベクトル[の|][演算|計算]を[する|行う]
行列[の|][演算|計算]を[する|行う]
numpyを[使う|入れる|インポートする]
'''

np.array(l)
'''
@type(l,リスト)から配列を[作る|作成する|作成]
'''
np.array(t)
'''
@type(t,タプル)から配列を作る
'''

a.shape()
'''
@type(a,配列)の[形状|形]を調べる
'''

a.dtype()
'''
@type(a,配列)の[データ型|型]を調べる
'''

np.ndim(x)
'''
@type(x,配列)の[次元数|次元の数]を調べる
'''

np.arange(10)
'''
0から9までの配列を作る
'''

x.reshape(3,3)
'''
@type(x,配列)を3×3の多次元配列に変形する
'''

np.concatenate([a,b])
'''
@type(a,配列)と@type(b,配列)を[列方向|縦方向]に連結する
'''

np.concatenate([a,b], axis=0)
'''
@type(a,配列)と@type(b,配列)を[列方向|縦方向]に連結する
'''

np.concatenate([a,b], axis=1)
'''
@type(a,配列)と@type(b,配列)を[行方向|横方向]に連結する
'''

np.sum(x)
'''
@type(x,配列)の[合計値|合計]を調べる
'''

np.sum(x, axis=0)
'''
@type(x,配列)の列ごとの[合計値|合計]を調べる
'''

np.sum(x, axis=1)
'''
@type(x,配列)の行ごとの[合計値|合計]を調べる
'''

np.mean(x)
'''
@type(x,配列)の[平均値|平均]を調べる
'''

np.mean(x, axis=0)
'''
@type(x,配列)の列ごとの[平均値|平均]を調べる
'''

np.mean(x, axis=1)
'''
@type(x,配列)の行ごとの[平均値|平均]を調べる
'''

np.min(x)
'''
@type(x,配列)の[最小値|最小]を調べる
'''

np.min(x, axis=0)
'''
@type(x,配列)の列ごとの[最小値|最小]を調べる
'''

np.min(x, axis=1)
'''
@type(x,配列)の行ごとの[最小値|最小]を調べる
'''

np.max(x)
'''
@type(x,配列)の[最大値|最大]を調べる
'''

np.max(x, axis=0)
'''
@type(x,配列)の列ごとの[最大値|最大]を調べる
'''

np.max(x, axis=1)
'''
@type(x,配列)の行ごとの[最大値|最大]を調べる
'''

np.std(x)
'''
@type(x,配列)の標準偏差を調べる
'''

np.std(x, axis=0)
'''
@type(x,配列)の列ごとの標準偏差を調べる
'''

np.std(x, axis=1)
'''
@type(x,配列)の行ごとの標準偏差を調べる
'''

np.var(x)
'''
@type(x,配列)の分散を調べる
'''

np.var(x, axis=0)
'''
@type(x,配列)の列ごとの分散を調べる
'''

np.var(x, axis=1)
'''
@type(x,配列)の行ごとの分散を調べる
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

np.empty_like(x)
'''
@type(x,配列)と同じ大きさの[空配列|空の配列]を作る
'''

np.gcd(a,b)
'''
@type(a,配列)と@type(b,配列)の要素ごとの最大公約数を調べる
'''

np.lcm(a,b)
'''
@type(a,配列)と@type(b,配列)の要素ごとの最小公倍数を調べる
'''

np.unique(x)
'''
@type(x,配列)から重複を除いた配列を作る
@type(x,配列)のユニークな要素を調べる
'''

u, counts = np.unique(a, return_counts=True)
'''
@type(x,配列)のユニークな要素とその個数を調べる
'''

u, indices = np.unique(x, return_index=True)
'''
@type(x,配列)のユニークな要素とその位置を調べる
'''

np.cumsum(x)
'''
@type(x,配列)の累積和を調べる
'''

np.cumprod(x)
'''
@type(x,配列)の累積積を調べる
'''

x.flatten()
'''
@type(x,配列)を[一次元にする|一次元化|平坦化]
'''
