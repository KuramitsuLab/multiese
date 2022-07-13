import seaborn as sns

__X__ = 'iris'
'''
@X('iris';'tips';'titanic')
@Y([アヤメ|アイリス];チップ;タイタニック[号|])
'''

df = sns.load_dataset(__X__)
'''
__Y__のデータセットを[|データフレームとして]ロードする
__Y__のデータセットからデータフレームを[読み込む|ロードする]
'''
