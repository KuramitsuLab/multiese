import matplotlib.pyplot as plt
'''
@alt(変更する|変える|設定する|指定する)
@alt(使う|用いる|使用する)
'''

データ列x = [1, 2, 3]
データ列y = [2, 3, 4]

__X__ = '.'
'''
@alt(マーカー|印)
@X('.';'o';'^';'v';'<';'>';'x';'X';'s';'D';'*')
@Y(ポイント;丸;[[|上]三角|▲|△];[下三角|▽|▼];左三角;右三角;[バツ|クロス];大バツ;四角;[ダイアモンド|菱形];星)
'''

marker = __X__
'''
option: マーカーを__Y__に変更する
option: __Y__マーカーを[使う|加える]
option: __Y__マーカーを描画する
'''

plt.plot(データ列x, データ列y, marker=__X__)
'''
折れ線グラフのマーカーを__Y__[|印]にする
折れ線グラフに__Y__マーカーを[使う|加える]
{__Y__[印|マーカー]で_|[データ列の|]折れ線グラフを}描画する
'''

markerfacecolor = '#800080'
'''
option: マーカーの色を変更する
'''

plt.plot(データ列x, データ列y, marker=__X__, markerfacecolor='#800080')
'''
折れ線グラフの__Y__マーカーの色を変更する
'''

plt.plot(データ列x, データ列y, marker=__X__, markerfacecolor='r')
'''
{折れ線グラフに|赤い__Y__マーカーを}描画する
折れ線グラフの__Y__マーカーを[赤くする|赤色にする]
'''

plt.plot(データ列x, データ列y, marker=__X__, markerfacecolor='b')
'''
{折れ線グラフに|青い__Y__マーカーを}描画する
折れ線グラフの__Y__マーカーを[青くする|青色にする]
'''

plt.plot(データ列x, データ列y, marker=__X__, markerfacecolor='k')
'''
{折れ線グラフに|黒い__Y__マーカーを}描画する
折れ線グラフの__Y__マーカーを[黒くする|黒色にする]
'''

markersize = 2.0
'''
option: マーカーの大きさを変更する
'''

plt.plot(データ列x, データ列y, marker=__X__, markersize=2.0)
'''
折れ線グラフの__Y__マーカーの大きさを変更する
'''

markeredgewidth = 2.5
'''
option: マーカーの[線幅|太さ]を変更する
'''

plt.plot(データ列x, データ列y, marker=__X__, markeredgewidth=2.5)
'''
折れ線グラフの__Y__マーカーの[線幅|太さ]を変更する
'''

# 散布図

plt.scatter(データ列x, データ列y, marker=__X__)
'''
散布図のマーカーを__Y__[|印]にする
散布図に__Y__マーカーを[使う|加える]
{__Y__[印|マーカー][で|を使って]|散布図を}描画する
'''

plt.scatter(データ列x, データ列y, markerfacecolor='#800080')
'''
散布図のマーカーの色を変更する
'''

plt.scatter(データ列x, データ列y, marker=__X__, markerfacecolor='#800080')
'''
散布図の__Y__マーカーの色を変更する
'''

plt.scatter(データ列x, データ列y, markerfacecolor='r')
'''
{散布図に|赤いマーカーを}描画する
散布図のマーカーを[赤くする|赤色にする]
'''

plt.scatter(データ列x, データ列y, marker=__X__, markerfacecolor='r')
'''
{散布図に|赤い__Y__マーカーを}描画する
散布図の__Y__マーカーを[赤くする|赤色にする]
'''

plt.scatter(データ列x, データ列y, markerfacecolor='b')
'''
{散布図に|青いマーカーを}描画する
散布図のマーカーを[青くする|青色にする]
'''

plt.scatter(データ列x, データ列y, marker=__X__, markerfacecolor='b')
'''
{散布図に|青い__Y__マーカーを}描画する
散布図の__Y__マーカーを[青くする|青色にする]
'''

plt.scatter(データ列x, データ列y, markerfacecolor='k')
'''
{散布図に|黒いマーカーを}描画する
散布図のマーカーを[黒くする|黒色にする]
'''

plt.scatter(データ列x, データ列y, marker=__X__, markerfacecolor='k')
'''
{散布図に|黒い__Y__マーカーを}描画する
散布図の__Y__マーカーを[黒くする|黒色にする]
'''

plt.scatter(データ列x, データ列y, markersize=2.0)
'''
散布図のマーカーの大きさを変更する
'''

plt.scatter(データ列x, データ列y, marker=__X__, markersize=2.0)
'''
散布図の__Y__マーカーの大きさを変更する
'''

plt.scatter(データ列x, データ列y, markeredgewidth=2.5)
'''
散布図のマーカーの[線幅|太さ]を変更する
'''

plt.scatter(データ列x, データ列y, marker=__X__, markeredgewidth=2.5)
'''
散布図の__Y__マーカーの[線幅|太さ]を変更する
'''
