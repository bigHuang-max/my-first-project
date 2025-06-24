# 使用import导入requests模块
from bs4 import BeautifulSoup
import requests
from pyecharts.charts import  Line
# https://comment.bilibili.com/{cid}.xml cid码可以找到
#API应用程序接口  所以不用Agent-headers  XML 可拓展标记语言  cid 表示弹幕池  
# 将https://comment.bilibili.com/218710655.xml赋值给变量url
#API 一般以 URL 形式存在的，B站的弹幕 API 的 URL 链接为：
#https://comment.bilibili.com/{cid}.xml
############在视频链接中获取 cid，拼接弹幕接口链接，从中提取出 XML 代码。

url = "https://comment.bilibili.com/218710655.xml"

# 由于 API 是网站提供的，可以不用设置 header。
# 将变量url作为参数，添加进requests.get()中，给赋值给response  
#使用 .text 属性获取 response 内容，赋值给变量 xml。在使用 print 输出变量 xml，即可获得视频弹幕接口 XML 代码。
response = requests.get(url)
response.encoding=response.apparent_encoding
xml = response.text
soup=BeautifulSoup(xml,"lxml")
#提取全部节点
content_all=soup.find_all(name="d")
timeList=[]
# 使用.text属性获取response内容，赋值给xml
for comment in content_all:

    # TODO 使用.attrs获取p对应的属性值，并赋值给data
    data=comment.attrs["p"]
    time =data.split(",")[0]
    timeList.append(float(time))
subtitlesDict={}
for x in range(25)    :
    start =x*30 
    end=30*(x+1)
    segment_range=f"{start}-{end}"
    subtitlesDict[segment_range]=0
print(timeList)    
for subtitle in subtitlesDict:
    start_key=subtitle.split("-")[0]
    end_key=subtitle.split("-")[1]
    for item in timeList:
        if   int(start_key) <= item <= int(end_key):
            #此处整型才能比较 
            subtitlesDict[subtitle]+=1
line=Line()
line.add_xaxis(list(subtitlesDict.keys()) )           
line.add_yaxis("弹幕数",list(subtitlesDict.values()))
line.render("line.html")
print("success")

    



