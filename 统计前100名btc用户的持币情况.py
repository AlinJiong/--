# 即对比两个csv文件中数据的变化情况

import pandas as pd

data1 = pd.read_csv('btc前1000名钱包地址-2022.3.25.csv')
data2 = pd.read_csv('btc前1000名钱包地址-2022.3.24.csv')

data = pd.merge(data1, data2, on='地址')

data['余额变化'] = data.apply(lambda x: x['余额_x'] - x['余额_y'], axis=1)

data.to_csv('btc_diff.csv', encoding='utf-8')