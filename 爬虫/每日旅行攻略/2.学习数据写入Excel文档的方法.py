from csv import writer
from sre_constants import SUCCESS
import requests
import time
from bs4 import BeautifulSoup
import  pandas as pd 

headers={
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
}
writer=pd.ExcelWriter("/Users/生活黑客/OneDrive/桌面/VS code/美食排行.xlsx")
for city in ["10065","10099","10132"]:
    score_list=[]
    review_list=[]
    title_list=[]
    for page in range(1,11):
        time.sleep(1)
        url = f"http://www.mafengwo.cn/cy/{city}/0-0-0-0-0-{page}.html"
    
        response=requests.get(url,headers=headers)
        html=response.text
        soup=BeautifulSoup(html,"lxml")
        content_all=soup.find_all(class_="item clearfix")
        for content in content_all:
            content_grade=content.find(class_="grade")
            score=content_grade.em.string
            review=content_grade.p.em.string
            title=content.find(class_="title").h3.a.string
            score_list.append(score)
            review_list.append(review)
            title_list.append(title)
    total={"名称":title_list,"评分":score_list,"点评数量":review_list}
    info=pd.DataFrame(total)
    if city=="10065":
        info.to_excel(excel_writer=writer,sheet_name="北京美食")
    elif city=="10099" :
        info.to_excel(excel_writer=writer,sheet_name="上海美食")    
    else:    
        info.to_excel(excel_writer=writer,sheet_name="厦门美食")

writer.save()        
print("SUCCESS")



    
