import requests

from bs4 import BeautifulSoup
url="http://nocturne.bczcdn.com/zip/1625207762993_63705/web.html"

response=requests.get(url)
response.encoding=response.apparent_encoding
html=response.text
soup=BeautifulSoup(html,"lxml")
content_all=soup.find_all(class_="rank")
for content in content_all:
    tit_list=content.find(name="a")
    for title in tit_list:
        print(title.string)
            
        

