
from cgitb import html
import requests 
from bs4 import BeautifulSoup
import time 
# 将User-Agent以字典键对形式赋值给headers
headers = {
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
}


for page in range(1,11):
    time.sleep(1)
    
    url=f"https://www.mafengwo.cn/cy/10065/0-0-0-0-0-{page}.html"

    # TODO 使用requests.get()请求内容，获取响应消息，赋值给response
    response=requests.get(url,headers=headers)
    html=response.text
    # TODO 使用print()输出响应消息的.status_code属性
    soup=BeautifulSoup(html,"lxml")
    content_all=soup.find_all(class_="item clearfix")
    for content in content_all :
        content_grade=content.find(class_="grade")
        score=content_grade.em.string
        review=content_grade.p.em.string
        title=content.find(class_="title").h3.a.string
        print(score,review,title)

     




