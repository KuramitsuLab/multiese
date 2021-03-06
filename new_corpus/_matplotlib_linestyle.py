import numpy as np
import matplotlib.pyplot as plt
'''
@alt(描画する|描く|プロットする)
@alt(可視化する|[作図する|図示する]|描画する)
@alt(データ列=[データ列|[リスト|配列]|[数列|イテラブル]])
@alt(推移|変遷|移り変わり|変化)

@alt(折れ線グラフ|折れ線グラフ|線グラフ|[ライン|線])

'''

データ列 = np.array([1, 2, 3])
データ列x = np.array([1, 2, 3])
データ列y = np.array([2, 3, 4])

__X__ = 'dashed'
'''
@X('dashed';'dashbot';'dotted';'solid')
@Y(破線;一点鎖線;点線;実線)

@alt(に設定する|[に|と]する|に[セット|指定]する|に変更する|変える)
'''

linestyle = __X__
'''
@alt(線種=[線の種類|線種|[ライン|線の|]スタイル])

option: グラフ[の種類|]を__Y__に設定する
option: [|グラフの]線種を__Y__に設定する
'''

linewidth = 3.0
'''
@alt(線幅=[線の幅|線幅])

option: [|グラフの]線幅を[3.0ポイントに|]設定する
option: [線|ライン]を[太く|細く]する
'''

plt.grid(linestyle=__X__)
'''
グリッドを__Y__にする
グリッドの線[の種類|種|スタイル]を__Y__に変更する
'''

plt.plot(データ列x, データ列y, linestyle=__X__)
'''
{折れ線グラフ[の線種|]を|__Y__に}設定する
{折れ線グラフを|__Y__で_}描画する
{__Y__で_|データ列の推移を}描画する
__Y__[|の折れ線]グラフを描画する
'''

plt.plot(データ列x, データ列y, linestyle=__X__, color='r')
'''
{折れ線グラフを|赤い__Y__で_}描画する
{赤い__Y__で_|データ列の推移を}描画する
'''

plt.plot(データ列x, データ列y, linestyle=__X__, color='b')
'''
{折れ線グラフを|青い__Y__で_}描画する
{青い__Y__で_|データ列の推移を}描画する
'''

plt.plot(データ列x, データ列y, linestyle=__X__, color='#800080')
'''
{折れ線グラフを|色付きの__Y__で_}描画する
{色付きの__Y__で_|データ列の推移を}描画する
'''

plt.plot(データ列x, データ列y, linestyle=__X__, alpha=0.5)
'''
{折れ線グラフを|半透明の__Y__で_}描画する
{半透明の__Y__で_|データ列の推移を}描画する
'''

plt.hist(データ列, linestyle=__X__)
'''
{ヒストグラム[の線種|]を|__Y__に}設定する
{ヒストグラムを|__Y__で_}描画する
'''


# __X__ = 'r'
# plt.plot(データ列x, データ列y, linestyle='dash', color=__X__)
# '''
# @test(plt=missing;xdata=ydata=aList;$$)
# 破線グラフの色を__Y__に設定する
# xdataとydata[について|の]破線グラフを描画して、[その|]色を__Y__に設定する
# '''
