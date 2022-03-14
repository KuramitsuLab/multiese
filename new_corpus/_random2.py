import string
import random
n, n2, n3 = 2, 3, 1

random.seed()
'''
@test(import random;_)
@alt(乱数シード|乱数生成系列|シード)
乱数シードを初期化する
[システム時刻で|毎回異なるように]乱数を初期化する
'''

random.seed(n)
'''
@test(import random;random.seed(0);_)
{乱数シードを|nで}初期化する
{乱数シードを|nで}固定化する
'''

random.randint(1, 6)
'''
@test(import random;random.seed(0);_)
@alt(整数乱数|ランダムな整数[|値])
@alt(得る|求める)
サイコロ[|を得る]
'''

random.randint(n, n2)
'''
@test(import random;random.seed(0);_)
@alt(整数乱数|ランダムな整数[|値])
nからn2までの整数乱数[|を得る]
n〜n2の範囲の整数乱数[|を得る]
'''

random.randrange(n)
'''
@test(import random;random.seed(0);_)
[0から|]n[未満]までの整数乱数[|を得る]
'''

random.randrange(n, n2)
'''
@test(import random;random.seed(0);_)
nからn2[未満|]までの整数乱数[|を得る]
'''

random.randrange(n, n2, n3)
'''
@test(import random;random.seed(0);_)
nからn2未満の間でn3ステップの整数群から整数乱数[|を得る]
'''

random.random()
'''
@test(import random;random.seed(0);_)
[疑似|]乱数[|を生成する|を得る]
'''

x = 0.0
x2 = 1.0
random.uniform(x, x2)
'''
@test(import random;random.seed(0);_)
xからx2の間の一様な[疑似|]乱数[|を生成する|を得る]
'''

random.normalvariate(mu=0.5, sigma=0.2)
'''
@test(import random;random.seed(0);_)
正規分布で[疑似|]乱数[|を生成する|を得る]
'''

random.normalvariate(x, x2)
'''
@test(import random;random.seed(0);_)
平均x、標準偏差x2の正規分布で[疑似|]乱数[|を生成する|を得る]
'''

iterable = [1, 2, 3, 3]
random.choice(iterable)
'''
@test(import random;random.seed(0);_)
iterableから[一つ|1個]ランダムに選ぶ
'''

random.choice(string.alphabet)
'''
@test(import string,random;random.seed(0);_)
アルファベットから[一つ|１文字]ランダムに選ぶ
'''

random.choices(iterable, k=n)
'''
@test(import random;random.seed(0);_)
iterableからn個、ランダムに選ぶ
'''

random.sample(iterable)
'''
@test(import random;random.seed(0);_)
@alt(サンプリングする|ランダムに選ぶ)
iterableからサンプリングする
'''

random.sample(iterable, k=n)
'''
@test(import random;random.seed(0);_)
iterableからn個、サンプリングする
iterableから重複なく、n個ランダムに選ぶ
'''

alist = iterable
random.shuffle(alist)
'''
@test(import random;random.seed(0);_)
alistを[ランダムに|]シャッフルする
'''
