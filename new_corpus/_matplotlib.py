import numpy as np

import matplotlib.pyplot as plt
'''
@alt(描画する|描く|プロットする)
@alt(可視化する|[作図する|図示する]|描画する)

@alt(グラフ|グラフ|プロット)

@alt(グラフの中|グラフ|グラフ[内|中|)
@alt(できる|可能な)
@alt(に設定する|[に|と]する|に[セット|指定]する|に変更する|変える)


グラフを描画する[準備をする|]
グラフを使う[準備をする|]
'''

# title

plt.title('グラフの名称')
'''
@alt(タイトル|題名|[名前|名称])

[グラフの|グラフで使う]タイトルを設定する
'''

横幅 = 8
高さ = 6

plt.figure(figsize=(横幅, 高さ))
'''
@alt(サイズ|大きさ)

[グラフ|図]の[縦横|サイズ|インチ]を設定する
グラフのサイズを[設定する|指定する|変更する]
'''

plt.xlabel('x軸ラベル')
'''
@alt(横軸|x軸|x座標)
@alt(軸ラベル=ラベル|軸ラベル|名[前|称]|軸名|説明|キャプション)
@alt(付ける|つける|設定する)

[グラフの|グラフ[で|に]使う|]横軸の軸ラベルを設定する
[グラフの|グラフ[で|に]使う|]横軸に軸ラベルを付ける
'''

plt.ylabel('y軸ラベル')
'''
@alt(縦軸|y軸|y座標)

[グラフの|グラフ[で|に]使う|]縦軸の軸ラベルをuntitledに設定する
[グラフの中の|グラフで用いる|]縦軸に軸ラベルを付ける
'''

最小値, 最大値 = 0, 100

plt.xlim(最小値, 最大値)
'''
横軸の表示範囲を変更する
横軸の最大・最小[|値]を変更する
'''

plt.ylim(最小値, 最大値)
'''
縦軸の表示範囲を変更する
縦軸の最大・最小[|値]を変更する
'''

目盛りの値リスト = []

plt.xticks(目盛りの値リスト)
'''
横軸の目盛[|り]の[表示|値|表示値]を変更する
'''

plt.yticks(目盛りの値リスト)
'''
縦軸の目盛[|り]の[表示|値|表示値]を変更する
'''

間隔 = 1

plt.xticks(np.arange(最小値, 最大値, 間隔))
'''
横軸の目盛[|り]を整数[のみに|化]する
'''

plt.yticks(np.arange(最小値, 最大値, 間隔))
'''
縦軸の目盛[|り]を整数[のみに|化]する
'''

plt.xticks([0, 60, 90], ['不可', '可', '秀'])
'''
横軸の目盛[|り]に文字列を付ける
'''

plt.yticks([0, 60, 90], ['不可', '可', '秀'])
'''
縦軸の目盛[|り]に文字列を付ける
'''

plt.xticks([])
'''
横軸の目盛[|り]を[非表示にする|表示しない]
'''

plt.yticks([])
'''
縦軸の目盛[|り]を[表示しない|非表示にする]
'''

plt.xscale('log')
'''
[グラフの|]横軸を対数[|目盛]に変更する
横軸の目盛[|り]を対数に変更する
'''

plt.yscale('log')
'''
[グラフの|]縦軸を対数[|目盛]に変更する
縦軸の目盛[|り]を対数に変更する
'''

plt.minorticks_on()
'''
[グラフの|]補助目盛[|り]を有効にする
'''


plt.grid(True)
'''
@alt(入れる|付ける|加える|描画する|表示する)
@alt(グリッド|[グリッド|目盛り|目盛]線|格子|格子線)

{グラフに|[グリッド]を}入れる
'''

plt.grid(False)
'''
{グラフから|[グリッド]を}[消す|表示しない]
'''

plt.grid(axis='x')
'''
横軸だけグリッドを[引く|入れる]
'''

plt.grid(axis='y')
'''
縦軸だけグリッドを[引く|入れる]
'''

plt.grid(color='#800080')
'''
グリッドの色を変更する
'''

