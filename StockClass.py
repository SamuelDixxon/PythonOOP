class Stock():

    def __init__(self,  ticker, priceCurr, exists):
        # initializing all Stock attributes
        self.ticker = ticker
        self.priceCurr = priceCurr
        self.exists = exists

    # getter methods / setter methods

    def getpriceCurr(self):
        return self.priceCurr

    def getticker(self):
        return self.ticker

    def stockexists(self):
        return self.exists

    def setprice(self, newprice):
        self.priceCurr = newprice

    def setticker(self, newticker):
        self.ticker = newticker

    def setexists(self, change):
        self.exists = change
