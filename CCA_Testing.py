'''只要缺失值的比例只要超過5%就不建議採用CCA，
只要5%以下而且資料的缺失是隨機的就能使用CCA，
5%以上可能會破壞（Distort）那個變數的資料分布狀態'''

import pandas as pd
import matplotlib.pyplot as mp
import seaborn as sns

# 讀取訓練集
data = pd.read_csv("./train.csv")

# 使用isnull方法計算每個欄位的缺值 再用sum方法計算每個欄位總缺值數量
print(data.isnull().sum())
print(r'總紀錄筆數:{}'.format(data.shape[0]))
print(r'總紀錄Columns:{}'.format(data.shape[1]))  # 23

# 透過缺漏值的數量計算，總共有兩個欄位有缺值


# 自變數（或是特徵）是有缺值的
var_na = [col for col in data.columns if data[col].isnull().mean() > 0]
print('自變數（或是特徵）是有缺值的', var_na)
print('\n')
# 篩選出小於5%的變數
cca_var = [var for var in data.columns if data[var].isnull().mean() < 0.05]
print('篩選出小於5%的變數:', cca_var)
print('\n')

# 移除小於5%的變數
cca_df = data[cca_var].dropna()
print('移除小於5%的變數後', cca_df)
# 後前總共刪掉了多少資料
print(cca_df.shape[0], data.shape[0])
print('總共移除%d資料 ' % (data.shape[0]-cca_df.shape[0]))

# 來看一下CCA後的資料變動 : SaleCondition
sns.set(context='notebook', style='white')
mp.style.use("dark_background")
mp.title('Thresholds(SalePrice) < 0.05 (CCA) Original/After')
mp.hist(data['SalePrice'], color='blue', bins=50, label="Original")
mp.hist(data['SalePrice'], color='white', width=9000, bins=50, label="After")
mp.legend()
mp.show()