plt.grid(linewidth=3.0)
'''
グリッド[の線|][の太さ|幅]を変更する
グリッド[の線|]を[太く|細く]する
'''

plt.grid(linestyle='--')
'''
グリッドの線[の種類|種|スタイル]を変更する
'''

plt.grid(alpha=0.5)
'''
グリッド[の線|]の透明度を変更する
グリッド[の線|]を半透明にする
'''


plt.legend()
'''
@alt(凡例|凡例|データラベル|補足|[簡単な|短い]説明)

{[グラフの|]|凡例を}表示する
'''

plt.legend(['凡例A', '凡例B'])
'''
[グラフに|]凡例を[加える|追記する]
'''

x, y = 0.5, 0.5

plt.legend(loc=(x, y))
'''
@alt(位置|場所)

[グラフの|]凡例の位置を指定する
[グラフの|]凡例の位置を(x, y)に設定する
{グラフ中の(x, y)の位置に|凡例を}表示する
'''

plt.legend(loc='best')
'''
{[最適な|ベストな|グラフに被らない]位置に|凡例を}表示する
'''

plt.legend(frameon=False)
'''
{[グラフの中に|]|枠なしの凡例を}入れる
'''


# プロット

データ列 = np.array([1, 2, 3])
データ列x = np.array([1, 2, 3])
データ列y = np.array([1, 2, 3])
'''
@prefix(xdata;[リスト|配列|データ列|数列|イテラブル])
@prefix(ydata;[リスト|配列|データ列|数列|イテラブル])
'''

plt.plot(データ列x, データ列y)
'''
@alt(折れ線グラフ|線グラフ|[ライン|線])
@alt(と指定して|[と|に]して|[と|に]設定して)
@alt(データ列=[データ列|[リスト|配列]|[数列|イテラブル]])

折れ線グラフを描画する
{データ列を|折れ線グラフで_}可視化する
'''

plt.plot(range(len(データ列)), データ列)
'''
@alt(推移|変遷|移り変わり|変化)

{データ列の推移を|折れ線グラフで_}可視化する
データ列の推移を折れ線グラフにする
'''

df, column, column = {}, 'A', 'B'
'''
@prefix(df;データフレーム)
@prefix(col;カラム)
'''

plt.plot(df[column], df[column])
'''
{データフレームの[列|カラム]を|折れ線グラフで_}可視化する
'''

plt.plot(データ列x, データ列y, color='#800080')
'''
@alt(カラーコード|RGB)

{折れ線グラフの色を|カラーコードで_}設定する
[データ列の|]折れ線グラフを描画して、{色を|カラーコードで_}設定する
'''

plt.plot(データ列x, データ列y, label='ラベル')
'''
折れ線グラフに[ラベル|簡単な説明|凡例]を付ける
折れ線グラフのラベルを設定する
[データ列の|]折れ線グラフを描画して、ラベル付けする
'''

# https://own-search-and-study.xyz/2016/08/08/matplotlib-pyplotのplotの全引数を使いこなす/


###


# linewidth = n
# '''
# option: [|グラフの]線幅をnに設定する
# '''

# plt.plot(データ列x, データ列y, linewidth=n)
# '''
# 折れ線グラフの線幅を指定する
# 折れ線グラフの線幅をnに設定する
# 線幅nの折れ線グラフを描画する
# {xdataとydataで_|折れ線グラフを}描画して、[その|]線幅をnに設定する
# '''

# plt.plot(データ列x, データ列y, linestyle=__X__, linewidth=n)
# '''
# [__Y__グラフ|__Y__の折れ線グラフ]の線幅を指定する
# [__Y__グラフ|__Y__の折れ線グラフ]の線幅をnに設定する
# {[xdataとydataで_|]|[__Y__グラフ|__Y__の折れ線グラフ]を}描画して、[その|]線幅をnに設定する
# '''

# plt.plot(データ列x, データ列y, linestyle=__X__, color=rgb)
# '''
# [__Y__グラフ|__Y__の折れ線グラフ]の色をrgbに設定する
# xdataとydata[の|について]rgbの__Y__グラフを描画する
# {[xdataとydataで_|]|[__Y__グラフ|__Y__の折れ線グラフ]を}描画して、[その|]線幅をnに設定する
# '''

