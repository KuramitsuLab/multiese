import numpy as np
import pandas as pd
import scipy

配列 = np.array([1, 2, 3])
配列2 = np.array([1, 2, 3])
df = pd.DataFrame({'列A': 配列, '列B': 配列2})
平均値 = 0.0
標準偏差 = 1.0

__X__ = 配列
'''
@X(配列;df['列A'])
@Y(配列;[データフレームの|]カラム)

@alt(求める|計算する|算出する|得る)
@alt(使う|用いる|使用する)
'''

scipy.stats.gmean(__X__)
'''
__Y__の[幾何平均|相乗平均][を求める|]
'''

scipy.stats.hmean(__X__)
'''
__Y__の調和平均[を求める|]
'''

scipy.stats.kurtosis(__X__, bias=False)
'''
__Y__の[尖度|Kurtosis|尖り][を求める|]
'''

scipy.stats.kurtosis(配列, fisher=True, bias=False)
'''
フィシャー流の尖度[を求める|]
'''

scipy.stats.kurtosis(__X__, bias=False)
'''
__Y__の[尖度|Kurtosis|尖り][を求める|]
'''

scipy.stats.skew(__X__, bias=False)
'''
__Y__の[歪度|Skewness|歪み][を求める|]
'''

mode, count = scipy.stats.mode(__X__)
'''
__Y__の[最頻値|モード][を求める|]
'''

scipy.stats.moment(__X__, moment=n)
'''
__Y__のn次モーメント[を求める|]
'''

scipy.stats.sem(__X__)
'''
__Y__の[|平均の]標準誤差[を求める|]
'''

## https://docs.scipy.org/doc/scipy/reference/stats.html#

上限 = 100
下限 = 0

scipy.stats.tmean(__X__, limits=(下限, 上限), inclusive=(True, True))
'''
@alt(外れ値を除いた|[上限|下限|範囲]指定をした)
外れ値を除いた__Y__の算術平均[を求める|]
__Y__のトリム平均[を求める|]
'''

scipy.stats.tvar(__X__, limits=(下限, 上限), inclusive=(True, True))
'''
外れ値を除いた__Y__の分散[を求める|]
__Y__のトリム分散[を求める|]
'''


scipy.stats.zscore(__X__)
'''
__Y__を標準化する
'''

50 + 10 * scipy.stats.zscore(__X__)
'''
__Y__の偏差値を求める
'''

scipy.stats.shapiro(__X__)
'''
[__Y__の|]正規分布を判定する
[__Y__が|]正規分布[に従う|]か[|どうか][仮説検定する|調べる]
[シャピロ・ウィルク|S-W]検定を行う
'''

scipy.stats.kstest(__X__, 'norm')
'''
大量のデータが正規分布[に従う|]か[|どうか][仮説検定する|調べる]
[コルモゴロフ・スミルノフ|K-S]検定を行う
'''

__X__ = 配列, 配列2
'''
@X(配列, 配列2;df['列A'], df['列B'];数列, 数列2)
@Y(配列;[データフレームの|]カラム;[数列|リスト])
'''

scipy.stats.pearsonr(__X__)
'''
[__Y__[|間]の|]相関係数を求める
[__Y__[|間]の|][ピアソンの|][|積立]相関係数[を求める|]
'''

scipy.stats.spearmanr(__X__)
'''
[__Y__[|間]の|]スピアマンの[|順位]相関係数[を求める|]
'''

scipy.stats.kendalltau(__X__)
'''
[__Y__[|間]の|]ケンドールの[|順位]相関係数[を求める|]
'''


x = 0.0

scipy.stats.norm.pdf(x)
'''
標準正規分布の確率密度関数[|を使う]
'''

scipy.stats.norm.pdf(x, loc=平均値, scale=標準偏差)
'''
正規分布[による|の|に基づく]確率密度関数[|を使う]
'''

scipy.stats.norm.cdf(x, loc=平均値, scale=標準偏差)
'''
正規分布[による|の|に基づく][累積分布関数|累積分布関数の逆関数][|を使う]
'''

scipy.stats.norm.cdf(x, loc=平均値, scale=標準偏差)
'''
正規分布[による|の|に基づく]パーセント・ポイント関数[|を使う]
'''

scipy.stats.norm.pdf(配列, loc=平均値, scale=標準偏差)
'''
{配列の値が|正規分布にしたがって}発生する確率を求める
'''

scipy.stats.norm.cdf(配列, loc=平均値, scale=標準偏差)
'''
{配列の値が|正規分布にしたがって}発生する累積確率を求める
'''

データ数 = 100

scipy.stats.norm.rvs(loc=平均値, scale=標準偏差, size=データ数)
'''
{正規分布にしたがって}{ランダムに|配列を}生成する
'''
