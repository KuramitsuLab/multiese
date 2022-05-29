import matplotlib
import matplotlib.pyplot as plt
from sympy import N
'''
@test($$;plt.__name__)
@alt(描画する|描く|プロットする)
@alt(グラフ|プロット)
グラフを描画する[準備をする|]
グラフを使う[準備をする|]
'''

import seaborn as sns
'''
@alt(見栄え|見た目|デザイン)
[綺麗な|見やすい]グラフを描画する[準備をする|]
[綺麗な|見やすい]グラフを使う[準備をする|]
グラフ[の見栄え|の描画|]を綺麗にする
グラフ[の描画|]を見やすくする
グラフの見栄えを[良く|よく]する
'''

sns.set()
'''
@test(sns=missing;$$)
[seabornの|]デフォルト[|スタイル|見栄え]を適用する
{グラフ[の見栄え|]を|[デフォルトで|]}[いい|イイ]感じに設定する
'''

__X__ = 'paper'
sns.set(context=__X__)
'''
@test(sns=missing;$$)
@X('paper';'notebook';'talk';'poster')
@Y(論文;画面;[スライド|プレゼン];ポスター)
{グラフ[の用途|の目的|]を|__Y__に}設定する
{グラフを|__Y__用に}設定する
'''

__X__ = 'deep'
sns.set(pallete=__X__)
'''
@test(sns=missing;$$)
@X('deep';'muted';'pastel';'dark';'bright';'colorblind')
@Y(濃く;淡く;パステル調に;暗く;明るく;色差別なく)
@alt(カラーパレット|色|パレット|[色|カラー|]テーマ|色[|調|使い])
グラフ[の[色|カラーパレット]]を[|全般的に]__Y__する
[グラフの|]{カラーパレットを|[|全般的に]}__Y__する
'''

__X__ = 'deep'
sns.set(pallete=__X__)
'''
@test(sns=missing;$$)
@X('deep';'muted';'pastel';'dark';'bright';'colorblind')
@Y(濃い;淡い;パステル調の;暗い;明るい;色差別ない)
{グラフの描画で|__Y__カラーパレットを}使う
'''

palleteName = 'pastel'

sns.set(pallete=palleteName)
'''
@test(sns=missing;$$)
グラフ[の|で使う]カラーパレットをpalleteNameで指定する
グラフ[の|で使う]カラーパレットをpalleteNameに設定する
'''

fontName = 'Yu Gothic'
sns.set(font=fontName)
'''
@test(sns=missing;$$)
グラフで使うフォントをfontNameに指定する
グラフの中のフォントをfontNameに設定する
'''

sns.set(font='IPAexGothic')
'''
@test(sns=missing;$$)
@alt(グラフの中|グラフ|グラフ[内|中|)
@alt(できる|可能な)
@alt(に設定する|[に|と]する|に[セット|指定]する|に変更する|変える)
{グラフで|日本語[|フォント]を}[表示できる|使える]ようにする
グラフの中の[日本語フォント|日本語表示]を[有効にする|利用可能にする]
[グラフの|グラフで使う]フォントを[日本語表示|日本語]に設定する
[グラフの|]文字化けを防ぐ
'''

sns.set(style='darkgrid')
'''
@test(sns=missing;$$)
@alt(背景|背景色|グリッド)
グラフの背景を暗くする
グラフの背景を暗くする
'''

sns.set(style='whitegrid')
'''
@test(sns=missing;$$)
@alt(背景|背景色|グリッド)
グラフの背景を白くする
'''

untitled = 'untitled'

plt.title(untitled)
'''
@test(plt=missing;$$)
@alt(タイトル|題名|名前)
[グラフの|グラフで使う]タイトルを[untitledに|]設定する
'''

width = 8
height = 6

plt.figure(figsize=(width, height))
'''
@test(plt=missing;$$)
@alt(サイズ|大きさ)
グラフのサイズを[横width縦height|縦height横width]に設定する
グラフのサイズを[設定する|指定する|変更する]
'''

plt.xlabel(untitled)
'''
@test(plt=missing;$$)
@alt(横軸|x軸|x座標)
@alt(軸ラベル=ラベル|軸ラベル|名[前|称]|軸名|説明|キャプション)
@alt(付ける|つける|設定する)
[グラフの|グラフで使う|]横軸の軸ラベルをuntitledに設定する
[グラフの|グラフで使う|]横軸に[untitledという|]軸ラベルを付ける
'''

plt.ylabel(untitled)
'''
@test(plt=missing;$$)
@alt(縦軸|y軸|y座標)
[グラフの中の|グラフで使う|]縦軸の軸ラベルをuntitledに設定する
[グラフの中の|グラフで使う|]縦軸に[untitledという|]軸ラベルを付ける
'''