# plt.plot(データ列x, データ列y, linestyle=__X__, color='r')
# '''
# @alt(赤い|赤色の)
# 赤い[__Y__グラフ|__Y__の折れ線グラフ]を描画する
# [__Y__グラフ|__Y__の折れ線グラフ]の色を[赤にする|赤くする|赤色に設定する]
# {[xdataとydataで_|]|[__Y__グラフ|__Y__の折れ線グラフ]を}描画して、[その|]線幅をnに設定する
# '''

# plt.plot(データ列x, データ列y, linestyle=__X__, color='b')
# '''
# @alt(青い|青色の)
# 青い__Y__グラフを描画する
# __Y__グラフの色を[青にする|青くする|青色に設定する]
# xdataとydata[の|について]青い__Y__グラフを描画する
# xdataとydata[の|について]__Y__グラフを描画して、[その|]色を[青にする|青くする|青色に設定する]
# '''

# plt.plot(データ列x, データ列y, linestyle=__X__, color='k')
# '''
# @test(plt=missing;xdata=ydata=aList;$$)
# @alt(黒い|黒色の)
# 黒い__Y__グラフを描画する
# __Y__グラフの色を[黒にする|黒くする|黒色に設定する]
# xdataとydata[の|について]黒い__Y__グラフを描画する
# xdataとydata[の|について]__Y__グラフを描画して、[その|]色を[黒にする|黒くする|黒色に設定する]
# '''


# 散布図

plt.scatter(データ列x, データ列y)
'''
@alt(散らばり|相関|分布|散布)

[データ列の|]散布図を描画する
[データ列の|]散らばりを可視化する
'''

plt.scatter(データ列x, データ列y, s=n)
'''
散布図のマーカーの大きさを指定する
散布図のマーカーの大きさをnに設定する

xdataを縦軸、ydataを横軸として、大きさnの散布図を描画する
{xdataとydata[について|]の散布図を|大きさnで}描画する
xdataとydata[について|の]散布図を描画して、その大きさをnに設定する
'''

plt.plot(データ列x, データ列y, marker=__X__)
'''
@test(plt=missing;xdata=ydata=aList;$$)
@X('.';'o';'^';'v';'<';'>';'x';'X';'s';'D';'*')
@Y(ポイント;丸;[[|上]三角|▲|△];[下三角|▽|▼];左三角;右三角;[バツ|クロス];大バツ;四角;[ダイアモンド|菱形];星)
{散布図に|__Y__マーカーを}使う
{__Y__マーカーで_|散布図を}描画する
xdataとydata[について|の]散布図を描画して、マーカーを__Y__に設定する
xdataとydata[について|]の散布図に__Y__マーカーを描画する
'''

plt.plot(データ列x, データ列y, marker=__X__, c=rgb)
'''
@test(plt=missing;xdata=ydata=aList;$$)
{散布図に|rgbの__Y__マーカーを}使う
{rgbの__Y__マーカーで_|散布図を}描画する
{xdataとydata[について|]の散布図に|rgbの__Y__マーカーを}描画する
xdataとydata[について|の]散布図を描画して、__Y__マーカーの色をrgbに設定する
'''

plt.plot(データ列x, データ列y, marker=__X__, c='r')
'''
@test(plt=missing;xdata=ydata=aList;$$)
{散布図に|赤い__Y__マーカーを}使う
{赤い__Y__マーカーで_|散布図を}描画する
{xdataとydata[について|]の散布図に|赤い__Y__マーカーを}描画する
'''

plt.plot(データ列x, データ列y, marker=__X__, c='k')
'''
@test(plt=missing;xdata=ydata=aList;$$)
{散布図に|黒い__Y__マーカーを}使う
{黒い__Y__マーカーで_|散布図を}描画する
{xdataとydata[について|]の散布図に|黒い__Y__マーカーを}描画する
'''

plt.axvline(x=0, linestyle=__X__)
'''
@X('dashed';'dashbot';'dotted';'solid')
@Y(破線;一点鎖線;点線;実線)
グラフに[x=0の|鉛直方向の]__Y__を付ける
'''

