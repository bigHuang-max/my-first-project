#1. 解析网页，使用.attr方法获得每个电影的url

#2. 进入电影网页，提取电影名称、电影评分、电影简介等3项信息

#注意：使用.attr方法获得的url不完整，需要自己添加前缀“https://ssr1.scrape.center/”

#3. 将这些信息写入"/Users/电影推荐.xlsx"文件中，工作表命名为："电影推荐"，写入Excel的数据顺序为："电影名称", "电影评分", "电影简介"



# 使用import导入requests模块
import requests

# 从bs4中导入BeautifulSoup模块
from bs4 import BeautifulSoup

# 使用import导入pandas模块，并使用as简写为pd
import pandas as pd

# 将网址赋值给变量url
url = 'https://ssr1.scrape.center/'

# 将User-Agent以字典键对形式赋值给headers
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}


# 新建3个列表，用于存储景点名字nameList、评分scoreList和简介detailList
nameList = []
scoreList = []
detailList = []

# 使用ExcelWriter()函数打开 /Users/电影推荐.xlsx 文档，赋值给writer
writer = pd.ExcelWriter("/Users/生活黑客/OneDrive/桌面/VS code/电影推荐.xlsx")


# 定义一个新函数getInfo，包含参数info_url
def getInfo(info_url):

    # 将info_url和headers参数，添加进requests.get()中，给赋值给res
    res = requests.get(info_url, headers=headers)

    # 使用.text属性获取网页内容，赋值给html
    html = res.text
    # 用BeatifulSoup()传入变量html和解析器lxml，赋值给soup
    soup = BeautifulSoup(html, "lxml")

    #  TODO 使用find()方法找到电影名字(class="m-b-sm"节点)，并赋值给name
    name = soup.find(class_="m-b-sm").text

    #  TODO 将name添加进nameList中
    nameList.append(name)

    #  TODO 使用find()方法找到评分所在区域(class="score"节点)，score
    score= soup.find(class_="score").text

    #  TODO 将score添加进scoreList中
    scoreList.append(score)

    #  TODO 使用find()方法找到电影简介所在区域(class="drama"节点)，并赋值给detail
    detail = soup.find(class_="drama").p.text
    # TODO  将detail添加进detailList中
    detailList.append(detail)


# 将 url 和 headers参数，添加进requests.get()中，将字典headers传递headers参数，给赋值给response
response = requests.get(url, headers=headers)

# 将服务器响应内容转换为字符串形式，赋值给html
html = response.text

# 使用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
soup = BeautifulSoup(html, "lxml")

# 使用find_all()查询soup中class="name"的节点，赋值给content_all
content_all = soup.find_all(name="a", class_="name")

# for循环遍历content_all
for content in content_all:

    # 获取a标签下的href对应的属性值，并赋值给detail_url
    detail_url  = content.attrs["href"]

    # 给detail_url加上前缀，并赋值给info_url
    info_url = "https://ssr1.scrape.center" + detail_url

    # 调用getInfo()函数，传入参数info_url
    getInfo(info_url)


# 先将获取的列表信息转换成字典类型，赋值给total
total = {"电影名称": nameList, "电影评分": scoreList, "电影简介": detailList}


# 将total传入DataFrame()函数，赋值给info
info = pd.DataFrame(total)

# 使用to_excel将信息写入writer文档中，并设置工作表名称为sheet_name="电影推荐"
info.to_excel(excel_writer=writer, sheet_name="电影推荐")

# 使用save()函数保存文档
writer.save()