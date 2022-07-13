import numpy as np
import pandas as pd

iterable = [1, 2, 1, 3]
リスト = [1, 2, 1, 3]
配列 = np.array([1, 2, 1, 3])

__X__ = iterable
'''
@X(iterable;リスト;配列)
@Y(イテラブル;リスト;配列)
'''

pd.get_dummies(__X__)
'''
__Y__をダミー変数に変換する
'''
