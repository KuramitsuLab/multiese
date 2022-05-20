import matplotlib
import matplotlib.pyplot as plt
'''
@test($$;plt.__name__)
@alt(描画する|描く|プロットする)
@alt(グラフ|プロット|matplotlib)
グラフを描画する
グラフを使う
'''

import seaborn as sns
'''
@test($$;sns.__name__)
[綺麗な|キレイな|見やすい]グラフを描画する
[綺麗な|キレイな|見やすい]グラフを使う
グラフを[綺麗|キレイ]にする
グラフを見やすくする
グラフの見た目を[良く|よく]する
'''

sns.set()
'''
@test(sns=missing;$$)
@alt(見た目|デザイン)
[seabornの|]デフォルト[|スタイル|見た目]を適用する
グラフ[の見た目]を[デフォルトで|][いい|イイ]感じに設定する
'''

__X__ = 'paper'
sns.set(context=__X__)
'''
@test(sns=missing;$$)
@X('paper';'notebook';'talk';'poster')
@Y(論文;画面;[スライド|プレゼン];ポスター)
グラフ[の用途|の目的|]を__Y__[|用]に設定する
'''

__X__ = 'deep'
sns.set(pallete=__X__)
'''
@test(sns=missing;$$)
@X('deep';'muted';'pastel';'dark';'bright';'colorblind')
@Y(濃く;淡く;パステル調に;暗く;明るく;色差別なく)
@alt(カラーパレット|色|パレット|[色|カラー|]テーマ|色[|調|使い])
グラフ[[の|で使う]カラーパレット|]を[|全般的に]__Y__する
'''

__X__ = 'deep'
sns.set(pallete=__X__)
'''
@test(sns=missing;$$)
@X('deep';'muted';'pastel';'dark';'bright';'colorblind')
@Y(濃い;淡い;パステル調の;暗い;明るい;色差別ない)
{__X__カラーパレットを|グラフ[|全般]に}使う
'''

s = 'pastel'

sns.set(pallete=s)
'''
@test(sns=missing;$$)
グラフ[の|で使う]カラーパレットをsで指定する
グラフ[の|で使う]カラーパレットをsに設定する
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
{グラフの中で|日本語[|フォント]を}[表示できる|使える]ようにする
グラフの中の[日本語フォント|日本語表示]を[有効にする|利用可能にする]
[グラフの中の|グラフで使う]フォントを[日本語表示|日本語]に設定する
[グラフの中の|]文字化けを防ぐ
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

sns.set(palette=s)
'''
@test(sns=missing;$$)
グラフの[|描画で使う]パレットをsに設定する
'''

s = s2 = 'label'
plt.title(s)
'''
@test(plt=missing;$$)
@alt(グラフ|プロット)
@alt(タイトル|題名|名前)
[グラフの中の|グラフで使う]タイトルをsに設定する
'''

n, n2 = 10, 6
plt.figure(figsize=(n, n2))
'''
@test(plt=missing;$$)
@alt(サイズ|大きさ)
[描画する|表示する|出力する|]グラフのサイズを[横n縦n2|縦n2横n|n×n2]に設定する
'''

plt.xlabel(s)
'''
@test(plt=missing;$$)
@alt(横軸|x軸|x座標)
@alt(軸ラベル|ラベル|ラベル|名[前|称]|軸名|説明)
@alt(付ける|つける|設定する)
[グラフの中の|グラフで使う|]横軸の軸ラベルをsに設定する
[グラフの中の|グラフで使う|]横軸にsという軸ラベルを付ける
'''

plt.ylabel(s)
'''
@test(plt=missing;$$)
@alt(縦軸|y軸|y座標)
[グラフの中の|グラフで使う|]縦軸の軸ラベルをsに設定する
[グラフの中の|グラフで使う|]縦軸にsという軸ラベルを付ける
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
{[グラフの中に|]|凡例を}入れる
'''

plt.legend([s, s2])
'''
@test(plt=missing;$$)
{[グラフの中に]|凡例を|sとs2と}入れる
'''

x, x2 = 0.5, 0.5
plt.legend(loc=(x, x2))
'''
@test(plt=missing;$$)
{[グラフの中に|]|凡例を|(x, x2)の[位置|場所]に}入れる
{グラフ中の(x, x2)の[位置|場所]に|凡例を|}入れる
'''

plt.legend(loc='best')
'''
@test(plt=missing;$$)
{[最適な|ベストな|最も適切な|グラフに被らない][位置|場所]に|凡例を}入れる
'''

plt.legend(frameon=False)
'''
@test(plt=missing;$$)
{[グラフの中に|]|枠なしの凡例を}入れる
'''

xdata = ydata = [1, 2, 3]
plt.plot(xdata, ydata)
'''
@test(plt=missing;xdata=ydata=alist;$$)
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
@test(plt=missing;xdata=ydata=alist;$$)
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

