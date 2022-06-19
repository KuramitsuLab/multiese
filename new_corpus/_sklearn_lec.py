import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


説明変数 = df[['列名']]
'''
データフレームのひとつの[列|カラム][だけ|のみ|を]説明変数にする
'''

説明変数 = df[['列名', '列名2']]
'''
データフレームの[列|カラム]を説明変数にする
'''

説明変数 = df[df.columns[:-1]]
'''
データフレームの最後の[列|カラム]以外を[全て|]説明変数にする
'''

説明変数 = df[df.columns[1:]]
'''
データフレームの[先頭|最初]の[列|カラム]以外を[全て|]説明変数にする
'''

目的変数 = df['列名']
'''
データフレームの[列|カラム]を目的変数にする
'''

model = sklearn.linear_model.LinearRegression()
'''
@alt(線形回帰モデル=[線形回帰モデル|[単|重]回帰モデル|[線形|回帰]モデル])
@alt(用意する|準備する)
@alt(作る|[新規|]作成する)

[新しい|空の|]線形回帰モデルを[作る|用意する]
[線形|単|重|]回帰分析[の準備をする|を行う]
'''

normalize = True
'''
option: {説明変数を|事前に}正規化する
'''

fit_intercept = False
'''
option: [切片|バイアス]を[算出|計算]しない
'''

正則化項 = 0.1
model = sklearn.linear_model.Ridge(alpha=正則化項)
'''
[新しい|空の|]リッジ回帰モデルを[作る|用意する]
リッジ回帰分析[の準備をする|を行う]
'''

model = sklearn.linear_model.Rosso(alpha=正則化項)
'''
[新しい|空の|]ロッソ回帰モデルを[作る|用意する]
ロッソ回帰分析[の準備をする|を行う]
'''

model = sklearn.linear_model.ElasticNet()
'''
@alt(ハイブリッド|組み合わせた)

[新しい|空の|]リッジ回帰とロッソ回帰のハイブリットモデルを[作る|用意する]
リッジ回帰とロッソ回帰のハイブリッド分析[の準備をする|を行う]
正則化付き線形回帰モデルを[作る|用意する]
正則化付き[線形|単|重|]回帰分析[の準備をする|を行う]
'''


model.fit(説明変数, 目的変数)
'''
@alt(予測モデル=[モデル|[|線形|重|単]回帰モデル|分類モデル])
@alt(教師データ|データ|訓練データ)

予測モデルを[学習する|作る|訓練する]
{教師データで_|予測モデル}を学習する
{説明変数と目的変数で_|予測モデルを}学習する
予測モデルの[当てはめを実行する|訓練を開始する]
予測モデルを[当て|あて]はめる
'''

model.coef_
'''
@alt(回帰変数|係数)

線形[|回帰]モデルの回帰変数[|を得る]
'''

model.intercept_
'''
@alt(切片|バイアス)

線形[|回帰]モデルの切片[|を得る]
'''

model = sklearn.linear_model.LinearRegression(fit_intercept=False)
'''
切片なしの線形回帰モデルを[作る|用意する]
切片なしの[線形|単|重|]回帰分析[の準備をする|を行う]
'''

y_pred = model.predict(説明変数)
'''
予測モデルから目的変数を予測する
'''

pd.DataFrame({'実測': 目的変数, '予測': model.predict(説明変数)})
'''
@alt(実測値|目的変数)
{予測モデルの予測値と|実測値を}[比較する|対比させる]
'''

plt.scatter(目的変数, model.predict(説明変数))
'''
{予測モデルの予測値と|実測値を}散布図に描く
'''

目的変数 - model.predict(説明変数)
'''
予測モデルの残差を求める
'''

plt.hist(目的変数 - model.predict(説明変数))
'''
予測モデルの残差をヒストグラムにする
'''

sklearn.metrics.mean_absolute_error(データ列, データ列2)
'''
[データ列[間|]の|][平均絶対誤差|MAE]を求める
'''

np.sqrt(sklearn.metrics.mean_squared_error(データ列, データ列2))
'''
[データ列[間|]の|][平方根平均二乗誤差|RMSE]を求める
'''

sklearn.metrics.mean_squared_error(データ列, データ列2)
'''
[データ列[間|]の|]平均[二|２]乗誤差を求める
[MSE|Mean Squared Error]を求める 
'''

sklearn.metrics.mean_squared_error(目的変数, model.predict(説明変数))
'''
予測モデルの[平均[二|２]乗誤差|精度|正確さ]を求める
'''

