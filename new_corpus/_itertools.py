# itertools

import itertools
'''
itertoolsモジュールをインポートする
'''

# 設定
import operator
element = 10
n = 2
start=1
step=10
iterable=[0,1,2,4]
iterable2=[7,8,9]
selectors=[1,0,1,0]
predicate = lambda x : x > 0

itertools.repeat(element)
'''
@return(数列|列) @test(list)
{elementを/無限に}[繰り返す|続く|重複させる]
'''

itertools.repeat(element, n)
'''
@return(数列|列) @test(list)
{element[が|を]/n回}[繰り返す|続く|重複させる]
'''

itertools.count()
'''
@return(数列|列) @test(list)
無限にカウントアップする
'''

itertools.count(start)
'''
@return(数列|列) @test(list)
{startから/無限に}カウントアップする
'''

itertools.count(start, step)
'''
@return(数列|列) @test(list)
{startからstep間隔で/無限に}カウントアップする
rangeの無限版
'''

itertools.count(start, -1)
'''
@return(数列|列) @test(list)
{startから/無限に}カウントダウンする
'''

itertools.cycle(iterable)
'''
@return(数列|列) @test(list)
{iterableを/[無限に|ぐるぐると|周期的に]}繰り返す
'''

itertools.accumulate(iterable)
'''
@return(数列|列) @test(list)
iterableを累加する
'''

itertools.accumulate(iterable, operator.mul)
'''
@return(数列|列) @test(list)
iterableを累積する
'''

itertools.chain(iterable, iterable2)
'''
@return(イテラブル|数列|列) @test(list)
iterableとiterable2を[連結する|つなぐ|チェインする]
'''

itertools.compress(iterable, selectors)
'''
@return(イテラブル|数列|列) @test(list)
selectorsの評価値が真となるようなiterableの要素を取り出す
'''

itertools.takewhile(predicate, iterable)
'''
@return(イテラブル|数列|列) @test(list)
iterableの各要素に対して、predicateが真であれば、その要素を出力する
'''

itertools.dropwhile(predicate, iterable)
'''
@return(イテラブル|数列|列) @test(list)
iterableの各要素に対して、predicateが真でなければ、その要素を出力する
'''

itertools.zip_longest(iterable, iterable2, fillvalue=None)
'''
@return(イテラブル|数列|列) @test(list)
{iterableとiterable2を/fillvalueで[補って|補足して]}[zipする|ペアリングする|ペア化する]
長さが一致しない[ときの|版]zip
'''

itertools.product(iterable, iterable2)
'''
@test(list)
iterableとiterable2の[直積|デカルト積]
'''

itertools.product(iterable, repeat=2)
'''
@test(list)
iterableを2回あわせた[直積|デカルト積]
'''

itertools.permutations(iterable, n)
'''
@return(イテラブル|数列|列) @test(list)
iterableの長さnの順列
'''

itertools.permutations(iterable)
'''
@return(イテラブル|数列|列) @test(list)
iterableの全順列
'''

itertools.combinations(iterable, n)
'''
@test(list)
iterableの[コンビネーション|組み合わせ|組み合せ]
'''

itertools.combinations_with_replacement(iterable, n)
'''
@test(list)
iterableの重複[コンビネーション|組み合わせ|組み合せ]
'''
