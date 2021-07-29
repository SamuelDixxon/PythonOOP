class Stock:

    def __init__(self,  ticker, priceCurr, exists, hasDiv):
        # initializing all Stock attributes
        self.ticker = ticker
        self.priceCurr = priceCurr
        self.exists = exists
        self.hasDiv = hasDiv

    # getter methods / setter methods

    def getinfo(self):
        a = {'Ticker: ': self.ticker, 'Current Price: ': self.priceCurr,
             'Stock Exists': self.exists, 'Has a Dividend: ': self.hasDiv}
        for key, val in a.items():
            print("{} {}".format(key, val))

 # test 123

    def __str__(self):
        print(f"ticker: {self.ticker}")
        print(f"current price: {self.priceCurr}")
        print(f"exists: {self.exists}")
        print(f"has dividend: {self.hasDiv}")

    def getpriceCurr(self):
        return self.priceCurr

    def getticker(self):
        return self.ticker

    def stockexists(self):
        return self.exists

    def divexists(self):
        return self.hasDiv

    def setprice(self, newprice):
        self.priceCurr = newprice

    def setticker(self, newticker):
        self.ticker = newticker

    def setexists(self, change):
        self.exists = change

    def sethasdiv(self, change):
        self.hasDiv = change