sklearn.metrics.r2_score(データ列, データ列2)
'''
@alt(決定係数|R2|[当て|あて]はまりの良さ|寄与率)
[データ列[間|]の|]決定係数を求める
'''

sklearn.metrics.r2_score(目的変数, model.predict(説明変数))
'''
予測モデルの[当てはまりの良さ|決定係数]を求める
'''

X_train, X_test, y_train, y_test = train_test_split(説明変数, 目的変数, test_size=0.3)
'''
ホールドアウト[法|]を使う
訓練データとテストデータに分割する
'''


sklearn.model_selection.cross_val_score(model, 説明変数, 目的変数, cv=5, scoring='r2')
'''
@alt(交差検証|クロスバリデーション)
回帰モデルを交差検証する
'''


model = sklearn.tree.DecisionTreeRegressor()
'''
[新しい|空の|]回帰木モデルを[作る|用意する]
回帰木分析[の準備をする|を行う]
'''

sklearn.tree.plot_tree(model, feature_names=X.columns, filled=True)
'''
@alt(決定木|回帰木|分類木)

決定木を表示する
決定木を[可視化|グラフ[化|に]]する
'''

plt.barh(X.columns, model.feature_importances_)
'''
@alt(決定木|回帰木|分類木)

決定木の重要度を表示する
決定木の重要度を[可視化|グラフ[化|に]]する
'''

n = 2

maxdepth = n
'''
option: [決定木の|][深さを制限する|最大深さを設定する]
'''

# クラス分類

model = sklearn.linear_model.LogisticRegression()
'''
[新しい|空の|]ロジスティック回帰モデルを[作る|用意する]
線形のクラス分類[をする|を行う]
'''

混同行列 = sklearn.metrics.confusion_matrix(正解データ列, 予測データ列)
'''
@alt(クラス分類結果=[クラス分類|[分類|予測]結果|分類モデル])

クラス分類結果の[予測精度|偽陽性|偽陰性|真陽性|真陰性]を見る
[予測データの|][混同行列|コンフュージョン・マトリックス]を[求める|算出する]
'''

sns.heatmap(混同行列, annot=True, cmap='Reds')
'''
{混同行列を|ヒートマップで_}確認する
'''

sns.heatmap(confusion_matrix(正解データ列, 予測データ列), annot=True, cmap='Reds')
'''
{クラス分類の[予測精度|偽陽性|偽陰性]を|ヒートマップで_}見る
'''

sklearn.metrics.accuracy_score(正解データ列, 予測データ列)
'''
クラス分類結果の[正解率|正確さ|アキュレシー|分類精度]を求める 
'''

sklearn.metrics.precision_score(正解データ列, 予測データ列)
'''
クラス分類結果の[適合率|PPV]を求める 
偽陽性を[避けたい|抑えたい]指標を使う
'''

sklearn.metrics.recall_score(正解データ列, 予測データ列)
'''
クラス分類結果の[再現率|リコール|真陽性率|感度]を求める 
偽陰性を[避けたい|抑えたい]指標を使う
'''

sklearn.metrics.f1_score(正解データ列, 予測データ列)
'''
クラス分類結果の[F値|適合率と再現率の調和平均]を求める 
'''


# 回帰

model = sklearn.ensemble.RandomForestRegressor()
'''
{ランダムフォレストで|回帰分析を}[行う|する]
'''

model = sklearn.ensemble.ExtraTreeRegressor(n_estimators=10)
'''
{ランダム性を追加したランダムフォレストで|回帰分析を}[行う|する]
'''

model = sklearn.svm.SVR(kernel='rbf', C=1e3, gamma=0.1, epsilon=0.1)
'''
[|新しい]サポートベクター回帰モデルを[作る|用意する]
{サポートベクターマシンで_|回帰分析を}[行う|する]
'''

model = sklearn.gaussian_process.GaussianProcessRegressor()
'''
[|新しい|空の]ガウス過程回帰モデルを[作る|用意する]
{ガウス過程で_|回帰分析を}[行う|する]
'''

model = sklearn.neighbors.KNeighborsRegressor(n_neighbors=5)
'''
{[K最近傍法|KNN]で_|回帰分析を}[行う|する]
'''

model = sklearn.linear_model.SGDRegressor()
'''
{[確率的勾配降下|SDG]で_|回帰分析を}[行う|する]
'''