plt.plot(xdata, ydata, alpha=x)
'''
@test(plt=missing;xdata=ydata=alist;$$)
@alt(透明度|アルファ[|値])
透明度xの折れ線グラフを描画する
折れ線グラフの透明度をxに設定する
{xdataとydataの折れ線グラフを|透明度xで}描画する
xdataとydataの折れ線グラフを描画して、透明度をxに設定する
'''

matplotlib.colors.cnames
'''
@test(import matplotlib;$$)
グラフで使える色の一覧[|を得る|を知る]
'''

plt.plot(xdata, ydata, color=s)
'''
@test(plt=missing;xdata=ydata=alist;$$)
折れ線グラフの色をsに設定する
{xdataとydataの折れ線グラフを|sの色で}描画する
xdataとydataの折れ線グラフを描画して、色をsに設定する
'''

rgb = '#fff'
plt.plot(xdata, ydata, color=rgb)
'''
@test(plt=missing;xdata=ydata=alist;rgb='#fff';$$)
@prefix(rgb;カラーコード)
折れ線グラフの色をrgbに設定する
{xdataとydataの折れ線グラフを|rgbで}描画する
xdataとydata[|について]の折れ線グラフを描画して、[その|]色をrgbに設定する
'''

# https://own-search-and-study.xyz/2016/08/08/matplotlib-pyplotのplotの全引数を使いこなす/