plt.axhline(y=0, linestyle=__X__)
'''
グラフに[y=0の|水平方向の]__Y__を付ける
'''

# https: // yyousuke.github.io/matplotlib/matplotlib.html

plt.scatter(データ列x, データ列y, c=aList, cmap='Blues')
'''
aListに応じて、散布図の色を変える
xdataとydata[について|]aList[の値|]に応じて、散布図の色を変える
'''

plt.colorbar()
'''
カラーバーを描画する
カラーバーを付ける
'''

plt.colorbar(orientation='horizontal')
'''
@alt(横向き|水平)
カラーバーを横向き[で|に]描画する
カラーバーを横向き[で|に]付ける
'''


plt.scatter(データ列x, データ列y, label=s)
'''
xdataとydata[について|]の散布図に[sという|]凡例用のラベルを付ける
xdataとydata[について|の]散布図を描画して、sという凡例用のラベルを付ける
'''

# ヒストグラム

データ列 = [1, 2, 2, 1, 1, 1, 1]

plt.hist(データ列)
'''
@alt(ヒストグラム|ヒストグラム|[度数分布図|柱状図|柱状グラフ])

[データ列の|]ヒストグラムを描画する
[データ列の|]出現頻度を可視化する
{ヒストグラムで_|データ列を}可視化する
データ列をヒストグラムにする
'''

plt.hist(df[column])
'''
{データフレームの[列|カラム]を|ヒストグラムで_}描画する
データフレームの[列|カラム]をヒストグラムにする
'''

区関数 = 10

plt.hist(データ列, bins=区関数)
'''
@alt(ビン数|ビン[|の数]|区間[数|の数|])

ヒストグラムのビン数を設定する
{ビン数を設定して|ヒストグラムを}描画する
ヒストグラムを描画して、ビン数を設定する
'''

start = 0
end = 100

plt.hist(データ列, range=(start, end))
'''
@alt(範囲|区間|上限下限)

ヒストグラムの範囲を設定する
{ヒストグラムを|上限から下限[まで|]の範囲で}描画する
'''

plt.hist(データ列, density=True)
'''
ヒストグラムの描画して、正規化する
正規化されたヒストグラムを描画する
ヒストグラムを描画し、合計を1にする
'''

plt.hist([データ列, データ列], color=['b', 'r'])
'''
{ヒストグラムを|[２つ|横に]並べて}描画する
{データ列を|[２つ|横に]並べて}ヒストグラムにする
'''

plt.hist([データ列, データ列, データ列], color=['b', 'r', 'g'])
'''
{ヒストグラムを|[３つ|複数[横に|]]並べて}描画する
{データ列を|[３つ|複数[横に|]]並べて}ヒストグラムにする
'''

# 箱ヒゲ図

plt.boxplot(データ列)
'''
@alt(箱ひげ図|箱[髭|ヒゲ]図|ボックスチャート)

{データ列を|箱ひげ図で_}描画する
データ列を箱ひげ図にする
{箱ひげ図で_|データ列を}可視化する
データ列の[四分位|パーセンタイル]を可視化する
'''

plt.boxplot([データ列, データ列])
'''
{データ列を|２つ並べて}箱ひげ図にする
[２つの|複数の]データ列を箱ひげ図にする
{箱ひげ図を|[２つ|横に]並べて}描画する
'''

plt.boxplot([df['カラム'], df['カラム']])
'''
データフレームの[カラム|列]を並べて箱ひげ図にする
{データフレームの[２つの|複数の][カラム|列]を並べて|箱ひげ図で_}可視化する
'''

plt.boxplot([データ列, データ列], labels=['A', 'B'])
'''
{箱ひげ図に[ラベル|簡単な説明]を付ける}
'''

vert = False
'''
option: 箱ひげ図を[水平方向|横[方向|向き]]にする
'''

plt.boxplot(データ列, vert=False)
'''
箱ひげ図を横[方向|向き]にする
'''

showmeans = False
'''
option: [箱ひげ図に|]平均を[加える|追記する]
'''