model = sklearn.neural_network.MLPRegressor(hidden_layer_sizes=(10, 10))
'''
{[パーセプトロン|ニューラルネット|多層パーセプトロン|MLP]で_|回帰分析を}[行う|する]
'''

model = sklearn.cross_decomposition.PLSRegression(n_components=10)
'''
[|新しい|空の]部分的最小二乗回帰モデルを[作る|用意する]
{[部分的最小二乗法|PLS]で_|回帰分析を}[行う|する]
'''

model = sklearn.linear_model.RANSACRegressor(random_state=0)
'''
[|新しい|空の]ロバスト回帰モデルを[作る|用意する]
{[ロバスト推定|RANSAC]で_|回帰分析を}[行う|する]
'''

model = sklearn.linear_model.HuberRegressor()
'''
[ロバストな|外れ値に強い]線形回帰モデルを[作る|用意する]
[ロバストな|外れ値に強い][線形|単|重|]回帰分析[の準備をする|を行う]
'''

model = sklearn.ensemble.GradientBoostingRegressor()
'''
[|新しい|空の]勾配ブースティング回帰木を[作る|用意する]
{勾配ブースティングで_|回帰分析を}[行う|する]
'''

model = sklearn.ensemble.HistGradientBoostingRegressor()
'''
[|新しい|空の]ヒストグラムベースの勾配ブースティング回帰木を[作る|用意する]
{ヒストグラムと勾配ブースティングで_|回帰分析を}[行う|する]
'''

model = sklearn.ensemble.AdaBoostRegressor(random_state=0, n_estimators=100)
'''
{ブースティングで_|回帰分析を}[行う|する]
'''

model = sklearn.ensemble.BaggingRegressor(n_estimators=10)
'''
{バギングで_|回帰分析を}[行う|する]
'''

sklearn.ensemble.VotingRegressor()
'''
{アンサンブル学習で_|回帰分析を}[行う|する]
'''

sklearn.ensemble.StackingRegressor()
'''
{スタッキングで_|回帰分析を}[行う|する]
'''

# 分類器

model = sklearn.ensemble.RandomForestClassifier()
'''
{ランダムフォレストで|クラス分類を}[行う|する]
'''

model = sklearn.ensemble.ExtraTreeClassifier(n_estimators=10)
'''
{[ランダム性を強化した|よりランダムな]ランダムフォレストで|クラス分類を}[行う|する]
'''

model = sklearn.svm.SVR(kernel='rbf', C=1e3, gamma=0.1, epsilon=0.1)
'''
@alt(分類モデル|分類器)

[|新しい]サポート[ベクター|ベクトル]分類モデルを[作る|用意する]
{サポートベクターマシンで_|クラス分類を}[行う|する]
'''

model = sklearn.gaussian_process.GaussianProcessClassifier()
'''
[|新しい|空の]ガウス過程分類モデルを[作る|用意する]
{ガウス過程で_|クラス分類を}[行う|する]
'''

model = sklearn.neighbors.KNeighborsClassifier(n_neighbors=5)
'''
{[K最近傍法|KNN]で_|クラス分類を}[行う|する]
'''

model = sklearn.linear_model.SGDClassifier()
'''
{[確率的勾配降下|SDG]で_|クラス分類を}[行う|する]
'''

model = sklearn.neural_network.MLPClassifier(hidden_layer_sizes=(10, 10))
'''
{[パーセプトロン|ニューラルネット|多層パーセプトロン|MLP]で_|クラス分類を}[行う|する]
'''

model = sklearn.linear_model.RANSACClassifier(random_state=0)
'''
[|新しい|空の]ロバスト分類モデルを[作る|用意する]
{[ロバスト推定|RANSAC]で_|クラス分類を}[行う|する]
'''

model = sklearn.linear_model.HuberClassifier()
'''
[ロバストな|外れ値に強い]線形分類モデルを[作る|用意する]
[ロバストな|外れ値に強い][線形|単|重|]クラス分類[の準備をする|を行う]
'''

model = sklearn.ensemble.GradientBoostingClassifier()
'''
[|新しい|空の]勾配ブースティング分類木を[作る|用意する]
{勾配ブースティングで_|クラス分類を}[行う|する]
'''

model = sklearn.ensemble.HistGradientBoostingClassifier()
'''
[|新しい|空の]ヒストグラムベースの勾配ブースティング分類木を[作る|用意する]
{ヒストグラムと勾配ブースティングで_|クラス分類を}[行う|する]
'''

