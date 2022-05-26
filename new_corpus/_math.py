# math
from importlib import import_module

import math
'''
@test($$;type(math))
[math[|モジュール]|算術計算ライブラリ]を[インポートする|使う]
'''

math = import_module('math')

x, x2 = 1.5, 3.1
n, n2, n3 = 1, 3, 7

math.sqrt(x)
'''
xの[平方根|ルート][|を求める]
'''

math.ceil(x)
'''
xの[天井|天井数][|を求める]
x以上の最小の整数[|を求める]
xを切り上げて整数に変換する
xを切り上げる
'''

math.floor(x)
'''
xの[床|床数][|を求める]
x以下の最大の整数[|を求める]
xを切り下げて整数に変換する
xを切り下げる
'''

math.gcd(n, n2)
'''
@alt(最大公約数|GCD)
nとn2の最大公約数[|を求める]
'''

math.lcm(n, n2)
'''
@alt(最小公倍数|LCM)
nとn2の最小公倍数[|を求める]
'''

math.gcd(n, n2, n3)
'''
@test(n3=5;$$)
3数n,n2,n3の最大公約数[|を求める]
'''

math.lcm(n, n2, n3)
'''
@test(n3=120;$$)
3数n,n2,n3の最小公倍数[|を求める]
'''

math.comb(n, n2)
'''
@alt(コンビネーション|[組合せ|組み合わせ]|nCk)
nとn2のコンビネーション[|を求める]
n個の集まりからn2個[重複なく|]選ぶ方法[|を求める]
異なるn個のものからn2個選ぶ場合の数
'''

math.copysign(x, x2)
'''
{x2の符号を/xに}コピーする
xの符号をx2と同じにする
'''

math.fabs(x)
'''
xの絶対値[|を求める]
'''

math.factorial(n)
'''
nの階乗[|を求める]
'''

math.frexp(x)[0]
'''
xの仮数[|部][|を求める]
'''

math.frexp(x)[1]
'''
xの指数[|部][|を求める]
'''

math.isclose(x, x2)
'''
xとx2が[近い|近似値]かどうか
x[は|が]x2に[近い|ほぼ等しい]かどうか
'''

math.isfinite(x)
'''
x[が|は]有限かどうか
'''

math.isinf(x)
'''
x[が|は]無限大かどうか
'''

math.isnan(x)
'''
x[が|は][NaN|非数]かどうか
'''

math.modf(x)[0]
'''
xの小数部[|を求める]
'''

math.modf(x)[1]
'''
xの整数部[|を求める]
'''

math.perm(n)
'''
@(総数|数)
nの[順列|並べ方]の総数[|を求める]
'''

math.perm(n, n2)
'''
@alt(とき|時|場合)
n個からn2個取り出したときの[順列|並べ方]の総数[|を求める]
n個のものからn2個取り出したときの並べ方[の総数][|を求める]
'''

# math.prod(l)
# @type(l, リスト)の要素積

math.remainder(x, x2)
'''
xをx2で割った剰余[|を求める]
'''

math.exp(x)
'''
eのx乗[|を求める]
'''

math.log(x)
'''
xの自然対数[|を求める]
'''

math.log(x, x2)
'''
x2を底とするxの対数[|を求める]
x2に対するxの対数[|を求める]
'''

math.log1p(x)
'''
1+xの自然対数
'''

math.log2(x)
'''
xの[二進|2進|バイナリ]対数[|を求める]
2を底とするxの対数[|を求める]
'''

math.log10(x)
'''
xの常用対数[|を求める]
10を底とするxの対数[|を求める]
'''

math.cos(x)
'''
xの[余弦|コサイン|cos][|を求める]
'''

math.sin(x)
'''
xの[正弦|サイン|sin][|を求める]
'''

math.tan(x)
'''
xの[正接|タンジェント|tan][|を求める]
'''

x = 0.33
math.acos(x)
'''
@test(x=0.33;$$)
xの[逆余弦|アークコサイン][|を求める]
xの[余弦|コサイン|cos]の逆数[|を求める]
'''

math.asin(x)
'''
@test(x=0.33;$$)
xの[逆正弦|アークサイン][|を求める]
xの[正弦|サイン|sin]の逆数[|を求める]
'''

math.atan(x)
'''
@test(x=0.33;$$)
xの[逆正接|アークタンジェント][|を求める]
xの[正接|タンジェント|tan]の逆数[|を求める]
'''

x = math.pi/2

math.degrees(x)
'''
xの角度[|を求める]
'''

degree = 60

math.radians(degree)
'''
xのラジアン[|を求める]
'''

math.acosh(x)
'''
@alt(・|)
xの逆双曲線余弦[|を求める]
xの[双曲線余弦|ハイパボリック・コサイン]の逆数[|を求める]
'''

math.asinh(x)
'''
xの逆双曲線正弦[|を求める]
xの[双曲線正弦|ハイパボリック・サイン]の逆数[|を求める]
'''

math.atanh(x)
'''
@test(x=0.3;$$)
xの逆双曲線正接[|を求める]
xの[双曲線正接|ハイパボリック・タンジェント]の逆数[|を求める]
'''

math.cosh(x)
'''
xの[双曲線余弦|ハイパボリック・コサイン][|を求める]
'''

math.sinh(x)
'''
xの[双曲線正弦|ハイパボリック・サイン][|を求める]
'''

math.tanh(x)
'''
@test(x=0.33;$$)
xの[双曲線正接|ハイパボリック・タンジェント][|を求める]
'''


point = (1, 2)
point2 = (0, 1)

math.dist(point, point2)
'''
@test(x=(1,0);x2=(0,1);$$)
@prefix(point;[点|ベクトル])
pointとpoint2のユークリッド距離[|を求める]
'''

math.hypot(x, x2)
'''
xとx2の[斜辺|ノルム][|を求める]
原点からの(x, x2)の距離[|を求める]
'''

math.gamma(x)
'''
ガンマ関数[|を使う]
xにおけるガンマ関数の値[|を求める]
'''

math.lgamma(x)
'''
xにおけるガンマ関数の絶対値に自然対数をとった値[|を求める]
'''

math.pi
'''
[円周率|π][|を使う]
'''

math.e
'''
[ネイピア数|自然対数の底][|を使う]
'''

math.inf
'''
無限大[|を使う]
'''

math.nan
'''
[NaN|非数][|を使う]
'''
