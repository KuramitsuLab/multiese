import sympy
'''
@alt(シンボル|記号|変数)
@prefix(z;[変数|パラメータ])
@prefix(e;[数式|数値])

[代数計算|シンボル計算|数式処理][|モジュール|ライブラリ]を使う
'''

s = 'z'

sympy.Symbol(s)
'''
sをシンボルに変換する
sを代数計算の変数に変換する
sの変数名を数式に変換する
'''

z = sympy.Symbol(s)
'''
sを[シンボル|変数][に|化]して、zにする
'''

e = e2 = sympy.Symbol(s)
n = 2
oo = sympy.oo

e.subs(z, n)
'''
eのzにnを代入する
'''

e.subs(z, e2)
'''
eのzにe2を代入する
eのzをe2で置き換える
'''

sympy.expand(e)
'''
eを展開する
eの展開を行う
'''

sympy.factor(e)
'''
eを因数分解する
eの因数分解を行う
'''

sympy.sympify(e)
'''
eを簡単[に|化]する
eを簡略[に|化]する
eの簡[略|単]化を行う
'''

sympy.apart(e)
'''
eを部分分数[に|として]展開する
eの部分分数化[を行う|する]
'''
# Expand `e` into partial fractions


sympy.solve(e)
'''
{eを|方程式として}解く
方程式の解[|を求める]
'''

# Solve a formula as an equation
# Solve a equation `e`
# Find solutions to equations

sympy.solve(e, z)
'''
{方程式として|eのzの解を}求める
'''

sympy.solve([e, e2])
'''
連立方程式の解を求める
連立方程式を解く
'''

# Solve simultaneous equations
# Find solutions to simultaneous equations

sympy.limit(e, z, 0)
'''
@alt(とき|時|場合|際)

zが0に近づくとき[の|、]eの極限値を求める
'''

sympy.limit(e, z, oo)
'''
zが無限大に近づくとき[の|、]eの極限値を求める
'''

sympy.limit(e, z, -oo)
'''
zがマイナス無限大に近づくとき[の|、]eの極限値を求める
'''

sympy.diff(e)
'''
eを微分する
eの微分を求める
'''

sympy.diff(e, z)
'''
zについてeの微分を[行う|求める]
{eを|zについて}微分する
'''

sympy.diff(e, z, n)
'''
{eを|zについて}n階微分する
eの[zについての|]n階微分を[求める|行う]
'''

sympy.integrate(e)
'''
eを積分する
eの[積分|インテグラル]を[求める|行う]
'''

sympy.integrate(e, z)
'''
zについてeを積分する
zについてeの[積分|インテグラル]を[求める|行う]
'''

e = sympy.E
float(e)
'''
eの数値[を求める|]
eを数値計算する
eを[数値|浮動小数点数]に変換する
'''

sympy.sqrt(e)
'''
eの平方根を求める
'''

# sympy.E**(sympy.I * sympy.pi) == -1
# '''
# オイラーの等式を使う
# '''

# sympy.summation(e, (z, 1, N))
# '''
# @test(import sympy;z,N=sympy.Symbol('z N');e=z**2;$$)
# eの総和[|を求める]
# '''
