import requests

class GetRequest:
    def __init__(self,url):
        self.url = url
    
    def sendGetRequest(self):
        response = requests.get(self.url)
        text = response.text
        return text
    
class PostRequest:
    def __init__(self, url, body):
        self.url = url
#        self.header = header | None
        self.body = body
    
    def sendPostRequest(self):
        response = requests.post(url=self.url, data=self.body)
        return response