plt.grid(True)
'''
@test(plt=missing;$$)
@alt(入れる|付ける|加える|描画する|表示する)
@alt(グリッド|[グリッド|目盛り|メモリ]線|格子|格子線)
{グラフに|[グリッド]を}入れる
'''

plt.legend()
'''
@test(plt=missing;$$)
@alt(凡例|凡例|データラベル|補足)
{[グラフに|]|凡例を}入れる
'''

plt.legend([s, s2])
'''
@test(plt=missing;$$)
{[グラフに]|凡例を|sとs2と}入れる
'''

x, y = 0.5, 0.5
plt.legend(loc=(x, y))
'''
@test(plt=missing;$$)
@alt(位置|場所)
[グラフの|]凡例の位置を指定する
[グラフの|]凡例の位置を(x, y)に設定する
{グラフ中の(x, y)の位置に|凡例を}入れる
'''

plt.legend(loc='best')
'''
@test(plt=missing;$$)
{[最適な|ベストな|グラフに被らない]位置に|凡例を}入れる
'''

plt.legend(frameon=False)
'''
@test(plt=missing;$$)
{[グラフの中に|]|枠なしの凡例を}入れる
'''

xdata = ydata = [1, 2, 3]

plt.plot(xdata, ydata)
'''
@test(plt=missing;xdata=ydata=aList;$$)
@alt(グラフ|グラフ)
@alt(折れ線グラフ|線グラフ|[ライン|線])
@alt(と指定して|[と|に]して|[と|に]設定して)
@prefix(xdata;[リスト|配列|データ列|数列|イテラブル])
@prefix(ydata;[リスト|配列|データ列|数列|イテラブル])
折れ線グラフを描画する
xdataとydataの折れ線グラフを描画する
xdataとydataを折れ線グラフ[で|に]描画する
xdataを縦軸、ydataを横軸と指定して、折れ線グラフを描画する
'''

plt.plot(range(len(xdata)), xdata)
'''
@test(plt=missing;xdata=ydata=aList;$$)
@alt(変化|変遷|移り変わり|推移)
xdataの変化を折れ線グラフ[で|に]描画する
ydataを横軸と指定して、[折れ線グラフ|xdataの変化]を描画する
'''

df, col, col2 = {}, 'A', 'B'

plt.plot(df[col], df[col2])
'''
@test(plt=missing;$$)
@prefix(df;データフレーム)
@prefix(col;カラム)
{dfのcolとcol2を|折れ線グラフで_}描画する
'''

alpha = 0.5

plt.plot(xdata, ydata, alpha=alpha)
'''
@test(plt=missing;xdata=ydata=aList;$$)
@alt(透明度|アルファ[|値])
透明度alphaの折れ線グラフを描画する
折れ線グラフの透明度をalphaに設定する
{xdataとydataの折れ線グラフを|透明度alphaで}描画する
xdataとydataの折れ線グラフを描画して、透明度をalphaに設定する
'''

matplotlib.colors.cnames
'''
@test(import matplotlib;$$)
グラフで[使える|利用可能な]色[名|]の一覧[|を得る|を知る]
'''

plt.plot(xdata, ydata, color=s)
'''
@test(plt=missing;xdata=ydata=aList;$$)
折れ線グラフの色をsに設定する
{xdataとydataの折れ線グラフを|sの色で}描画する
xdataとydataの折れ線グラフを描画して、色をsに設定する
'''

rgb = '#fff'

plt.plot(xdata, ydata, color=rgb)
'''
@test(plt=missing;xdata=ydata=aList;rgb='#fff';$$)
@prefix(rgb;カラーコード)
折れ線グラフの色をrgbに設定する
{xdataとydataの折れ線グラフを|rgbで}描画する
xdataとydata[|について]の折れ線グラフを描画して、[その|]色をrgbに設定する
'''

# https://own-search-and-study.xyz/2016/08/08/matplotlib-pyplotのplotの全引数を使いこなす/


__X__ = 'r'
plt.plot(xdata, ydata, linestyle='dash', color=__X__)
'''
@test(plt=missing;xdata=ydata=aList;$$)
破線グラフの色を__Y__に設定する
xdataとydata[について|の]破線グラフを描画して、[その|]色を__Y__に設定する
'''

__X__ = 'r'
plt.plot(xdata, ydata, linewidth=n, color=__X__)
'''
@test(plt=missing;xdata=ydata=aList;$$)
__Y__色の折れ線グラフを描画して、[その|]線幅をnに設定する
xdataとydataについて__Y__色の折れ線グラフを描画して、[その|]線幅をnに設定する
'''

