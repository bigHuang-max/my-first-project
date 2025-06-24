#1. 提取的商品名称中有空行，需要去掉；

#2. 商品的价格不能直接进行比较，需要转换数据类型。

#3. 写入的商品价格需要在50-150元（包括50，150）。
#有小数，所以浮点型
#4. 商品名称和价格之间空一格，每个商品之间换一行；



#5. 写入文档中需要添加换行"\n
# 使用import导入requests模块
import requests

# 从bs4中导入BeautifulSoup模块
from bs4 import BeautifulSoup

# 将网址赋值给变量url
url = "https://nocturne-spider.baicizhan.com/practise/50.html"

# 将User-Agent以字典键对形式赋值给headers
headers = { "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

# 将 url 和 headers参数，添加进requests.get()中，将字典headers传递headers参数，给赋值给response
response = requests.get(url, headers=headers)

# 将服务器响应内容转换为字符串形式，赋值给html
html = response.text

# 使用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
soup = BeautifulSoup(html, 'lxml')

# TODO 获取商品名称
# 获取商品价格
# 判断价格区间
# 写入txt文档
content_all=soup.find_all(class_="item_wrap_right")
for content in content_all:
    product=content.find(class_="s_l_name").text.strip()
    price=content.find(class_="search_list_price").find("span").text
    if float(price)>=50 and float(price)<=150:
        with open("洗面奶.txt","a") as f:
            f.write(f"{product} {price}"+"\n")
            
        
    