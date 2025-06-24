#使用set()函数能够对列表中的元素去重，去重后需要赋值给新的变量。

# 定义列表wordList
wordList = ["夜曲", "编程", "课程", "好", "好", "课程"]

# 使用set()函数对列表进行去重，并赋值给wordSet
wordSet = set(wordList)

# 使用print()输出wordList
#print(wordList)

# 使用print()输出wordSet
#print(wordSet)

#输出结果
#['夜曲', '编程', '课程', '好', '好', '课程']
#{'编程', '夜曲', '课程', '好'}
    
    
import requests

# TODO 从bs4中导入BeautifulSoup模块
from bs4 import BeautifulSoup

# TODO 使用import导入jieba模块
import jieba



# TODO 将豆瓣评论URL地址，赋值给变量url


url="https://nocturne-spider.baicizhan.com/practise/12.html"
# TODO 将User-Agent以字典键对形式赋值给headers
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

# TODO 将 url 和 headers参数，添加进requests.get()中，将字典headers传递headers参数，给赋值给response
response=requests.get(url,headers=headers)

# TODO 将服务器响应内容转换为字符串形式，赋值给html
html=response.text

# TODO 使用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
soup=BeautifulSoup(html,"lxml")

# TODO 使用find_all()查询soup中class="short"的节点，赋值给content_all
content_all=soup.find_all(class_="short")

# TODO 创建一个空白列表wordList

wordList=[]
# TODO for循环遍历content_all
for content in content_all:

    # TODO 获取每个节点中标签内容，赋值给contentString
    contentString=content.string
   
    # TODO 使用jieba.lcut()将contentString进行分词，赋值给words
    words=jieba.lcut(contentString)
    

    # TODO 将列表wordList和列表words进行累加
    wordList+=words  
wordSet=set(wordList)      
print(wordSet)
print(len(wordSet))
    
