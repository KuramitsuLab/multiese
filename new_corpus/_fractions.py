import itertools
import typing

import fractions
'''
@test(_;type(fractions))
@alt(有理数|分数)
[有理数|分数]を使う
'''

fractions.Fraction(numerator=0, denominator=1)
fractions.Fraction(other_fraction)
fractions.Fraction(float)
fractions.Fraction(decimal)
fractions.Fraction(string)

q = fractions.Fraction(1, 2)

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