plt.boxplot(データ列, showmeans=True)
'''
箱ひげ図を描画して、平均[値|]を[加える|追加する]
平均[値|]付き箱ひげ図を描画する
'''

plt.boxplot(データ列, meanline=True)
'''
箱ひげ図を描画して、平均線を[加える|追加する]
平均線付き箱ひげ図を描画する
'''


# 棒グラフ

ラベル列 = ['A', 'B', 'C']
データ列 = [10, 8, 6]

plt.bar(ラベル列, データ列)
'''
@alt(縦棒グラフ=[棒グラフ|縦棒グラフ|[縦向き|縦方向の|鉛直|垂直]棒グラフ])

縦棒グラフを描画する
データ列を縦棒グラフにする
'''

plt.barh(ラベル列, データ列)
'''
@alt(横棒グラフ|横[向き|方向の]棒グラフ|[水平|平行][な|]棒グラフ])

横棒グラフを描画する
データ列を横棒グラフにする
'''

plt.bar(ラベル列, データ列, bottom=データ列y, color='#800080')
'''
縦棒グラフを積み上げにする
積み上げ棒グラフを描画する
'''

plt.barh(ラベル列, データ列, bottom=データ列y, color='#800080')
'''
横棒グラフを積み上げにする
積み上げ横棒グラフを描画する
'''

plt.bar(ラベル列, データ列, width=0.5)
'''
縦棒グラフを描画して、[バー|棒]の[横|]幅を[調整する|設定する]
棒グラフの[横|]幅を[調整する|設定する]
'''

plt.barh(ラベル列, データ列, width=0.5)
'''
横棒グラフを描画して、[バー|棒]の[縦|]幅を[調整する|設定する]
横棒グラフの[縦|]幅を[調整する|設定する]
'''

plt.bar(ラベル列, データ列, align='center')
'''
縦棒グラフを描画して、[ラベルを|]中央寄せする
'''

plt.barh(ラベル列, データ列, align='center')
'''
横棒グラフを描画して、[ラベルを|]中央寄せする
'''

plt.bar(ラベル列, データ列, align='edge')
'''
縦棒グラフを描画して、[ラベルを|]左寄せする
'''

plt.barh(ラベル列, データ列, align='edge')
'''
横棒グラフを描画して、[ラベルを|]下寄せする
'''

plt.bar(ラベル列, データ列, color=rgb)
'''
{棒グラフの色を|[rgbに|]}設定する
'''

plt.barh(ラベル列, データ列, color=rgb)
'''
{横棒グラフの色を|[rgbに|]}設定する
'''

# 円グラフ

plt.pie(データ列, startangle=90)
'''
データ列を円グラフにする
{円グラフで_|データ列の[割合|比率|パーセント]を}可視化する
'''

plt.pie(データ列, startangle=90, autopct='%.2f%%')
'''
円グラフの[割合|パーセント|百分率]を表示する
[割合|パーセント|百分率]付きの円グラフを描画する
'''

plt.pie(データ列, startangle=90, labels=ラベル列)
'''
円グラフにラベルを付ける
ラベル付きの円グラフを描画する
'''

plt.pie(データ列, startangle=90, counterclock=False)
'''
{円グラフを|時計回りに}描画する
'''

plt.pie(データ列, startangle=90, explode=[0, 0.3, 0])
'''
円グラフの特定の要素[だけ|を][切り出す|目立たせる]
'''

plt.axis('equals')
'''
[グラフを|作画を]正方形にする
円グラフを[真円|正円|完全な円|きれいな円|円|正確な円]にする
[グラフの|作画の|][x軸とy軸|縦横]の比率を[等しく|同じ]する
[グラフの|作画の|]縦横比を[等しく|同じ]する
'''

plt.savefig('foo.png')
'''
{グラフを|[画像|PNG]ファイルとして}保存する
'''

plt.show()
'''
グラフを表示する
'''


'''
plt.subplot(X, y, 2)
X行y列の2つ目のグラフ指定



plt.axis('equal')


# 出力・保存


plt.show()
プロットを[描画する|表示する|出力する]
'''
