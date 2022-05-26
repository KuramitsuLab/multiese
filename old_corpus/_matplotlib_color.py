import matplotlib.pyplot as plt

データ列=[1,2,3]
データ列2=[2,3,4]

#blue;green;red;cyan;magenta;yellow;black;white
#青;緑;赤;シアン;赤紫;黄色;黒;白

__X__= 'r'

color = __X__
'''
@X('aliceblue';'antiquewhite';'aqua';'aquamarine';'azure';'beige';'bisque';'black';'blanchedalmond';'blue';'blueviolet';'brown';'burlywood';'cadetblue';'chartreuse';'chocolate';'coral';'cornflowerblue';'cornsilk';'crimson';'cyan';'darkblue';'darkcyan';'darkgoldenrod';'darkgray';'darkgreen';'darkgrey';'darkkhaki';'darkmagenta';'darkolivegreen';'darkorange';'darkorchid';'darkred';'darksalmon';'darkseagreen';'darkslateblue';'darkslategray';'darkslategrey';'darkturquoise';'darkviolet';'deeppink';'deepskyblue';'dimgray';'dimgrey';'dodgerblue';'firebrick';'floralwhite';'forestgreen';'fuchsia';'gainsboro';'ghostwhite';'gold';'goldenrod';'gray';'green';'greenyellow';'grey';'honeydew';'hotpink';'indianred';'indigo';'ivory';'khaki';'lavender';'lavenderblush';'lawngreen';'lemonchiffon';'lightblue';'lightcoral';'lightcyan';'lightgoldenrodyellow';'lightgray';'lightgreen';'lightgrey';'lightpink';'lightsalmon';'lightseagreen';'lightskyblue';'lightslategray';'lightslategrey';'lightsteelblue';'lightyellow';'lime';'limegreen';'linen';'magenta';'maroon';'mediumaquamarine';'mediumblue';'mediumorchid';'mediumpurple';'mediumseagreen';'mediumslateblue';'mediumspringgreen';'mediumturquoise';'mediumvioletred';'midnightblue';'mintcream';'mistyrose';'moccasin';'navajowhite';'navy';'oldlace';'olive';'olivedrab';'orange';'orangered';'orchid';'palegoldenrod';'palegreen';'paleturquoise';'palevioletred';'papayawhip';'peachpuff';'peru';'pink';'plum';'powderblue';'purple';'rebeccapurple';'red';'rosybrown';'royalblue';'saddlebrown';'salmon';'sandybrown';'seagreen';'seashell';'sienna';'silver';'skyblue';'slateblue';'slategray';'slategrey';'snow';'springgreen';'steelblue';'tan';'teal';'thistle';'tomato';'turquoise';'violet';'wheat';'white';'whitesmoke';'yellow';'yellowgreen')
@Y(アリスブルー;アンティークホワイト;アクア;アクアマリン;紺碧;ベージュ;ビスク;ブラック;ブランチドアーモンド;青;ブルーバイオレット;[茶色|ブラウン];バリーウッド;カデットブルー;[シャルトリューズ|黄緑];チョコレート;[コーラル|珊瑚];[コーンフラワーブルー|やわらかい青];コーンズシルク;[クリムゾン|真紅|深紅];シアン;[紺|ダークブルー|濃い青];[ダーク|濃い]シアン;ダークゴールデンロッド;ダークグレー;ダークグリーン;ダークグレー;ダークカーキ;ダークマゼンタ;ダークオリーブグリーン;ダークオレンジ;ダークオーキッド;[暗い赤|ダークレッド];ダークサーモン;ダークシアグリーン;ダークスレートブルー;ダークスラテグレー;ダーク・スラテグレー;ダークターコイズ;ダークバイオレット;デピンク;ディープスカイブルー;ディムグレー;ディムグレー;ドジャーブルー;耐火レンガ;フローラルホワイト;フォレストグリーン;フクシア;ゲインズボロ;ゴーストホワイト;ゴールド;ゴールデンロッド;グレー;グリーン;グリーンイエロー;グレー;ハニーデュー;ホットピンク;インディアンレッド;インディゴ;アイボリー;カーキ;ラベンダー;ラベンダーブラッシュ;ローングリーン;レモンシフォン;ライトブルー;ライトコーラル;ライトシアン;ライトゴールドロディイエロー;ライトグレー;ライトグリーン;ライトグレー;淡いピンク色;ライトサーモン;ライトグリーン;ライトスカイブルー;ライトスレイグレー;ライトスレイグレー;ライトスチールブルー;ライトイエロー;ライム;ライムグリーン;リネン;マゼンタ;マルーン;ミディアムアクアマリン;ミディアムブルー;ミディアムオーキッド;ミディアムパープル;ミディアムシアグリーン;ミディアムスレートブルー;ミディアムスプリンググリーン;ミディアムターコイズ;ミディアムバイオレットレッド;ミッドナイトブルー;ミントクリーム;ミスティローズ;モカシン;ナバホホワイト;ネイビー;オールドレース;オリーブ;オリベドラブ;オレンジ;オレンジレッド;オーキッド;パールゴールデンロッド;ペールグリーン;パレットトルコイズ;パールバイオレットレッド;パパイヤウィップ;ピーチパフ;ペルー;ピンク;プラム;パウダーブルー;パープル;レベッカパープル;赤;ロージーブラウン;ロイヤルブルー;サドルブラウン;サーモン;サンディーブラウン;シーグリーン;貝殻;シエナ;シルバー;スカイブルー;スレートブルー;スラグレー;スラグレー;スノー;スプリンググリーン;スチールブルー;[タン|淡い茶色];[青緑|ティール];シスル;トマト;[ターコイズ|青緑];[青紫|バイオレット];小麦色;[白|ホワイト];ホワイトスモーク;黄色;イエローグリーン)

[オプションで、|]__Y__[色|]を使う
[オプションで、|]{[グラフの|]色を|__Y__に}設定する
'''

plt.plot(データ列, データ列2, color=__X__)
'''
[折れ|]線グラフの色を__Y__に設定する
__Y__色の[|折れ]線グラフを描画する
[折れ|]線グラフを描画して、[その|]色を__Y__に設定する
'''

plt.hist(データ列, color=__X__)
'''
{ヒストグラムの色を|__Y__に}設定する
__Y__色のヒストグラムを描画する
ヒストグラムを描画して、[その|]色を__Y__に設定する
'''

## 赤くする

__X__ = 'r'

plt.plot(データ列, データ列2, color=__X__)
'''
@X('r';'b';'k';'w';'y')
@Y(赤く;青く;黒く;白く;黄色く)

[折れ|]線グラフの色を__Y__する
[折れ|]線グラフを描画して、色を__Y__する
'''

plt.hist(データ列, color=__X__)
'''
ヒストグラムの色を__Y__する
ヒストグラムを描画して、色を__Y__する
'''

## 赤い

plt.plot(データ列, データ列2, color=__X__)
'''
@X('r';'b';'k';'w';'y')
@Y(赤い;青い;黒い;白い;黄色い)

__Y__[折れ|]線グラフを描画する
'''

plt.hist(データ列, color=__X__)
'''
__Y__ヒストグラムを描画する
'''

###カラーマップ

plt.get_cmap("カラーマップ名")
'''
名前からカラーマップを得る
'''

plt.hist(データ列, color=plt.get_cmap("Spectral"))
'''
{ヒストグラムを|カラーマップで_}描画する
ヒストグラム[で|に]カラーマップを使う
'''
