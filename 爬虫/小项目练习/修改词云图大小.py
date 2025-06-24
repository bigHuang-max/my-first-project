import requests
from bs4 import BeautifulSoup
import jieba
#jieba 又名结巴
from pyecharts.charts import WordCloud
url="https://nocturne-spider.baicizhan.com/2020/09/02/coco/"
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
response=requests.get(url,headers=headers)
html=response.text
soup=BeautifulSoup(html,"lxml")
content_all=soup.find_all(name="em")
wordList=[]
for i in content_all:
    content=i.string
    words=jieba.lcut(content)
    wordList=wordList+words
wordDict={}
for words in wordList:
    if words==".." or words=="......":
        continue
    if len(words)>1:
        if words not in wordDict:
            wordDict[words]=1
        else:
            wordDict[words]=wordDict[words]+1
wordCloud=WordCloud()
wordCloud.add(series_name="",data_pair=wordDict.items(),width=800,height=500,word_size_range=[30,70])
wordCloud.render("dream.html")
print("success")
        
    