__X__ = 'r'
plt.plot(xdata, ydata, color=__X__)
'''
@test(plt=missing;xdata=ydata=alist;$$)
@X('aliceblue';'antiquewhite';'aqua';'aquamarine';'azure';'beige';'bisque';'black';'blanchedalmond';'blue';'blueviolet';'brown';'burlywood';'cadetblue';'chartreuse';'chocolate';'coral';'cornflowerblue';'cornsilk';'crimson';'cyan';'darkblue';'darkcyan';'darkgoldenrod';'darkgray';'darkgreen';'darkgrey';'darkkhaki';'darkmagenta';'darkolivegreen';'darkorange';'darkorchid';'darkred';'darksalmon';'darkseagreen';'darkslateblue';'darkslategray';'darkslategrey';'darkturquoise';'darkviolet';'deeppink';'deepskyblue';'dimgray';'dimgrey';'dodgerblue';'firebrick';'floralwhite';'forestgreen';'fuchsia';'gainsboro';'ghostwhite';'gold';'goldenrod';'gray';'green';'greenyellow';'grey';'honeydew';'hotpink';'indianred';'indigo';'ivory';'khaki';'lavender';'lavenderblush';'lawngreen';'lemonchiffon';'lightblue';'lightcoral';'lightcyan';'lightgoldenrodyellow';'lightgray';'lightgreen';'lightgrey';'lightpink';'lightsalmon';'lightseagreen';'lightskyblue';'lightslategray';'lightslategrey';'lightsteelblue';'lightyellow';'lime';'limegreen';'linen';'magenta';'maroon';'mediumaquamarine';'mediumblue';'mediumorchid';'mediumpurple';'mediumseagreen';'mediumslateblue';'mediumspringgreen';'mediumturquoise';'mediumvioletred';'midnightblue';'mintcream';'mistyrose';'moccasin';'navajowhite';'navy';'oldlace';'olive';'olivedrab';'orange';'orangered';'orchid';'palegoldenrod';'palegreen';'paleturquoise';'palevioletred';'papayawhip';'peachpuff';'peru';'pink';'plum';'powderblue';'purple';'rebeccapurple';'red';'rosybrown';'royalblue';'saddlebrown';'salmon';'sandybrown';'seagreen';'seashell';'sienna';'silver';'skyblue';'slateblue';'slategray';'slategrey';'snow';'springgreen';'steelblue';'tan';'teal';'thistle';'tomato';'turquoise';'violet';'wheat';'white';'whitesmoke';'yellow';'yellowgreen')
@Y(アリスブルー;アンティークホワイト;アクア;アクアマリン;紺碧;ベージュ;ビスク;ブラック;ブランチドアーモンド;青;ブルーバイオレット;ブラウン;ハリウッド;カデットブルー;シャルトルーズ;チョコレート;コーラル;コーンフラワーブルー;コーンズシルク;クリムゾン;シアン;ダークブルー;ダークシアン;ダークゴールデンロッド;ダークグレー;ダークグリーン;ダークグレー;ダークカーキ;ダークマゼンタ;ダークオリーブグリーン;ダークオレンジ;ダークオーキッド;ダークレッド;ダークサーモン;ダークシアグリーン;ダークスレートブルー;ダークスラテグレー;ダーク・スラテグレー;ダークターコイズ;ダークバイオレット;デピンク;ディープスカイブルー;ディムグレー;ディムグレー;ドジャーブルー;耐火レンガ;フローラルホワイト;フォレストグリーン;フクシア;ゲインズボロ;ゴーストホワイト;ゴールド;ゴールデンロッド;グレー;グリーン;グリーンイエロー;グレー;ハニーデュー;ホットピンク;インディアンレッド;インディゴ;アイボリー;カーキ;ラベンダー;ラベンダーブラッシュ;ローングリーン;レモンシフォン;ライトブルー;ライトコーラル;ライトシアン;ライトゴールドロディイエロー;ライトグレー;ライトグリーン;ライトグレー;淡いピンク色;ライトサーモン;ライトグリーン;ライトスカイブルー;ライトスレイグレー;ライトスレイグレー;ライトスチールブルー;ライトイエロー;ライム;ライムグリーン;リネン;マゼンタ;マルーン;ミディアムアクアマリン;ミディアムブルー;ミディアムオーキッド;ミディアムパープル;ミディアムシアグリーン;ミディアムスレートブルー;ミディアムスプリンググリーン;ミディアムターコイズ;ミディアムバイオレットレッド;ミッドナイトブルー;ミントクリーム;ミスティローズ;モカシン;ナバホホワイト;ネイビー;オールドレース;オリーブ;オリベドラブ;オレンジ;オレンジレッド;オーキッド;パールゴールデンロッド;ペールグリーン;パレットトルコイズ;パールバイオレットレッド;パパイヤウィップ;ピーチパフ;ペルー;ピンク;プラム;パウダーブルー;パープル;レベッカパープル;赤;ロージーブラウン;ロイヤルブルー;サドルブラウン;サーモン;サンディーブラウン;シーグリーン;貝殻;シエナ;シルバー;スカイブルー;スレートブルー;スラグレー;スラグレー;スノー;スプリンググリーン;スチールブルー;タン;ティール;アザミ;トマト;ターコイズ;バイオレット;小麦;ホワイト;ホワイトスモーク;黄色;イエローグリーン)
折れ線グラフの色を__Y__に設定する
__Y__色の折れ線グラフを描画する
xdataとydata[について|の]折れ線グラフを描画して、[その|]色を__Y__に設定する
'''

