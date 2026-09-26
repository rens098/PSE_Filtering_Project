import yfinance as yf # type: ignore
import pandas as pd # type: ignore
# dat = yf.Ticker("MSFT")
# dat.info
# dat.calendar
# dat.analyst_price_targets
# dat.quarterly_income_stmt
# dat.history(period='1mo')
# dat.option_chain(dat.options[0]).calls

stock_market_index = ['PSEI.PS', '^DJI','^GSPC','^IXIC','DAX','^FTSE','^N225','^HSI']

def get_stock_ticker(code):
    lst = []
    for i in code:
        dat = yf.Ticker(i)
        lst.append(dat.info['symbol'])
    return lst

def get_stock_market(code):
    lst = []
    for i in code:
        dat = yf.Ticker(i)
        lst.append(dat.info['market'])
    return lst

def get_stock_longname(code):
    lst = []
    for i in code:
        dat = yf.Ticker(i)
        lst.append(dat.info['longName'])
    return lst

def get_stock_curr(code):
    lst = []
    for i in code:
        dat = yf.Ticker(i)
        lst.append(dat.info['currency'])
    return lst

df = pd.DataFrame({
    'tickersym' : get_stock_ticker(stock_market_index),
    'market' : get_stock_market(stock_market_index),
    'longName': get_stock_longname(stock_market_index),
    'curreny': get_stock_curr(stock_market_index),
    'timeStamp': pd.Timestamp.now()
})

print(df)

dat = yf.Ticker('PSEI.PS')
#print(dat.info)

