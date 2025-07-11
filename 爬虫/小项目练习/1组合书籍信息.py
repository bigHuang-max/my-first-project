import requests

# 从bs4中导入BeautifulSoup模块
from bs4 import BeautifulSoup

# 将URL地址，赋值给变量url
url = "https://nocturne-spider.baicizhan.com/practise/27.html"

# 将User-Agent以字典键对形式赋值给headers
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

# 将 url 和 headers参数，添加进requests.get()中，将字典headers传递headers参数，给赋值给response
response = requests.get(url, headers=headers)

# 将服务器响应内容转换为字符串形式，赋值给html
html = response.text

# 使用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
soup = BeautifulSoup(html, "lxml")

# 使用find_all()查询soup中class="item"的节点，赋值给content_all
content_all = soup.find_all(class_="item")

# TODO for循环遍历content_all
for content in content_all:

    # TODO 使用find查询content中class="pl2"的节点(p后面是字母l)，赋值给pl2
    p12 = content.find(class_="pl2")

    # TODO 使用.text获取pl2中a标签下的的text文本信息，赋值给title
    title = p12.find("a").text

    # TODO 使用replace()去掉title中的换行符"\n"
    title = title.replace("\n","")

    # TODO 使用replace()去掉title中的空格
    title = title.replace(" ","")

    # TODO 使用find查询content中class="rating_nums"的节点，赋值给rating_nums
    rating_nums = content.find(class_="rating_nums")

    # TODO 获取rating_nums节点中的内容，赋值给rate
    rate = rating_nums.string

    # TODO 使用find查询content中class="inq"的节点，赋值给inq
    inq = content.find(class_="inq")

    # TODO 获取inq节点中的内容，赋值给introduction
    introduction = inq.string

    # TODO 使用格式化输出结果，title,rate,introduction两两之间加空格
    print(f"{title} {rate} {introduction}")