__X__ = 'r'
plt.plot(xdata, ydata, linestyle='dash', color=__X__)
'''
@test(plt=missing;xdata=ydata=alist;$$)
破線グラフの色を__Y__に設定する
xdataとydata[について|の]破線グラフを描画して、[その|]色を__Y__に設定する
'''

__X__ = 'r'
plt.plot(xdata, ydata, linewidth=n, color=__X__)
'''
@test(plt=missing;xdata=ydata=alist;$$)
__Y__色の折れ線グラフを描画して、[その|]線幅をnに設定する
xdataとydataについて__Y__色の折れ線グラフを描画して、[その|]線幅をnに設定する
'''

plt.plot(xdata, ydata, c=__X__)
'''
@test(plt=missing;xdata=ydata=alist;$$)
{散布図に|__Y__色のマーカーを}使う
{__Y__色[のマーカー|]で_|散布図を}描画する
{xdataとydata[について|]の散布図を|__Y__色で_}描画する
xdataとydata[について|の]散布図を描画して、[マーカーの|]色を__Y__に設定する
'''

plt.plot(xdata, ydata, c=__X__, alpha=0.5)
'''
@test(plt=missing;xdata=ydata=alist;$$)
{__Y__色[のマーカー|]で_|散布図を|重なりを見やすく}描画する
{xdataとydata[について|]の散布図を|__Y__色で_|重なりを見やすく}描画する
'''

plt.hist(xdata, color=__X__)
'''
@test(plt=missing;xdata=ydata=alist;$$)
@alt(ヒストグラム|[柱状図|柱状グラフ|度数分布図])
{__Y__[色|]で_|[xdataについての|]ヒストグラムを}描画する
{xdataを|__Y__色のヒストグラムで_}描画する
'''

###

__X__ = 'r'
plt.plot(xdata, ydata, color=__X__)
'''
@test(plt=missing;xdata=ydata=alist;$$)
@X('r';'b';'k';'w';'y')
@Y(赤く;青く;黒く;白く;黄色く)
折れ線グラフの色を__Y__する
xdataとydataの折れ線グラフを描画して、色を__Y__する
'''

__X__ = 'r'
plt.plot(xdata, ydata, color=__X__)
'''
@test(plt=missing;xdata=ydata=alist;$$)
@X('r';'b';'k';'w';'y')
@Y(赤い;青い;黒い;白い;黄色い)
__Y__折れ線グラフを描画する
xdataとydataの__Y__折れ線グラフを描画する
'''

plt.plot(xdata, ydata, label=s)
'''
@test(plt=missing;xdata=ydata=alist;$$)
折れ線グラフのラベルをsに設定する
{xdataとydataの折れ線グラフを|sとラベル付けして}描画する
xdataとydataの折れ線グラフを描画して、sとラベル付けする
'''


plt.plot(xdata, ydata, linestyle=__X__)
'''
@test(plt=missing;xdata=ydata=alist;$$)
@X('dashed';'dashbot';'dotted';'solid')
@Y(破線;一点鎖線;点線;実線)
[__Y__グラフ|__Y__の折れ線グラフ]を描画する
折れ線グラフを__Y__に設定する
xdataとydata[の|について][__Y__グラフ|__Y__[|による|の]折れ線グラフ]を描画する
xdataとydataの折れ線グラフを描画して、__Y__に設定する
'''

plt.plot(xdata, ydata, linewidth=n)
'''
@test(plt=missing;xdata=ydata=alist;$$)
線幅nの折れ線グラフを描画する
折れ線グラフの線幅をnに設定する
xdataとydata[の|について]線幅nの折れ線グラフを描画する
xdataとydata[の|について]折れ線グラフを描画して、[その|]線幅をnに設定する
'''

plt.plot(xdata, ydata, linestyle=__X__, linewidth=n)
'''
@test(plt=missing;xdata=ydata=alist;$$)
線幅nの__Y__グラフを描画する
__Y__グラフの線幅をnに設定する
xdataとydata[の|について]線幅nの__Y__グラフを描画する
xdataとydata[の|について]__Y__グラフを描画して、[その|]線幅をnに設定する
'''