plt.plot(xdata, ydata, c=__X__)
'''
@test(plt=missing;xdata=ydata=aList;$$)
{散布図に|__Y__色のマーカーを}使う
{__Y__色[のマーカー|]で_|散布図を}描画する
{xdataとydata[について|]の散布図を|__Y__色で_}描画する
xdataとydata[について|の]散布図を描画して、[マーカーの|]色を__Y__に設定する
'''

plt.plot(xdata, ydata, c=__X__, alpha=0.5)
'''
@test(plt=missing;xdata=ydata=aList;$$)
{__Y__色[のマーカー|]で_|散布図を|重なりを見やすく}描画する
{xdataとydata[について|]の散布図を|__Y__色で_|重なりを見やすく}描画する
'''

plt.hist(xdata, color=__X__)
'''
@test(plt=missing;xdata=ydata=aList;$$)
@alt(ヒストグラム|[柱状図|柱状グラフ|度数分布図])
{__Y__[色|]で_|[xdataについての|]ヒストグラムを}描画する
{xdataを|__Y__色のヒストグラムで_}描画する
'''

###


plt.plot(xdata, ydata, label=untitled)
'''
@test(plt=missing;xdata=ydata=aList;$$)
折れ線グラフにラベルを付ける
折れ線グラフのラベルをuntitledに設定する
{xdataとydataの折れ線グラフを|untitledとラベル付けして}描画する
xdataとydataの折れ線グラフを描画して、untitledとラベル付けする
'''

linewidth = n
'''
＜オプション＞[|グラフの]線幅をnに設定する
'''

plt.plot(xdata, ydata, linewidth=n)
'''
折れ線グラフの線幅を指定する
折れ線グラフの線幅をnに設定する
線幅nの折れ線グラフを描画する
{xdataとydataで_|折れ線グラフを}描画して、[その|]線幅をnに設定する
'''

plt.plot(xdata, ydata, linestyle=__X__, linewidth=n)
'''
[__Y__グラフ|__Y__の折れ線グラフ]の線幅を指定する
[__Y__グラフ|__Y__の折れ線グラフ]の線幅をnに設定する
{[xdataとydataで_|]|[__Y__グラフ|__Y__の折れ線グラフ]を}描画して、[その|]線幅をnに設定する
'''

plt.plot(xdata, ydata, linestyle=__X__, color=rgb)
'''
[__Y__グラフ|__Y__の折れ線グラフ]の色をrgbに設定する
xdataとydata[の|について]rgbの__Y__グラフを描画する
{[xdataとydataで_|]|[__Y__グラフ|__Y__の折れ線グラフ]を}描画して、[その|]線幅をnに設定する
'''

plt.plot(xdata, ydata, linestyle=__X__, color='r')
'''
@alt(赤い|赤色の)
赤い[__Y__グラフ|__Y__の折れ線グラフ]を描画する
[__Y__グラフ|__Y__の折れ線グラフ]の色を[赤にする|赤くする|赤色に設定する]
{[xdataとydataで_|]|[__Y__グラフ|__Y__の折れ線グラフ]を}描画して、[その|]線幅をnに設定する
'''

plt.plot(xdata, ydata, linestyle=__X__, color='b')
'''
@alt(青い|青色の)
青い__Y__グラフを描画する
__Y__グラフの色を[青にする|青くする|青色に設定する]
xdataとydata[の|について]青い__Y__グラフを描画する
xdataとydata[の|について]__Y__グラフを描画して、[その|]色を[青にする|青くする|青色に設定する]
'''

plt.plot(xdata, ydata, linestyle=__X__, color='k')
'''
@test(plt=missing;xdata=ydata=aList;$$)
@alt(黒い|黒色の)
黒い__Y__グラフを描画する
__Y__グラフの色を[黒にする|黒くする|黒色に設定する]
xdataとydata[の|について]黒い__Y__グラフを描画する
xdataとydata[の|について]__Y__グラフを描画して、[その|]色を[黒にする|黒くする|黒色に設定する]
'''


# 散布図

plt.scatter(xdata, ydata)
'''
[xdataとydata[について|の]|]散布図を描画する
[xdataとydata[について|の]|][相関|散らばり]を可視化する
'''

plt.scatter(xdata, ydata, s=n)
'''
散布図のマーカーの大きさを指定する
散布図のマーカーの大きさをnに設定する

xdataを縦軸、ydataを横軸として、大きさnの散布図を描画する
{xdataとydata[について|]の散布図を|大きさnで}描画する
xdataとydata[について|の]散布図を描画して、その大きさをnに設定する
'''

