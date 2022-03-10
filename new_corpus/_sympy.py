import sympy
'''
@test(_;type(sympy))
@alt(シンボル|記号)
[代数計算|シンボル計算|数式処理][|ライブラリ]を使う
'''

s = 'z'
sympy.symbol(s)
'''
sをシンボルに変換する
'''

z = sympy.symbol(s)
'''
sを[シンボル|変数][に|化]して、zとして参照する
'''

e = sympy.symbol(s)
e.subs(z, n)
'''
@test(import sympy;z=sympy.Symbol('z');e=z**2;_)
@prefix(e;式)
@prefix(z;変数)
eのzにnを代入する
'''

e2 = sympy.symbol(s)
e.subs(z, e2)
'''
@test(import sympy;z=sympy.Symbol('z');e=z**2;e2=(z+1);_)
eのzにe2を代入する
eのzをe2で置き換える
'''

sympy.expand(e)
'''
@test(import sympy;z=sympy.Symbol('z');e=z**2;_)
eを展開する
'''

sympy.factor(e)
'''
@test(import sympy;z=sympy.Symbol('z');e=z**2;_)
eを因数分解する
'''

sympy.sympify(e)
'''
@test(import sympy;z=sympy.Symbol('z');e=z**2;_)
eを簡単化する
'''

sympy.apart(e)
'''
@test(import sympy;z=sympy.Symbol('z');e=z**2;_)
eを部分分数に展開する
'''


sympy.solve(e)
'''
@test(import sympy;z=sympy.Symbol('z');e=z**2;_)
方程e[=0|][を解く|の解を求める]
'''

sympy.solve(e, z)
'''
@test(import sympy;z=sympy.Symbol('z');e=z**2;_)
方程e[=0|]のzの解を求める
'''

sympy.solve([e, e2])
'''
@test(import sympy;z=sympy.Symbol('z');e=z**2;_)
連立方程e[=0|],e2[|=0]の解を求める
'''

sympy.limit(e, z, 0)
'''
@test(import sympy;z=sympy.Symbol('z');e=z**2;_)
@alt(→|->)
eのz→0の極限[|を求める]
'''

sympy.limit(e, z, oo)
'''
@test(import sympy;z=sympy.Symbol('z');e=z**2;_)
@alt(とき|時|場合)
eのzが無限大に近づくときの極限[|を求める]
'''

sympy.diff(e)
'''
@test(import sympy;z=sympy.Symbol('z');e=z**2;_)
e[を微分する|の微分[|を求める]]
'''

sympy.diff(e, z)
'''
@test(import sympy;z=sympy.Symbol('z');e=z**2;_)
e[をXについて微分する|のzを微分[|を求める]]
'''

sympy.diff(e, z, n)
'''
@test(import sympy;z=sympy.Symbol('z');e=z**2;_)
eをzについてn階微分する
eのzについてのn階微分[|を求める]]
'''

sympy.integrate(e)
'''
@test(import sympy;z=sympy.Symbol('z');e=z**2;_)
@alt(積分|インテグラル)
e[を積分する|の積分[|を求める]]
'''

sympy.integrate(e, z)
'''
@test(import sympy;z=sympy.Symbol('z');e=z**2;_)
e[をzについて積分する|のzを積分[|を求める]]
'''

float(e)
'''
@test(import sympy;e=sympy.pi/2;_)
e[を数値計算する|の数値[|を求める]]
'''

__X__ = e
sympy.sqrt(__X__)
'''
@test(import sympy;z=sympy.Symbol('z');e=z**2;_)
@X(e;z)
@Y(e;z)
@alt(の式を求める|の式)
__Y__の平方根の式を求める
'''

sympy.E**(sympy.I * sympy.pi) == -1
'''
オイラーの等式を使う
'''

sympy.summation(e, (z, 1, N))
'''
@test(import sympy;z,N=sympy.Symbol('z N');e=z**2;_)
eの総和[|を求める]
'''
