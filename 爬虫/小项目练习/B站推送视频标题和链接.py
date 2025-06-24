import requests
from bs4 import BeautifulSoup
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}
url="https://nocturne-spider.baicizhan.com/practise/26.html"
response=requests.get(url,headers=headers)    
html=response.text
soup=BeautifulSoup(html,"lxml")
content_all=soup.find_all(class_="info")
for content in content_all:
    title=content.find("p").string
    new_url=content.find("a").attrs["href"]
    print(f"{title}:{new_url}")    