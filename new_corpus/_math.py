# math

import math
[mathモジュール|算術用ライブラリ]を[インポートする|用いる|使う|使用する]

x,y = 1.5, 3.1

math.sqrt(x)
'''
xの[平方根|ルート]
'''

math.ceil(x)
'''
xの[天井|天井数]
xを切り上げて整数に変換する
xを切り上げる
'''

math.floor(x)
'''
xの[床|床数]
xを切り下げて整数に変換する
xを切り下げる
'''

math.gcd(x, y)
'''
xとyの最大公約数
'''

math.lcm(x, y)
'''
xとyの最小公倍数
'''

math.comb(x, y)
'''
xとyの[コンビネーション|組み合わせ]
'''

math.copysign(x, y)
'''
{yの符号を/xに}コピーする
xの符号をyと同じにする
'''

math.fabs(x)
'''
xの絶対値
'''

math.factorial(x)
'''
nの階乗
'''

math.frexp(x)[0]
'''
xの仮数
'''

math.frexp(x)[1]
'''
xの指数
'''

math.isclose(x, y)
'''
xとyが近いかどうか
xとyが近似値かどうか
'''

math.isfinite(x)
'''
xが有限かどうか
'''

math.isinf(x)
'''
xが無限大かどうか
'''

math.isnan(x)
'''
xが[NaN|非数]かどうか
'''

math.modf(x)[0]
'''
xの小数部
'''

math.modf(x)[1]
'''
xの整数部
'''

math.perm(x)
'''
xの順列の[総]数
'''

math.perm(x, y)
'''
xからy個取り出した[とき|時]の順列の[総]数
'''

math.prod(l)
@type(l, リスト)の要素積

math.remainder(x, y)
'''
xをyで割った剰余
'''

math.exp(x)
'''
eのx乗
'''

math.log(x)
'''
xの自然対数
'''

math.log(x, y)
'''
yを底とするxの対数
yに対するxの対数
'''

math.log1p(x)
'''
1+xの自然対数
'''

math.log2(x)
'''
2を底とするxの対数
'''

math.log10(x)
'''
xの常用対数
xの10を底とする対数
'''

math.cos(x)
'''
xの[余弦|コサイン|cos]
'''

math.sin(x)
'''
xの[正弦|サイン|sin]
'''

math.tan(x)
'''
xの[正接|タンジェント|tan]
'''

math.acos(x)
'''
xの[逆余弦|アークコサイン]
xの[余弦|コサイン|cos]の逆数
'''

math.asin(x)
'''
xの[逆正弦|アークサイン]
xの[正弦|サイン|sin]の逆数
'''

math.atan(x)
'''
xの[逆正接|アークタンジェント]
xの[正接|タンジェント|tan]の逆数
'''

math.degrees(x)
'''
xの角度
'''

math.radians(x)
'''
xのラジアン
'''

math.acosh(x)
'''
xの逆双曲線余弦
xの[双曲線余弦|ハイパボリックコサイン]の逆数
'''

math.asinh(x)
'''
xの逆双曲線正弦
xの[双曲線正弦|ハイパボリックサイン]の逆数
'''

math.atanh(x)
'''
xの逆双曲線正接
xの[双曲線正接|ハイパボリックタンジェント]の逆数
'''

math.cosh(x)
'''
xの[双曲線余弦|ハイパボリックコサイン]
'''

math.sinh(x)
'''
xの[双曲線正弦|ハイパボリックサイン]
'''

math.tanh(x)
'''
xの[双曲線正接|ハイパボリックタンジェント]
'''

math.dist(x, y)
'''
xとyのユークリッド距離
'''

math.hypot(x,y)
'''
xとyのノルム
原点からの(x, y)の距離
'''

math.gamma(x)
'''
ガンマ関数
'''

math.lgamma(x)
'''
ガンマ関数の絶対値の自然対数
'''

math.pi
'''
[円周率|π]
'''

math.e
'''
[ネイピア数|自然対数の底]
'''

math.inf
'''
無限大
'''

math.nan
'''
[NaN|非数]
'''