plt.plot(xdata, ydata, linestyle=__X__, color=rgb)
'''
@test(plt=missing;xdata=ydata=alist;rgb='#fff';$$)
__Y__グラフの色をrgbに設定する
__Y__グラフの色を[赤にする|赤くする|赤色に設定する]
xdataとydata[の|について]rgbの__Y__グラフを描画する
xdataとydata[の|について]__Y__グラフを描画して、[その|]色をrgbに設定する
'''

plt.plot(xdata, ydata, linestyle=__X__, color='r')
'''
@test(plt=missing;xdata=ydata=alist;$$)
@alt(赤い|赤色の)
赤い__Y__グラフを描画する
__Y__グラフの色を[赤にする|赤くする|赤色に設定する]
xdataとydata[の|について]赤い__Y__グラフを描画する
xdataとydata[の|について]__Y__グラフを描画して、[その|]色を[赤にする|赤くする|赤色に設定する]
'''

plt.plot(xdata, ydata, linestyle=__X__, color='b')
'''
@test(plt=missing;xdata=ydata=alist;$$)
@alt(青い|青色の)
青い__Y__グラフを描画する
__Y__グラフの色を[青にする|青くする|青色に設定する]
xdataとydata[の|について]青い__Y__グラフを描画する
xdataとydata[の|について]__Y__グラフを描画して、[その|]色を[青にする|青くする|青色に設定する]
'''

plt.plot(xdata, ydata, linestyle=__X__, color='k')
'''
@test(plt=missing;xdata=ydata=alist;$$)
@alt(黒い|黒色の)
黒い__Y__グラフを描画する
__Y__グラフの色を[黒にする|黒くする|黒色に設定する]
xdataとydata[の|について]黒い__Y__グラフを描画する
xdataとydata[の|について]__Y__グラフを描画して、[その|]色を[黒にする|黒くする|黒色に設定する]
'''

plt.plot(xdata, ydata, marker=__X__)
'''
@test(plt=missing;xdata=ydata=alist;$$)
@X('.';'o';'^';'v';'<';'>';'x';'X';'s';'D';'*')
@Y(ポイント;丸;[[|上]三角|▲|△];[下三角|▽|▼];左三角;右三角;[バツ|クロス];大バツ;四角;[ダイアモンド|菱形];星)
@alt(マーカー|印)
折れ線グラフに__Y__マーカーを使う
折れ線グラフのマーカーを__Y__に設定する
xdataとydataの折れ線グラフを描画して、マーカーを__Y__に設定する
xdataとydataの折れ線グラフに__Y__マーカーを描画する
'''

plt.plot(xdata, ydata, marker=__X__, markerfacecolor='r')
'''
@test(plt=missing;xdata=ydata=alist;$$)
xdataとydataの折れ線グラフに、赤い__Y__マーカーを描画する
折れ線グラフの__Y__マーカーを[赤くする|赤色にする]
'''

plt.plot(xdata, ydata, marker=__X__, markerfacecolor='b')
'''
@test(plt=missing;xdata=ydata=alist;$$)
xdataとydataの折れ線グラフに、青い__Y__マーカーを描画する
折れ線グラフの__Y__マーカーを[青くする|青色に設定する]
'''

plt.plot(xdata, ydata, marker=__X__, markerfacecolor='k')
'''
@test(plt=missing;xdata=ydata=alist;$$)
xdataとydataの折れ線グラフに、黒い__Y__マーカーを描画する
折れ線グラフの__Y__マーカーを[黒くする|黒色に設定する]
'''

plt.plot(xdata, ydata, marker=__X__, markerfacecolor='y')
'''
@test(plt=missing;xdata=ydata=alist;$$)
xdataとydataの折れ線グラフに、黄色い__Y__マーカーを描画する
折れ線グラフの__Y__マーカーを[黄色くする|黄色に設定する]
'''

