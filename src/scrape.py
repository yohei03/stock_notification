from bs4 import BeautifulSoup

class Scrape: 
    def __init__(self, text):
        self.soup = BeautifulSoup(text, 'html.parser')

    def getUrl(self, CSSSelectorOfStock):
        stockInfo = self.soup.select(CSSSelectorOfStock)
        stockUrl = stockInfo[0].attrs["href"]
        return [stockUrl]
    
    def getStockInfo(self, CSSSelectorOfStock):
        stockInfoArray = self.soup.select(CSSSelectorOfStock)
        stockInfo = stockInfoArray[0].contents
        return stockInfo

  
        
    

       