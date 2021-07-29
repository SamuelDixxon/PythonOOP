class Stock():

    def __init__(self,  ticker, priceCurr, exists, hasDiv):
        # initializing all Stock attributes
        self.ticker = ticker
        self.priceCurr = priceCurr
        self.exists = exists
        self.hasDiv = hasDiv

    # getter methods / setter methods

    def getinfo(self):
        a = [self.ticker, self.priceCurr, self.exists, self.hasDiv]
        for i in range(len(a)-1):
            printf("{}".format(a[i]+"\n"))

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
