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
