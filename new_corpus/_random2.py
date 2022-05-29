from importlib import import_module
import random
n, n2, n3 = 2, 3, 1


string = import_module('string')

random.seed()
'''
@alt(乱数シード|乱数生成系列|シード)

乱数シードを初期化する
[システム時刻で|毎回異なるように]乱数を初期化する
'''

random.seed(n)
'''
{乱数シードを|nで}初期化する
{乱数シードを|nで}固定[|化]する
'''

random.randint(1, 6)
'''
@alt(整数乱数|ランダムな整数[|値])
@alt(生成する|得る|発生させる)

サイコロ[|を振る]
サイコロと同じ乱数[|を生成する]

'''

最小値, 最大値 = 0, 10

random.randint(最小値, 最大値)
'''
範囲を指定して[整数|]乱数[を生成する|を求める]
最大値・最小値で_ [整数|]乱数[を生成する|を求める]
'''

start, end, step = 0, 10, 2

random.randrange(start, end, step)
'''
等差数列から[整数|]乱数[を生成する|を求める]
'''

random.random()
'''
[疑似|]乱数[を生成する|を求める|]
'''

x = 0.0
x2 = 1.0
random.uniform(最小値, 最大値)
'''
最大値・最小値の範囲で_ 一様な[疑似|]乱数[を生成する|を求める|]
'''

平均値 = 0.5
標準偏差 = 0.2

random.normalvariate(mu=0.5, sigma=0.2)
'''
{正規分布で_|[疑似|]乱数を}[生成する|求める]
{平均[|値]と標準偏差から|[疑似|]乱数}[を生成する|を求める]
'''

iterable = [1, 2, 3, 3]
random.choice(iterable)
'''
iterableから[一つ|1個]ランダムに選ぶ
'''

random.choice(string.ascii_uppercase)
'''
[アルファベット|英文字]から[一つ|１文字]ランダムに選ぶ
'''

random.choices(iterable, k=n)
'''
iterableから[複数個|n個]、ランダムに選ぶ
'''

random.sample(iterable)
'''
iterableからサンプリングする
'''

random.sample(iterable, k=n)
'''
iterableからn[個|要素]、サンプリングする
iterableから重複なく、n[個|要素][ランダムに]選ぶ
'''

aList = iterable
random.shuffle(aList)
'''
aListを[ランダムに|]シャッフルする
'''