plt.plot(xdata, ydata, marker=__X__)
'''
@test(plt=missing;xdata=ydata=aList;$$)
@X('.';'o';'^';'v';'<';'>';'x';'X';'s';'D';'*')
@Y(ポイント;丸;[[|上]三角|▲|△];[下三角|▽|▼];左三角;右三角;[バツ|クロス];大バツ;四角;[ダイアモンド|菱形];星)
{散布図に|__Y__マーカーを}使う
{__Y__マーカーで_|散布図を}描画する
xdataとydata[について|の]散布図を描画して、マーカーを__Y__に設定する
xdataとydata[について|]の散布図に__Y__マーカーを描画する
'''

plt.plot(xdata, ydata, marker=__X__, c=rgb)
'''
@test(plt=missing;xdata=ydata=aList;$$)
{散布図に|rgbの__Y__マーカーを}使う
{rgbの__Y__マーカーで_|散布図を}描画する
{xdataとydata[について|]の散布図に|rgbの__Y__マーカーを}描画する
xdataとydata[について|の]散布図を描画して、__Y__マーカーの色をrgbに設定する
'''

plt.plot(xdata, ydata, marker=__X__, c='r')
'''
@test(plt=missing;xdata=ydata=aList;$$)
{散布図に|赤い__Y__マーカーを}使う
{赤い__Y__マーカーで_|散布図を}描画する
{xdataとydata[について|]の散布図に|赤い__Y__マーカーを}描画する
'''

plt.plot(xdata, ydata, marker=__X__, c='k')
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

plt.scatter(xdata, ydata, c=aList, cmap='Blues')
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


plt.scatter(xdata, xdata, label=s)
'''
xdataとydata[について|]の散布図に[sという|]凡例用のラベルを付ける
xdataとydata[について|の]散布図を描画して、sという凡例用のラベルを付ける
'''

# ヒストグラム

データ列 = [1, 2, 2, 1, 1, 1, 1]

plt.hist(データ列)
'''
@alt(ヒストグラム|[度数分布図|柱状図|柱状グラフ])

ヒストグラムを描画する
'''

__X__ = xdata

plt.hist(__X__)
'''
@X(aList;aArray;df[column];ds)
@Y(aList;aArray;dfのcolumn;ds)

__Y__のヒストグラムを描画する
{__Y__を|ヒストグラムで_}可視化する
__Y__をヒストグラムにする
'''


plt.hist(データ列, alpha=0.5)
'''
ヒストグラムを半透明[に|化]する
ヒストグラムを描画して、半透明[に|化]にする
'''

plt.hist(データ列, alpha=x)
'''
{ヒストグラムの透明度を|xに}設定する
ヒストグラムを描画して、{透明度を|xに}設定する
'''


plt.hist(データ列, bins=n)
'''
@alt(ビン数|ビン[|の数]|区間[数|の数|])

ヒストグラムのビン数を設定する
{ビン数を[nに|]設定して|ヒストグラムを}描画する
ビン数nのヒストグラムを描画する
ヒストグラムを描画して、{ビン数を|nに}設定する
'''

start = 0
end = 100

plt.hist(データ列, range=(start, end))
'''
@alt(範囲|区間|間)

ヒストグラムの範囲を設定する
{ヒストグラムを|startからend[まで|]の範囲で}描画する
{startからendの範囲のヒストグラムを用いて|xdataを}描画する
startからend[まで|の範囲で]ヒストグラムにする
'''

plt.hist(データ列, density=True)
'''
ヒストグラムの描画して、正規化する
正規化されたヒストグラムを描画する
ヒストグラムを描画し、合計を1にする
'''

データ列2 = データ列

plt.hist([データ列, データ列2], color=['b', 'r'])
'''
２つのデータ列を並べてヒストグラムにする
{ヒストグラムを|[２つ|横に]並べて}描画する
'''

# 箱ヒゲ図

plt.boxplot(データ列)
'''
@alt(箱ひげ図|箱[髭|ヒゲ]図|ボックスチャート)

データ列を箱ひげ図で描画する
データ列を箱ひげ図にする
{箱ひげ図で_|データ列を}可視化する
'''

plt.boxplot([データ列, データ列2])
'''
２つのデータ列を並べて箱ひげ図にする
{箱ひげ図を|[２つ|横に]並べて}描画する
箱ひげ図を[２つ|横に]並べる
'''

column = 'A'
column2 = 'B'
column3 = 'C'

plt.boxplot([df[column], df[column2]])
'''
２つの[カラム|列]を並べて箱ひげ図にする
'''