model = sklearn.ensemble.AdaBoostClassifier(random_state=0, n_estimators=100)
'''
{ブースティングで_|クラス分類を}[行う|する]
'''

model = sklearn.ensemble.BaggingClassifier(n_estimators=10)
'''
{バギングで_|クラス分類を}[行う|する]
'''

sklearn.ensemble.VotingClassifier()
'''
{アンサンブル学習で_|クラス分類を}[行う|する]
'''

sklearn.ensemble.StackingClassifier()
'''
{スタッキングで_|クラス分類を}[行う|する]
'''


# 教師なし

model = sklearn.decomposition.PCA(n_components=n)
'''
[主成分分析|固有値分解|因子分析|スペクトル分解][を行う|の準備をする]
'''

__X__ = 2
sklearn.decomposition.PCA(n_components=__X__).fit_transform(多次元データ)
'''
@X(2;3;N)
@X(二;三;N)
{[多次元データを|]|主成分分析で_}__Y__次元に[次元|]削減する
'''

model = sklearn.decomposition.TruncatedSVD(n_components=n)
'''
[特異値分解|SVD][を行う|の準備をする]
'''

sklearn.decomposition.TruncatedSVD(n_components=__X__).fit_transform(多次元データ)
'''
{[多次元データを|]|[特異値分解|SVD]で_}__Y__次元に[次元|]削減する
'''

model = sklearn.manifold.MSD(n_components=n)
'''
[多次元尺度構成法|MSD][を行う|の準備をする]
'''

sklearn.manifold.MSD(n_components=__X__).fit_transform(多次元データ)
'''
{[多次元データを|]|[多次元尺度構成法|MSD]で_}__Y__次元に[次元|]削減する
'''

model = sklearn.manifold.TSNE(n_components=n)
'''
[[フィッシャーの|]線形判別分類|t-SNE|t分布型確率的近傍埋め込み法][を行う|の準備をする]
'''

sklearn.manifold.TSNE(n_components=__X__).fit_transform(多次元データ)
'''
{[多次元データを|]|[t-SNE|t分布型確率的近傍埋め込み法]で_}__Y__次元に[次元|]削減する
'''

sklearn.preprocessing.StandardScaler().fit_transform(データ)
'''
@alt(スケール変換|スケーリング)

[データを|][標準化|スケール変換]する
{[データを|]|平均と分散で_}標準化を行う
'''

sklearn.preprocessing.RobustScaler().fit_transform(データ)
'''
[データを|]外れ値に[頑健な|ロバストな]標準化を行う
{[データを|]|四分位点で_}[標準化|スケール変換]する
'''

sklearn.preprocessing.MaxAbsScaler().fit_transform(データ)
'''
{[データを|]|最大値で_}正規化[する|を行う]
'''

sklearn.preprocessing.MinMaxScaler().fit_transform(データ)
'''
{[データを|]|[最大値と最小値|最大最小]で_}正規化[する|を行う]
{[データを|]|[最大最小値|最大最小]で_}[標準化|スケール変換]する
'''

sklearn.preprocessing.MinMaxScaler(feature_range=(0, 1)).fit_transform(データ)
'''
{[データを|]|[最大値と最小値|最大最小]で_}[正規化する|揃える]
'''

np.log(データ列)
'''
データ列[の偏り|]を対数変換する
'''

np.sqrt(データ列)
'''
データ列[の偏り|]を平方根変換する
'''

sklearn.preprocessing.Normalizer(norm="l1").fit_transform(データ)
'''
{[データを|]|L1ノルムで_}正則化[する|を行う]
'''

sklearn.preprocessing.Normalizer(norm="l2").fit_transform(データ列)
'''
{[データを|]|L2ノルムで_}正規化[する|を行う]
データ列のノルムを[揃える|そろえる]
'''

sklearn.preprocessing.Binarizer(threshold=閾値).fit_transform(データ列)
'''
{[データ列を|]|[閾値|指定した値]で_}[二値化|バイナリ化]する
'''

sklearn.preprocessing.LabelEncoder().fit_transform(データ列)
'''
[カテゴリ|非数値]データ[列|]を[数値|連番]化する
[カテゴリ|非数値]データ[列|]を連番に変換する
'''

sklearn.preprocessing.OneHotEncoder(sparse=False).fit_transform(データ列)
'''
[カテゴリ|非数値]データ[列|]を[ワン・ホット|]ベクトル化する
'''
