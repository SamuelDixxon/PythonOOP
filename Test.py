from StockClass import Stock
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf

abc = Stock('AAPL', 144.98, True, True)


tickerData = yf.Ticker(abc.ticker)

tickerDf = tickerData.history(period='1m', start='2010-1-1', end='2021-1-1')


plt.plot(tickerDf.index, tickerDf['Close'])
plt.title(abc.ticker + " '2021-1-1 throw 2021-1-25")
plt.show()
