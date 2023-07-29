from request import GetRequest
from scrape import Scrape


requestToTopPage = GetRequest("https://finance.yahoo.co.jp")
textInTopPage = requestToTopPage.sendGetRequest()
scrapeInTopPage = Scrape(textInTopPage)

def scrapingInFirstStockPage():
  [firstStockUrl] = scrapeInTopPage.getUrl("#stockrank > div > div > section:nth-child(1) > ol > li:nth-child(1) > a")
  requestToFirstPage = GetRequest(firstStockUrl)
  textInFirstPage = requestToFirstPage.sendGetRequest()
  scrapeInFirstPage = Scrape(textInFirstPage)
  [firstStockNumber]= scrapeInFirstPage.getStockInfo("#industry > span")
  [firstStockName] = scrapeInFirstPage.getStockInfo("#root > main > div > div > div.XuqDlHPN > div:nth-child(3) > section._1zZriTjI._2l2sDX5w > div._1nb3c4wQ > header > div.DL5lxuTC > h1")
  return [
    firstStockNumber,
    firstStockName
  ]

def scrapingInSecondStockPage():
  [secondStockUrl] = scrapeInTopPage.getUrl("#stockrank > div > div > section:nth-child(1) > ol > li:nth-child(2) > a")
  requestToSecondPage = GetRequest(secondStockUrl)
  textInSecondPage = requestToSecondPage.sendGetRequest()
  scrapeInSecondPage = Scrape(textInSecondPage)
  [secondStockNumber]= scrapeInSecondPage.getStockInfo("#industry > span")
  [secondStockName] = scrapeInSecondPage.getStockInfo("#root > main > div > div > div.XuqDlHPN > div:nth-child(3) > section._1zZriTjI._2l2sDX5w > div._1nb3c4wQ > header > div.DL5lxuTC > h1")
  return [
    secondStockNumber,
    secondStockName
  ]

def scrapingInThirdStockPage():
  [thirdStockUrl] = scrapeInTopPage.getUrl("#stockrank > div > div > section:nth-child(1) > ol > li:nth-child(3) > a")
  requestToThirdPage = GetRequest(thirdStockUrl)
  textInThirdPage = requestToThirdPage.sendGetRequest()
  scrapeInThirdPage = Scrape(textInThirdPage)
  [thirdStockNumber]= scrapeInThirdPage.getStockInfo("#industry > span")
  [thirdStockName] = scrapeInThirdPage.getStockInfo("#root > main > div > div > div.XuqDlHPN > div:nth-child(3) > section._1zZriTjI._2l2sDX5w > div._1nb3c4wQ > header > div.DL5lxuTC > h1")
  return [
     thirdStockNumber,
     thirdStockName
  ]

def scrapingInFourthStockPage():
  [fourthStockUrl] = scrapeInTopPage.getUrl("#stockrank > div > div > section:nth-child(1) > ol > li:nth-child(4) > a")
  requestToFourthPage = GetRequest(fourthStockUrl)
  textInFourthPage = requestToFourthPage.sendGetRequest()
  scrapeInFourthPage = Scrape(textInFourthPage)
  [fourthStockNumber]= scrapeInFourthPage.getStockInfo("#industry > span")
  [fourthStockName] = scrapeInFourthPage.getStockInfo("#root > main > div > div > div.XuqDlHPN > div:nth-child(3) > section._1zZriTjI._2l2sDX5w > div._1nb3c4wQ > header > div.DL5lxuTC > h1")
  return [
    fourthStockNumber,
    fourthStockName
  ]

def scrapingInFifthStockPage():
  [fifthStockUrl] = scrapeInTopPage.getUrl("#stockrank > div > div > section:nth-child(1) > ol > li:nth-child(5) > a")
  requestToFifthPage = GetRequest(fifthStockUrl)
  textInFifthPage = requestToFifthPage.sendGetRequest()
  scrapeInFifthPage = Scrape(textInFifthPage)
  [fifthStockNumber]= scrapeInFifthPage.getStockInfo("#industry > span")
  [fifthStockName] = scrapeInFifthPage.getStockInfo("#root > main > div > div > div.XuqDlHPN > div:nth-child(3) > section._1zZriTjI._2l2sDX5w > div._1nb3c4wQ > header > div.DL5lxuTC > h1")
  return [
    fifthStockNumber,
    fifthStockName
  ]

print(scrapingInFirstStockPage())
print(scrapingInSecondStockPage())
print(scrapingInThirdStockPage())
print(scrapingInFourthStockPage())
print(scrapingInFifthStockPage())
