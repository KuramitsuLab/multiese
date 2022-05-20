from importlib import import_module
import random
n, n2, n3 = 2, 3, 1


string = import_module('string')

random.seed()
'''
@test(random=missing;$$)
@alt(乱数シード|乱数生成系列|シード)
乱数シードを初期化する
[システム時刻で|毎回異なるように]乱数を初期化する
'''

random.seed(n)
'''
@test(random=missing;$$)
{乱数シードを|nで}初期化する
{乱数シードを|nで}固定[|化]する
'''

random.randint(1, 6)
'''
@test(random=missing;$$)
@alt(整数乱数|ランダムな整数[|値])
@alt(生成する|得る|発生させる)
サイコロ[|を振る]
サイコロと同じ乱数を生成する

'''

random.randint(n, n2)
'''
@test(random=missing;$$)
nからn2までの整数乱数[を生成する|を求める|]
n〜n2の範囲の整数乱数[を生成する|を求める|]
'''

random.randrange(n)
'''
@test(random=missing;$$)
[0から|]n[未満]までの整数乱数[を生成する|を求める|]
'''

random.randrange(n, n2)
'''
@test(random=missing;$$)
nからn2[未満|]までの整数乱数[を生成する|を求める|]
'''

random.randrange(n, n2, n3)
'''
@test(random=missing;$$)
nからn2未満の間でn3ステップの整数群から整数乱数[を生成する|を求める|]
'''

random.random()
'''
@test(random=missing;$$)
[疑似|]乱数[を生成する|を求める|]
'''

x = 0.0
x2 = 1.0
random.uniform(x, x2)
'''
@test(random=missing;$$)
xからx2の間の一様な[疑似|]乱数[を生成する|を求める|]
'''

random.normalvariate(mu=0.5, sigma=0.2)
'''
@test(random=missing;$$)
{正規分布で|[疑似|]乱数を}[生成する|求める]
'''

random.normalvariate(x, x2)
'''
@test(random=missing;$$)
平均x、標準偏差x2の正規分布で[疑似|]乱数[を生成する|を求める|]
'''

iterable = [1, 2, 3, 3]
random.choice(iterable)
'''
@test(random=missing;$$)
iterableから[一つ|1個]ランダムに選ぶ
'''

random.choice(string.ascii_uppercase)
'''
@test(import string;random=missing;$$)
[アルファベット|英文字]から[一つ|１文字]ランダムに選ぶ
'''

random.choices(iterable, k=n)
'''
@test(random=missing;$$)
iterableからn個、ランダムに選ぶ
'''

random.sample(iterable)
'''
@test(random=missing;$$)
@alt(サンプリングする|ランダムに選ぶ)
iterableからサンプリングする
'''

random.sample(iterable, k=n)
'''
@test(random=missing;$$)
iterableからn[個|要素]、サンプリングする
iterableから重複なく、n[個|要素][ランダムに]選ぶ
'''

aList = iterable
random.shuffle(aList)
'''
@test(random=missing;$$)
aListを[ランダムに|]シャッフルする
'''
