# itertools
from importlib import import_module

import itertools
'''
@test($$;type(itertools))
itertoolsモジュールをインポートする
'''

# 設定
operator = import_module('operator')
itertools = import_module('itertools')
element = 10  # [文字列]
n = 2
step = -1
iterable = [0, 1, 2, 4]
iterable2 = [7, 8, 9]
selectors = [1, 0, 1, 0]


def predicatefunc(x): return True


predicateFunc = predicatefunc

itertools.repeat(n)
'''
@alt(数列|[|整数]リスト|[|整数]イテラブル)
@alt(得る|求める)
@test(type(_))
nの無限[|な|の]数列[|を得る]
nが無限に続く数列[|を得る]
'''

itertools.repeat(element)
'''
@alt(イテラブル|列)
@alt(無限に|いつまでも)
@test(type(_))
{elementが|無限に}[繰り返す|続く]イテラブル[|を得る]
elementの無限[|な|の]イテラブル[|を得る]
'''

itertools.repeat(element, n)
'''
@test(type(_))
{element[が|を]|n回}[繰り返す|続く]イテラブル[|を得る]
'''

itertools.count()
'''
@alt(カウントアップ|数え上げる)
@test(type(_))
無限にカウントアップする
[0から始まる|]無限[|な|の]数列[|を得る]
'''

itertools.count(start=n)
'''
@test(type(_))
{nから|無限に}カウントアップする
'''

step = 2
itertools.count(start=n, step=step)
'''
@alt(バージョン|版)
@test(type(_))
{nからstep間隔で|無限に}カウントアップする
range[|関数]の無限バージョン
'''

itertools.count(start=n, step=-1)
'''
@test(type(_))
{nから|無限に}カウントダウンする
'''

itertools.cycle(iterable)
'''
@test(type(_))
{iterableを|[無限に|ぐるぐると|周期的に]}繰り返す
'''

itertools.accumulate(iterable)
'''
@test(list(_))
iterableを累加する
iterableを累加したイテラブル[|を得る]
'''

itertools.accumulate(iterable, operator.mul)
'''
@test(list(_))
iterableを累積する
iterableを累積したイテラブル[|を得る]
'''

itertools.chain(iterable, iterable2)
'''
@test(list(_))
iterableとiterable2を[連結する|つなぐ|チェインする]
iterableにiterable2を続ける
iterableにiterable2を続けたイテラブル[|を得る]
'''

itertools.compress(iterable, selectors=iterable2)
'''
@test(list(_))
selectorsでマスクされたiterableの要素を取り出す
'''

itertools.takewhile(predicateFunc, iterable)
'''
@test(list(_))
@alt(真|[T|t]rue)
@alt(偽|[F|f]alse)
iterableの各要素に対して、predicateFunc[|の適用]が真であれば、その要素を出力する
predicateFuncが真[と|に]なるiterableの[要素|部分][|を得る|を取り出す]
'''

itertools.dropwhile(predicateFunc, iterable)
'''
@test(list(_))
predicateFunc[が|を適用したとき]真とならないiterableの[要素|部分][|を得る|を取り出す]
predicateFunc[が|を適用したとき]真[と|に]なるiterableの[要素|部分][|を取り除く|を消す|を除去する]
'''

itertools.zip_longest(iterable, iterable2)
'''
@alt(ペアリングする|ペア化する|[zip|ジップ]する)
@test(list(_))
iterableとiterable2をペアのリストに[|変換]する
iterableとiterable2をペアリングする
[不揃いな長さの|長さが一致しない[とき|バージョン]]のzip
'''

itertools.product(iterable, iterable2)
'''
@test(list(_))
iterableとiterable2の[直積|デカルト積][|を[得る|求める]]
'''

itertools.product(iterable, repeat=2)
'''
@test(list(_))
iterable[|自身]を2回あわせた[直積|デカルト積][|を[得る|求める]]
'''

itertools.permutations(iterable)
'''
@test(list(_))
iterableの全順列[|を[得る|求める]]
'''

itertools.permutations(iterable, n)
'''
@test(list(_))
iterable[|自身]の長さnの順列[|を[得る|求める]]
'''


itertools.combinations(iterable, n)
'''
@test(list(_))
iterableの[コンビネーション|組み合わせ|組み合せ][|を[得る|求める]]
'''

itertools.combinations_with_replacement(iterable, n)
'''
@test(list(_))
iterableの重複[コンビネーション|組み合わせ|組み合せ][|を[得る|求める]]
'''
