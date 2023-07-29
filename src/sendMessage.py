from getStockInfo import *
from request import PostRequest
from createText import createText

[firstStockNumber,firstStockName] = scrapingInFirstStockPage()
[secondStockNumber, secondStockName] = scrapingInSecondStockPage()
[thirdStockNumber, thirdStockName] = scrapingInThirdStockPage()
[fourthStockNumber, fourthStockName] = scrapingInFourthStockPage()
[fifthStockNumber, fifthStockName] = scrapingInFifthStockPage()

numbers = [
    firstStockNumber,
    secondStockNumber,
    thirdStockNumber,
    fourthStockNumber,
    fifthStockNumber
]

names = [
    firstStockName,
    secondStockName,
    thirdStockName,
    fourthStockName,
    fifthStockName
]

def sendMessage():
  text = createText(numbers, names)
  url = "https://slack.com/api/chat.postMessage"
  body = {
      "token": "xoxp-5654228858578-5666863709009-5651353020837-08544b2df99882d80d73cc9d5ad25dc0",
      "channel": "#stock_info",
      "text" : text,
  }
  postRequest = PostRequest(url= url,body=body)
  postRequest.sendPostRequest()
  return 
