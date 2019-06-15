import quandl

class LoadReturn:
    def loadDailyReturn():
        quandl.ApiConfig.api_key='8xsHs-1vCFmLsqD5Sfpr'
        stocks =['AAPL','AMZN','GOOGL','FB']
        data =quandl.get_table('WIKI/PRICES', ticker=stocks, qopts={'columns': ['date', 'ticker', 'adj_close']}
                      , date ={'gte': '2017-1-1', 'lte': '2018-12-31'}, paginate=True)
        data.to_csv(r'C:\Users\Paul\Desktop\AI\Python\Learning\AssetAllocationRecommendation\ReturnData\DailyReturn.csv')
        
    loadDailyReturn()     
