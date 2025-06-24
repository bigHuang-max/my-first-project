#1. 需要输出的名称拆分成两部分嵌套在节点中，需要用到.text知识点。

#2. 需要输出的房价需要 价格¥532，也要用到.text知识点。
#要求：每项用英文逗号隔开
# 使用import导入requests模块
######   名字，房型，价格，房源链接
import requests

# 从bs4中导入BeautifulSoup模块
from bs4 import BeautifulSoup

# 将网址赋值给变量url
url = "https://nocturne-spider.baicizhan.com/practise/53.html"

# 将User-Agent以字典键对形式赋值给headers
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

# 将 url 和 headers参数，添加进requests.get()中，将字典headers传递headers参数，给赋值给response
response = requests.get(url, headers=headers)

# 将服务器响应内容转换为字符串形式，赋值给html
html = response.text

# 使用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
soup = BeautifulSoup(html, "lxml")

# TODO 使用find_all()查询soup中class="_y89bwt"的节点，赋值给content_all
content_all = soup.find_all(class_="_y89bwt")

# TODO for循环遍历content_all
for content in content_all:
    
    # TODO 使用find()函数获取节点class="_qrfr9x5"，用.text提取房源名称，并赋值给name
    name = content.find(class_="_qrfr9x5").text

    # TODO 使用find()函数获取节点class="_1etkxf1"，用.text提取房型信息，并赋值给layout
    layout = content.find(class_="_1etkxf1").text
    
    # TODO 使用find()函数获取节点class="_1d8yint7"，用.text提取房子价格，并赋值给price
    price = content.find(class_="_1d8yint7").text

    # TODO 使用find()函数获取节点class="_1szwzht"，使用.a获取房源链接，使用.attrs获取href对应的属性值，并赋值给detail_url
    detail_url = content.find(class_="_1szwzht").a.attrs["href"]
    
    # TODO 给detail_url加上前缀"https://www.airbnb.cn"，并赋值给info_url
    info_url = "https://www.airbnb.cn" +detail_url

    # TODO 格式化输出name, layout, price, info_url,每个信息之间加英文逗号","
    print(f"{name},{layout},{price},{info_url}")