import requests

class Request:
    def __init__(self,url):
        self.url = url
    
    def send(self):
        response = requests.get(self.url)
        text = response.text
        return text