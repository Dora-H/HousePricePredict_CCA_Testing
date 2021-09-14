# HousePricePredict_CCA_Testing
只要缺失值的比例只要超過5%就不建議採用CCA，
只要5%以下而且資料的缺失是隨機的就能使用CCA，
5%以上可能會破壞（Distort）那個變數的資料分布狀態'''


## Requirements
● Python 3.8    
● pandas  
● matplotlib    
● seaborn


#### Read data(train.csv)
    data = pd.read_csv("./train.csv")


#### use isnull() method to sum up
    print(data.isnull().sum())
    print(r'總紀錄筆數:{}'.format(data.shape[0]))
    print(r'總紀錄Columns:{}'.format(data.shape[1]))


#### find those var is null(and < mean)
    var_na = [col for col in data.columns if data[col].isnull().mean() > 0]
    print('自變數（或是特徵）是有缺值的', var_na)
    print('\n')


#### find those var < 0.05
    cca_var = [var for var in data.columns if data[var].isnull().mean() < 0.05]
    print('篩選出小於5%的變數:', cca_var)
    print('\n')


#### delete var < 0.05
    cca_df = data[cca_var].dropna()
    print('移除小於5%的變數後', cca_df)


#### check how much data is deleted
    print(cca_df.shape[0], data.shape[0])
    print('總共移除%d資料 ' % (data.shape[0]-cca_df.shape[0]))


#### have a look how CCA changes before/after, eg:SaleCondition
    sns.set(context='notebook', style='white')
    mp.style.use("dark_background")
    mp.title('Thresholds(SalePrice) < 0.05 (CCA) Original/After')
    mp.hist(data['SalePrice'], color='blue', bins=50, label="Original")
    mp.hist(data['SalePrice'], color='white', width=9000, bins=50, label="After")
    mp.legend()
    mp.show()


#### Show data visualization
![SalePrice_CCA](https://user-images.githubusercontent.com/70878758/133231024-f45991da-c5b0-45fd-a0a2-968f9f55a0dc.png)

#### Show data visualization with animation
![Figure_2](https://user-images.githubusercontent.com/70878758/133233483-e27ad6e0-7bfb-4e22-848e-5291eb90ea87.gif)