# 棒グラフ

ラベル列 = ['A', 'B', 'C']
データ列 = [10, 8, 6]

plt.bar(ラベル列, データ列)
'''
@alt(縦棒グラフ|縦[向き|方向の]棒グラフ|[鉛直|垂直][な|]棒グラフ])

棒グラフを描画する
データ列とラベルを指定して、棒グラフを描画する
縦棒グラフを描画する
データ列とラベルを指定して、縦棒グラフを描画する
'''

plt.barh(ラベル列, データ列)
'''
@alt(横棒グラフ|横[向き|方向の]棒グラフ|[水平|平行][な|]棒グラフ])

横棒グラフを描画する
データ列とラベル列を指定して、横棒グラフを描画する
'''

plt.bar(ラベル列, データ列, color=rgb)
'''
{棒グラフの色を|[rgbに|]}設定する
'''

plt.barh(ラベル列, データ列, color=rgb)
'''
{横棒グラフの色を|[rgbに|]}設定する
'''

plt.bar(ラベル列, データ列, bottom=データ列2, color="red")
'''
[棒グラフ|縦棒グラフ]を積み上げにする
[データ列とラベル列を指定して、|]積み上げ棒グラフを描画する
'''

plt.barh(ラベル列, データ列, bottom=データ列2, color="red")
'''
横棒グラフを積み上げにする
[データ列とラベル列を指定して、|]積み上げ横棒グラフを描画する
'''


plt.bar(ラベル列, データ列, width=x)
'''
棒グラフを描画して、{[グラフ|棒の|]幅を|xに}設定する
{棒グラフの幅を|xに}設定する
'''

plt.barh(ラベル列, データ列, width=x)
'''
横棒グラフを描画して、{[グラフ|棒の|]幅を|xに}設定する
{横棒グラフの幅を|xに}設定する
'''

plt.bar(ラベル列, データ列, align='center')
'''
棒グラフを描画して、中央寄せする
縦棒グラフを描画して、中央寄せする
'''

plt.barh(ラベル列, データ列, align='center')
'''
横棒グラフを描画して、中央寄せする
'''


sns.pairplot(df[[column, column2, column3]])
'''
複数[カラム|列]の[散布図|ヒストグラム|関係性]を[一度に|まとめて]描画する
'''


'''
plt.subplot(X, y, 2)
X行y列の2つ目のグラフ指定


# 描画

plt.boxplot([df['G1'], df['G2'], df['G3']])
@type(df)の@type('G1', カラム)と@type('G2', カラム)と@type('G3', カラム)についての箱ひげ図を描画する
[同じグラフ内で|]@type(df)の@type('G1')と@type('G2')と@type('G3')を箱ひげ図で描画する
@type(df)の@type('G1')と@type('G2')と@type('G3')の箱ひげ図を一枚のグラフで描画する


plt.barh(X, Y)
{縦軸をX}としたYの[横棒グラフ|横向き棒グラフ|横方向の棒グラフ|水平棒グラフ|棒グラフ]を描画する
{縦軸をX}として、Yの横棒グラフを描画する



plt.xticks(x, ['A', 'B', 'C'])
横軸のラベルをxから'A'、'B'、'C'[へ変更する|に変える]
棒グラフの軸ラベルをxから'A'、'B'、'C'へ変更する
棒グラフの[項目名|項目|それぞれのラベル]をxから'A'、'B'、'C'へ変更する

plt.barh(y, x, align = 'center')
{棒グラフの位置を真ん中}として、{縦軸をy}としたxの横棒グラフを描画する
{軸をy}として、xの横棒グラフを描画する
{棒の位置を中心}に設定して、横向きの棒グラフを描画する

plt.yticks(y, ['A','B','C'])
縦軸のラベルをyから'A'、'B'、'C'へ変更する
棒グラフの項目名をyから'A'、'B'、'C'へ変更する

plt.pie(x)
xの円グラフを描画する
xについて円グラフを描画する
xを円グラフにする

plt.axis('equal')
円グラフを[真円|正円|完全な円|きれいな円|円|正確な円]にする


# 出力・保存

plt.savefig('foo.png')
[プロット|グラフ|図]を'foo.png'として[保存する|セーブする|出力する]
プロットを'foo.png'という名前で保存する
[作成した|作画した|作った|描画した|プロットした|]プロットを'foo.png'[という名前|]で保存する
作成したプロットを'foo.png'として保存する
作成したプロットを'foo.png'というファイル名で保存する
作成したプロットを'foo.png'というファイル名[をつけて|にして]保存する

plt.show()
プロットを[描画する|表示する|出力する]
'''
