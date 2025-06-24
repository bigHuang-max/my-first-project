#1. 获取User-Agent，设置请求头；

#2. 使用for循环和整数型转成字符串数据类型的知识，获取4页的URL；

#例如：url = "https://nocturne-spider.baicizhan.com/practise/23/PAGE/"+str(page)+".html"

#3. 将url和headers参数，添加进requests.get()中，获取网页HTML代码；

#4. 创建一个BeautifulSoup对象，使用find_all()函数获取节点；
####################包含多节点时用find_all()函数

#5. 调用.string属性，获取每个节点中标签内的内容。
# 使用import导入requests模块
import requests

# 从bs4中导入BeautifulSoup模块
from bs4 import BeautifulSoup

# 将User-Agent以字典键对形式赋值给headers
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

# TODO 使用for循环遍历range()函数生成的1-4的数字
for page in range(1,5):

    # TODO 用""https://nocturne-spider.baicizhan.com/practise/23/PAGE/"和page转换成的字符串格式相连，接着在连上".html"，并赋值给url
    url = "https://nocturne-spider.baicizhan.com/practise/23/PAGE/"+str(page)+".html"

    # TODO 将字典headers传递给headers参数
    # 将 url 和 headers参数，添加进requests.get()中，赋值给response
    response = requests.get(url,headers=headers)

    # TODO 将服务器响应内容转换为字符串形式，赋值给html
    html = response.text

    # TODO 用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
    soup = BeautifulSoup(html,"lxml")

    # TODO 使用find_all()查询soup中class=title的节点，赋值给content_all
    content_all = soup.find_all(class_="title")

    # TODO for循环遍历content_all
    for content in content_all:

        # TODO 获取每个节点中标签内的内容，赋值给contentString
        contentString = content.string
    
        # TODO 使用print输出contentString
        print(contentString)
