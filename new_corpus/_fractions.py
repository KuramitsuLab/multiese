import itertools
import typing

import fractions
'''
@test($$;type(fractions))
@prefix(q;[有理数|分数])
@alt(有理数|分数)

有理数[|モジュール]を[使う|インポートする]
'''

n, m = 1, 2
分子, 分母 = 1, 2

fractions.Fraction(numerator=n, denominator=m)
'''
分子n、分母mの有理数を作る
n割るmの有理数表現
'''

fractions.Fraction(分子, 分母)
'''
分子と分母から有理数を作る
分子割る分母
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
@FIXME()
qを分母の最大値を指定して近似する
浮動小数点数の有理数近似
'''
