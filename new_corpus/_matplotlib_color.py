import matplotlib
import matplotlib.pyplot as plt

データ列x = [1, 2, 3]
データ列y = [2, 3, 4]


matplotlib.colors.cnames
'''
グラフで[使える|利用可能な]色[名|]の一覧[|を得る|を知る]
色名とカラーコードの対応表を得る
'''

色名 = 'red'

matplotlib.colors.cnames[色名]
'''
[色名からカラーコードを得る|色名をからコードに変換する]
'''

# アルファ値

alpha = 0.5
'''
@alt(透明度|アルファ[|値])

option: [色を|表示を|]半透明にする
option: 色の透明度を設定する
'''

plt.plot(データ列x, データ列y, alpha=0.5)
'''
折れ線グラフの透明度を設定する
折れ線グラフを半透明にする
'''

plt.hist(データ列x, alpha=0.5)
'''
ヒストグラムを半透明[に|化]する
ヒストグラムを描画して、半透明[に|化]にする
'''

# blue;green;red;cyan;magenta;yellow;black;white
# 青;緑;赤;シアン;赤紫;黄色;黒;白

__X__ = 'r'
'''
@X('aliceblue';'antiquewhite';'aqua';'aquamarine';'azure';'beige';'bisque';'black';'blanchedalmond';'blue';'blueviolet';'brown';'burlywood';'cadetblue';'chartreuse';'chocolate';'coral';'cornflowerblue';'cornsilk';'crimson';'cyan';'darkblue';'darkcyan';'darkgoldenrod';'darkgray';'darkgreen';'darkgrey';'darkkhaki';'darkmagenta';'darkolivegreen';'darkorange';'darkorchid';'darkred';'darksalmon';'darkseagreen';'darkslateblue';'darkslategray';'darkslategrey';'darkturquoise';'darkviolet';'deeppink';'deepskyblue';'dimgray';'dimgrey';'dodgerblue';'firebrick';'floralwhite';'forestgreen';'fuchsia';'gainsboro';'ghostwhite';'gold';'goldenrod';'gray';'green';'greenyellow';'grey';'honeydew';'hotpink';'indianred';'indigo';'ivory';'khaki';'lavender';'lavenderblush';'lawngreen';'lemonchiffon';'lightblue';'lightcoral';'lightcyan';'lightgoldenrodyellow';'lightgray';'lightgreen';'lightgrey';'lightpink';'lightsalmon';'lightseagreen';'lightskyblue';'lightslategray';'lightslategrey';'lightsteelblue';'lightyellow';'lime';'limegreen';'linen';'magenta';'maroon';'mediumaquamarine';'mediumblue';'mediumorchid';'mediumpurple';'mediumseagreen';'mediumslateblue';'mediumspringgreen';'mediumturquoise';'mediumvioletred';'midnightblue';'mintcream';'mistyrose';'moccasin';'navajowhite';'navy';'oldlace';'olive';'olivedrab';'orange';'orangered';'orchid';'palegoldenrod';'palegreen';'paleturquoise';'palevioletred';'papayawhip';'peachpuff';'peru';'pink';'plum';'powderblue';'purple';'rebeccapurple';'red';'rosybrown';'royalblue';'saddlebrown';'salmon';'sandybrown';'seagreen';'seashell';'sienna';'silver';'skyblue';'slateblue';'slategray';'slategrey';'snow';'springgreen';'steelblue';'tan';'teal';'thistle';'tomato';'turquoise';'violet';'wheat';'white';'whitesmoke';'yellow';'yellowgreen')
@Y(アリスブルー;アンティークホワイト;アクア;アクアマリン;紺碧;ベージュ;ビスク;ブラック;ブランチドアーモンド;青;ブルーバイオレット;[茶色|ブラウン];バリーウッド;カデットブルー;[シャルトリューズ|黄緑];チョコレート;[コーラル|珊瑚];[コーンフラワーブルー|やわらかい青];コーンズシルク;[クリムゾン|真紅|深紅];シアン;[紺|ダークブルー|濃い青];[ダーク|濃い]シアン;ダークゴールデンロッド;ダークグレー;ダークグリーン;ダークグレー;ダークカーキ;ダークマゼンタ;ダークオリーブグリーン;ダークオレンジ;ダークオーキッド;[暗い赤|ダークレッド];ダークサーモン;ダークシアグリーン;ダークスレートブルー;ダークスラテグレー;ダーク・スラテグレー;ダークターコイズ;ダークバイオレット;デピンク;ディープスカイブルー;ディムグレー;ディムグレー;ドジャーブルー;耐火レンガ;フローラルホワイト;フォレストグリーン;フクシア;ゲインズボロ;ゴーストホワイト;ゴールド;ゴールデンロッド;グレー;グリーン;グリーンイエロー;グレー;ハニーデュー;ホットピンク;インディアンレッド;インディゴ;アイボリー;カーキ;ラベンダー;ラベンダーブラッシュ;ローングリーン;レモンシフォン;ライトブルー;ライトコーラル;ライトシアン;ライトゴールドロディイエロー;ライトグレー;ライトグリーン;ライトグレー;淡いピンク色;ライトサーモン;ライトグリーン;ライトスカイブルー;ライトスレイグレー;ライトスレイグレー;ライトスチールブルー;ライトイエロー;ライム;ライムグリーン;リネン;マゼンタ;マルーン;ミディアムアクアマリン;ミディアムブルー;ミディアムオーキッド;ミディアムパープル;ミディアムシアグリーン;ミディアムスレートブルー;ミディアムスプリンググリーン;ミディアムターコイズ;ミディアムバイオレットレッド;ミッドナイトブルー;ミントクリーム;ミスティローズ;モカシン;ナバホホワイト;ネイビー;オールドレース;オリーブ;オリベドラブ;オレンジ;オレンジレッド;オーキッド;パールゴールデンロッド;ペールグリーン;パレットトルコイズ;パールバイオレットレッド;パパイヤウィップ;ピーチパフ;ペルー;ピンク;プラム;パウダーブルー;パープル;レベッカパープル;赤;ロージーブラウン;ロイヤルブルー;サドルブラウン;サーモン;サンディーブラウン;シーグリーン;貝殻;シエナ;シルバー;スカイブルー;スレートブルー;スラグレー;スラグレー;スノー;スプリンググリーン;スチールブルー;[タン|淡い茶色];[青緑|ティール];シスル;トマト;[ターコイズ|青緑];[青紫|バイオレット];小麦色;[白|ホワイト];ホワイトスモーク;黄色;イエローグリーン)
'''

