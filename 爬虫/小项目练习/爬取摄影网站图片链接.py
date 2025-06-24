import requests
# TODO 使用from...import从bs4模块中导入BeautifulSoup
from bs4 import BeautifulSoup

# TODO 将URL"https://nocturne-spider.baicizhan.com/practise/19.html"赋值给变量url


url="https://nocturne-spider.baicizhan.com/practise/19.html"
# 将User-Agent以字典键对形式赋值给headers
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

# TODO 使用get()函数请求链接，并且带上headers
response=requests.get(url,headers=headers)

# TODO 使用.text属性将服务器相应内容转换为字符串形式，赋值给html
html=response.text

# TODO 使用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
soup=BeautifulSoup(html,"lxml")

# TODO 使用find_all()查询soup中class="item"的节点，赋值给content_all
content_all=soup.find_all(class_="item")      

# TODO for循环遍历content_all
for content in content_all:

    # TODO 使用find()查询content中的img标签，并赋值给imgContent
    imgContent=content.find("img")

    # TODO 使用.attrs获取data-src对应的属性值，并赋值给imgSrc
    imgSrc=imgContent.attrs["data-src"]

    # TODO 将url和imgSrc以字符串形式相连接，赋值给imgUrl
    imgUrl=url+imgSrc

    # TODO 输出imgUrl
    print(imgUrl)