plt.plot(xdata, ydata, marker=__X__, markerfacecolor='g')
'''
@test(plt=missing;xdata=ydata=alist;$$)
xdataとydataの折れ線グラフに、緑色の__Y__マーカーを描画する
折れ線グラフの__Y__マーカーを緑色に設定する
'''

plt.plot(xdata, ydata, marker=__X__, markersize=n)
'''
@test(plt=missing;xdata=ydata=alist;$$)
xdataとydataの折れ線グラフに、[大きさ|サイズ]nの__Y__マーカーを描画する
折れ線グラフの__Y__マーカーの[大きさ|サイズ]をnに設定する
'''

plt.plot(xdata, ydata, marker=__X__, markeredgewidth=n)
'''
@test(plt=missing;xdata=ydata=alist;$$)
xdataとydataの折れ線グラフに、線幅nの__Y__マーカーを描画する
折れ線グラフの__Y__マーカーの線幅をnに設定する
'''

# 散布図

plt.scatter(xdata, ydata)
'''
xdataを縦軸、ydataを横軸として、散布図を描画する
xdataとydata[について|の]散布図を描画する
'''

plt.scatter(xdata, ydata, s=n)
'''
xdataを縦軸、ydataを横軸として、大きさnの散布図を描画する
{xdataとydata[について|]の散布図を|大きさnで}描画する
xdataとydata[について|の]散布図を描画して、その大きさをnに設定する
'''

plt.plot(xdata, ydata, marker=__X__)
'''
@test(plt=missing;xdata=ydata=alist;$$)
@X('.';'o';'^';'v';'<';'>';'x';'X';'s';'D';'*')
@Y(ポイント;丸;[[|上]三角|▲|△];[下三角|▽|▼];左三角;右三角;[バツ|クロス];大バツ;四角;[ダイアモンド|菱形];星)
{散布図に|__Y__マーカーを}使う
{__Y__マーカーで_|散布図を}描画する
xdataとydata[について|の]散布図を描画して、マーカーを__Y__に設定する
xdataとydata[について|]の散布図に__Y__マーカーを描画する
'''

plt.plot(xdata, ydata, marker=__X__, c=rgb)
'''
@test(plt=missing;xdata=ydata=alist;$$)
{散布図に|rgbの__Y__マーカーを}使う
{rgbの__Y__マーカーで_|散布図を}描画する
{xdataとydata[について|]の散布図に|rgbの__Y__マーカーを}描画する
xdataとydata[について|の]散布図を描画して、__Y__マーカーの色をrgbに設定する
'''

plt.plot(xdata, ydata, marker=__X__, c='r')
'''
@test(plt=missing;xdata=ydata=alist;$$)
{散布図に|赤い__Y__マーカーを}使う
{赤い__Y__マーカーで_|散布図を}描画する
{xdataとydata[について|]の散布図に|赤い__Y__マーカーを}描画する
'''

