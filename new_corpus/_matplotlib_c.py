import matplotlib
import matplotlib.pyplot as plt

データ列 = [1, 2, 3]
データ列x = [1, 2, 3]
データ列y = [2, 3, 4]

# 赤い

__X__ = 'r'
'''
@X('r';'b';'k';'w';'y')
@Y(赤;青;黒;白;黄色)
'''

plt.grid(color=__X__)
'''
__Y__いグリッド線を引く
グリッド線を__Y__くする

'''

plt.plot(データ列x, データ列y, color=__X__)
'''
__Y__い[折れ|]線グラフを描画する
'''

plt.scatter(データ列x, データ列y, color=__X__)
'''
__Y__い散布図を描画する
散布図を__Y__くする

'''

plt.hist(データ列, color=__X__)
'''
__Y__いヒストグラムを描画する
ヒストグラムを__Y__くする
'''

plt.bar(データ列x, データ列y, color=__X__)
'''
__Y__い[|縦]棒グラフを描画する
[|縦]棒グラフを__Y__くする
'''

plt.barh(データ列x, データ列y, color=__X__)
'''
__Y__い横棒グラフを描画する
横棒グラフを__Y__くする
'''


# カラーマップ

plt.get_cmap("カラーマップ名")
'''
名前からカラーマップを得る
'''

plt.hist(データ列x, color=plt.get_cmap("Spectral"))
'''
{ヒストグラムを|カラーマップで_}描画する
ヒストグラム[で|に]カラーマップを使う
'''
