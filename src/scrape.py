from bs4 import BeautifulSoup

class Scrape: 
    def __init__(self, text):
        self.soup = BeautifulSoup(text, 'html.parser')

    def getUrl(self, CSSSelectorOfStock):
##        stockCodes = [n.get_text() for n in self.soup.select(CSSSelectorOfStockCode)]
        stockInfo = self.soup.select(CSSSelectorOfStock)
        stockUrl = stockInfo[0].attrs["href"]
        return [stockUrl]
    
    def getStockInfo(self, CSSSelectorOfStock):
        stockInfoArray = self.soup.select(CSSSelectorOfStock)
        stockInfo = stockInfoArray[0].contents
        return stockInfo

  
        
    

       