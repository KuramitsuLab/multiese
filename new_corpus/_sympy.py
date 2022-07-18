import sympy
'''
@alt(シンボル|記号|変数)
@prefix(z;[変数|パラメータ])
@prefix(e;[数式|数値])

[代数計算|シンボル計算|数式処理][|モジュール|ライブラリ]を使う
'''

変数名 = 'z'


sympy.Symbol(変数名)
'''
sをシンボルに変換する
sを代数計算の変数に変換する
sの変数名を数式に変換する
'''

x = sympy.Symbol('x')
'''
xを[シンボル|変数][に|化]する
'''

変数 = x
__X__ = x
'''
@X(変数;[|変数]x;y)
@Y(変数;[|変数]x;y)
'''

数式 = 数式2 = sympy.Symbol(変数名)
数値 = 2
oo = sympy.oo

数式.subs(__X__, 数値)
'''
数式の__Y__に数値を代入する
'''

数式.subs(__X__, 数式2)
'''
数式の__Y__に別の数式を代入する
数式の__X__を[指定した|別の]数式で置き換える
'''

sympy.expand(数式)
'''
数式を展開する
数式の展開を行う
'''

sympy.factor(数式)
'''
数式を因数分解する
数式の因数分解を行う
'''

sympy.sympify(数式)
'''
数式を簡[略|単][に|化]する
数式の簡[略|単]化を行う
'''

sympy.apart(数式)
'''
{数式を|部分分数[に|として]}展開する
数式の部分分数化[を行う|する]
'''

# Expand `e` into partial fractions

sympy.solve(数式)
'''
{数式を|方程式として}解く
方程式の解[|を求める]
'''

# Solve a formula as an equation
# Solve a equation `e`
# Find solutions to equations

sympy.solve(数式, __X__)
'''
{数式を|__Y__の方程式として}解く
{方程式として|数式のzの解を}求める
'''

sympy.solve([数式, 数式2])
'''
連立方程式の解を求める
連立方程式を解く
'''

# Solve simultaneous equations
# Find solutions to simultaneous equations

sympy.limit(数式, __X__, 0)
'''
@alt(とき|時|場合|際)

__Y__が0に近づくとき[の|、][数式の|]極限値を求める
'''

sympy.limit(数式, __X__, oo)
'''
__Y__が無限大に近づくとき[の|、][数式の|]極限値を求める
'''

sympy.limit(数式, __X__, -oo)
'''
__Y__がマイナス無限大に近づくとき[の|、][数式の|]極限値を求める
'''

sympy.diff(数式)
'''
数式を微分する
数式の微分を求める
'''

sympy.diff(数式, __X__)
'''
__Y__について[数式の|][偏|]微分を[行う|求める]
{[数式を|]|__Y__について}[偏|]微分する
'''

n = 2

sympy.diff(数式, __X__, n)
'''
{数式を|__Y__について}n階[|偏]微分する
[数式の|][__Y__についての|]n階[|偏]微分を[求める|行う]
'''

sympy.integrate(数式)
'''
数式を積分する
数式の[積分|インテグラル]を[求める|行う]
'''

sympy.integrate(数式, __X__)
'''
__Y__について数式を積分する
__Y__について数式の[積分|インテグラル]を[求める|行う]
'''

e = sympy.E

float(数式)
'''
数式の数値[を求める|]
数式を数値計算する
数式を[数値|浮動小数点数]に変換する
'''

sympy.sqrt(数式)
'''
数式の平方根を求める
'''

# sympy.E**(sympy.I * sympy.pi) == -1
# '''
# オイラーの等式を使う
# '''

# sympy.summation(数式, (z, 1, N))
# '''
# @test(import sympy;z,N=sympy.Symbol('z N');e=z**2;$$)
# 数式の総和[|を求める]
# '''
