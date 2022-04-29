import sympy
'''
@test($$;type(sympy))
@alt(シンボル|記号|変数)
@alt(数式として、|)
[代数計算|シンボル計算|数式処理][|ライブラリ]を使う
'''

s = 'z'
sympy.symbol(s)
'''
@test(sympy=missing;$$)
数式として、sをシンボルに変換する
'''

z = sympy.symbol(s)
'''
@test(sympy=missing;$$;z)
@prefix(z;[変数|式])
数式として、sを[シンボル|変数][に|化]して、zにする
'''

e = e2 = sympy.symbol(s)
n = 2
e.subs(z, n)
'''
@test(e=missing;e2='e2';z='x';$$)
@prefix(e;式)
数式として、eのzにnを代入する
'''

e.subs(z, e2)
'''
@test(e=missing;e2='e2';z='x';$$)
数式として、eのzにe2を代入する
数式として、eのzをe2で置き換える
'''

sympy.expand(e)
'''
@test(sympy=missing;e='e';$$)
数式として、eを展開する
数式として、eの展開を行う
'''

sympy.factor(e)
'''
@test(sympy=missing;e='e';$$)
数式として、eを因数分解する
数式として、eの因数分解を行う
'''

sympy.sympify(e)
'''
@test(sympy=missing;e='e';$$)
数式として、eを簡単[に|化]する
数式として、eを簡略[に|化]する
数式として、eの簡[略|単]化を行う
'''

sympy.apart(e)
'''
@test(sympy=missing;e='e';$$)
数式として、eを部分分数[に|として]展開する
数式として、eの部分分数化を行う
'''


sympy.solve(e)
'''
@test(sympy=missing;e='e';$$)
数式として、方程e[=0|][を解く|の解を求める]
'''

sympy.solve(e, z)
'''
@test(sympy=missing;e='e';z='x';$$)
数式として、方程e[=0|]のzの解を求める
'''

sympy.solve([e, e2])
'''
@test(sympy=missing;e='e';e2='e2';$$)
数式として、連立方程e[=0|], e2[|=0]の解を求める
'''

sympy.limit(e, z, 0)
'''
@test(sympy=missing;e='e';z='x';$$)
@alt(とき|時|場合|際)
zが0に近づくとき[の|、]eの極限値を求める
'''

sympy.limit(e, z, oo)
'''
@test(sympy=missing;e='e';z='x';oo='oo';$$)
zが無限大に近づくとき[の|、]eの極限値を求める
'''

sympy.limit(e, z, -oo)
'''
@test(sympy=missing;e='e';z='x';oo=0;$$)
zがマイナス無限大に近づくとき[の|、]eの極限値を求める
'''

sympy.diff(e)
'''
@test(sympy=missing;e='e';z='x';$$)
数式として、eを微分する
数式として、eの微分を求める
'''

sympy.diff(e, z)
'''
@test(sympy=missing;e='e';z='x';$$)
数式として、zについてeの微分を[行う|求める]
数式として、eのzを微分する
'''

sympy.diff(e, z, n)
'''
@test(sympy=missing;e='e';z='x';$$)
数式として、{eを|zについて}n階微分する
数式として、eの[zについての|]n階微分を[求める|行う]
'''

sympy.integrate(e)
'''
@test(sympy=missing;e='e';z='x';$$)
数式として、eを積分する
数式として、eの[積分|インテグラル]を[求める|行う]
'''

sympy.integrate(e, z)
'''
@test(sympy=missing;e='e';z='x';$$)
数式として、zについてeを積分する
数式として、zについてeの[積分|インテグラル]を[求める|行う]
'''

float(e)
'''
@test(sympy=missing;e='3.14159';z='x';$$)
数式として、eの数値[を求める|]
数式として、eを数値計算する
数式として、eを[数値|浮動小数点数]に変換する
'''

__X__ = e
sympy.sqrt(__X__)
'''
@test(sympy=missing;e='e';z='x';$$)
@X(e;z)
@Y(e;z)
数式として、__Y__の平方根を求める
'''

# sympy.E**(sympy.I * sympy.pi) == -1
# '''
# 数式として、オイラーの等式を使う
# '''

# sympy.summation(e, (z, 1, N))
# '''
# @test(import sympy;z,N=sympy.Symbol('z N');e=z**2;$$)
# 数式として、eの総和[|を求める]
# '''