plt.plot(xdata, ydata, marker=__X__, c='k')
'''
@test(plt=missing;xdata=ydata=alist;$$)
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
alistに応じて、散布図の色を変える
xdataとydata[について|]alist[の値|]に応じて、散布図の色を変える
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

plt.hist(xdata)
'''
@alt(ヒストグラム|[柱状図|柱状グラフ|度数分布図])
xdataのヒストグラムを描画する
{xdataを|ヒストグラムで_}描画する
xdataをヒストグラムにする
'''

plt.hist(df[col])
'''
dfのcol[について|の]ヒストグラムを描画する
{dfのcolを|ヒストグラムで_}描画する
{ヒストグラムを使って|dfのcolを}描画する
'''

plt.hist(xdata, alpha=0.5)
'''
ヒストグラムを半透明[に|化]する
[xdata[について|]の|]ヒストグラムを描画する際に半透明[に|化]にする
[xdata[について|]の|]ヒストグラムを描画して、半透明[に|化]にする
'''

plt.hist(xdata, alpha=x)
'''
ヒストグラムの透明度をxに設定する
[xdata[について|]の|]ヒストグラムを描画する際に、透明度をxに設定する
[xdata[について|]の|]ヒストグラムを描画して、透明度をxに設定する
'''

plt.hist(xdata, bins=n)
'''
@alt(ビン数|ビン[|の数]|区間[数|の数|])
{ビン数をnに設定して|xdataのヒストグラムを}描画する
ビン数nのヒストグラムを[xdataについて|]描画する
[xdata[について|]の|]ヒストグラムを描画する際にビン数をnに設定する
'''

plt.hist(xdata, range=(n, n2))
'''
@alt(範囲|区間|間)
{xdataのヒストグラムを|nからn2の範囲で}描画する
{nからn2の範囲のヒストグラムを用いて|xdataを}描画する
xdataをnからn2の範囲でヒストグラムにする
'''

plt.hist(xdata, density=True)
'''
[xdata[について|]の|]ヒストグラムを描画する際に合計を1にする
'''

plt.hist([xdata, ydata], color=['b', 'r'])
'''
{[xdataとydata[について|]の|]ヒストグラムを|[二つ|横に]並べて}描画する
'''

'''
plt.subplot(X, y, 2)
X行y列の2つ目のグラフ指定


# 描画



plt.boxplot(X)
Xについての[箱ひげ図|箱髭図|ボックスチャート]を描画する
Xを箱ひげ図で描画する
Xを箱ひげ図にする
{箱ひげ図を用いて}Xを描画する

plt.boxplot([X, Y])
XとYについての箱ひげ図を描画する
XとYを箱ひげ図に描画する
XとYを箱ひげ図にする
{箱ひげ図を用いて}XとYを描画する

plt.boxplot([X, Y, Z])
XとYとZについての箱ひげ図を描画する
XとYとZを箱ひげ図に描画する
XとYとZを箱ひげ図にする
{箱ひげ図を用いて}XとYとZを描画する

plt.boxplot(df['age'])
@type(df)において、@type('age')の箱ひげ図を描画する
@type(df)の@type('age')についての箱ひげ図を描画する
@type(df)の@type('age')を箱ひげ図に描画する
{箱ひげ図を用いて}@type(df)の@type('age')を描画する

plt.boxplot([df['G1'], df['G2'], df['G3']])
@type(df)の@type('G1', カラム)と@type('G2', カラム)と@type('G3', カラム)についての箱ひげ図を描画する
[同じグラフ内で|]@type(df)の@type('G1')と@type('G2')と@type('G3')を箱ひげ図で描画する
@type(df)の@type('G1')と@type('G2')と@type('G3')の箱ひげ図を一枚のグラフで描画する

sns.pairplot(df[['G1', 'G2', 'G3']])
@type(df)において、@type('G1')と@type('G2')と@type('G3')の関係性を[一気に|一度に]描画する
@type(df)の@type('G1')と@type('G2')と@type('G3')について関係性を一気に描画する

plt.bar(X, Y)
{横軸をX}としたYの[縦棒グラフ|縦向き棒グラフ|縦方向の棒グラフ|鉛直棒グラフ|垂直棒グラフ|棒グラフ]を描画する
{横軸をX}として、Yの縦棒グラフを描画する

plt.barh(X, Y)
{縦軸をX}としたYの[横棒グラフ|横向き棒グラフ|横方向の棒グラフ|水平棒グラフ|棒グラフ]を描画する
{縦軸をX}として、Yの横棒グラフを描画する

plt.bar(x, y, width = 0.5)
{グラフ幅を0.5}として、{横軸をx}としたyの[縦棒グラフ]を描画する
{棒と棒の隙間を0.5}として、{横軸をx}としたyの[縦向きの|]棒グラフを描画する

plt.bar(x, y, align='center')
棒グラフの位置を[真ん中として|中心に設定して]、{横軸をx}としたyの縦棒グラフを描画する
棒グラフの位置を真ん中として、xとyの縦棒グラフを描画する

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