color = __X__
'''
option: __Y__[色|]を使う
option: {[グラフの|フォントの|]色を|__Y__に}設定する
'''

markerfacecolor = __X__
'''
option: マーカーの色を__Y__にする
'''

plt.plot(データ列x, データ列y, color=__X__)
'''
[折れ|]線グラフの色を__Y__に設定する
__Y__色の[|折れ]線グラフを描画する
{[折れ|]線グラフを|__Y__色で_}描画する
'''

plt.hist(データ列, color=__X__)
'''
{ヒストグラムの色を|__Y__に}設定する
__Y__色のヒストグラムを描画する
{ヒストグラムを|__Y__色で_}描画する
'''

plt.scatter(データ列x, データ列y, color=__X__)
'''
散布図の色を__Y__にする
__Y__色の散布図を描画する
{散布図を|__Y__色で_}描画する
'''

plt.bar(データ列x, データ列y, color=__X__)
'''
[|縦]棒グラフの色を__Y__にする
__Y__色の[|縦]棒グラフを描画する
{[|縦]棒グラフを|__Y__色で_}描画する
'''

plt.barh(データ列x, データ列y, color=__X__)
'''
横棒グラフの色を__Y__にする
__Y__色の横棒グラフを描画する
{横棒グラフを|__Y__色で_}描画する
'''
