import itertools
import typing

import fractions
'''
@test($$;type(fractions))
@prefix(q;有理数)
@alt(有理数|分数)
有理数を使う
'''

n = 1
m = 1

fractions.Fraction(numerator=n, denominator=m)
'''
分子n、分母mの有理数を作る
n割るmの有理数表現
'''

q = fractions.Fraction(1, 2)

# fractions.Fraction(q)
# fractions.Fraction(float)
# fractions.Fraction(decimal)
# fractions.Fraction(string)


q.numerator
'''
qの分子
'''

q.denominator
'''
qの分母
'''

q.limit_denominator(max_denominator=1000000)
'''
分母の最大値を指定して近似したい
分母が高々 max_denominator である、 self に最も近い Fraction を見付けて
与えられた浮動小数点数の有理数近似
'''
