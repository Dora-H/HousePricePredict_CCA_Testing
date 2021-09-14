import pandas as pd
import matplotlib.pyplot as mp
import seaborn as sns

data = pd.read_csv("./train.csv")
print(data.isnull().sum())
print(r'總紀錄筆數:{}'.format(data.shape[0]))
print(r'總紀錄Columns:{}'.format(data.shape[1]))  # 23


var_na = [col for col in data.columns if data[col].isnull().mean() > 0]
print('自變數（或是特徵）是有缺值的', var_na)
print('\n')

cca_var = [var for var in data.columns if data[var].isnull().mean() < 0.05]
print('篩選出小於5%的變數:', cca_var)
print('\n')

cca_df = data[cca_var].dropna()
print('移除小於5%的變數後', cca_df)

print(cca_df.shape[0], data.shape[0])
print('總共移除%d資料 ' % (data.shape[0]-cca_df.shape[0]))

sns.set(context='notebook', style='white')
mp.style.use("dark_background")
mp.title('Thresholds(SalePrice) < 0.05 (CCA) Original/After')
mp.hist(data['SalePrice'], color='blue', bins=50, label="Original")
mp.hist(data['SalePrice'], color='white', width=9000, bins=50, label="After")
mp.legend()
mp.show()
