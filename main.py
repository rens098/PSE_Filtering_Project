import yfinance as yf
import pandas as pd
# dat = yf.Ticker("MSFT")
# dat.info
# dat.calendar
# dat.analyst_price_targets
# dat.quarterly_income_stmt
# dat.history(period='1mo')
# dat.option_chain(dat.options[0]).calls

stock_market_index = ['PSEI.PS', '^DJI']

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

df = pd.DataFrame({
    'tickersym' : get_stock_ticker(stock_market_index),
    'market' : get_stock_market(stock_market_index)
})

print(df)
