import requests

# 从bs4中导入BeautifulSoup模块
from bs4 import BeautifulSoup

# TODO 将获取的弹幕接口链接赋值给变量url
url="https://nocturne-spider.baicizhan.com/practise/33.xml"

# TODO 将变量url作为参数，添加进requests.get()中，给赋值给response
response=requests.get(url)

# TODO 将服务器响应内容转换为字符串形式，赋值给xml
xml=response.text

# TODO 使用BeautifulSoup()读取xml，添加lxml解析器，赋值给soup
soup=BeautifulSoup(xml,"lxml")

# TODO 使用find_all()查询soup中d的节点，赋值给content_all
content_all=soup.find_all("d")

# TODO 新建一个列表sendList
sendList=[]

# TODO for循环遍历content_all
for content in content_all:

    # TODO 使用.attrs获取p对应的属性值，并赋值给data
    data=content.attrs["p"]
    
    # TODO 使用split()函数分割data，获取第七项元素发送者ID，并赋值给变量senderID
    senderID=data.split(",")[6]

    # TODO 如果senderID不在sendList里
    if senderID not in sendList:

        # TODO 将senderID添加进列表sendList中
        sendList.append(senderID)

# TODO 使用len()函数来统计sendList数组的长度
sender=len(sendList)

# TODO 使用格式化输出，输出一共有多少个发送者
print(f"一共有{sender}个发送者")