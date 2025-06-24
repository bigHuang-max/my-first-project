# 导入 WordCloud() 类后，需要调用类中的方法，接下来，使用 WordCloud() 函数创建一个对象。
import requests
from bs4 import BeautifulSoup 
import jieba
from pyecharts.charts import  WordCloud
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')
url="https://movie.douban.com/subject/2129039/comments?sort=new_score&status=P"
headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
response=requests.get(url,headers=headers)
html=response.text
soup=BeautifulSoup(response.text,'html.parser') # 解决报警
content_all=soup.find_all(class_="short")
wordList=[]
for content in content_all:
    contentString=content.string              
    words=jieba.lcut(contentString)
    wordList+=words
print(wordList)
