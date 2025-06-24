# 定义函数 & 反爬虫编码 通过新建的函数 getPositionInfo，获取职位名称、公司名称、所在城市、工作持续月数。
# 导入requests模块
#我们不能从搜索页面中提取数据，需要在职位对应的页面中爬取数据，可是职位对应的 URL 链接在哪呢？
#找到了数据在页面中的位置后，现在我们可以先在搜索页中提取职位名称所在的节点，再从节点中提取职位对应的URL链接。
import requests

# 从bs4中导入BeautifulSoup模块
from bs4 import BeautifulSoup

# 导入time模块
import time

# 将User-Agent以字典键对形式赋值给headers
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}

#########  Don't  repeat yourself
#这个函数的功能是请求指定的 URL 并获取网页内容，使用 BeautifulSoup 解析网页，最后提取出需要的数据。
# 定义一个新函数getPositionInfo，包含参数detail_url
def getPositionInfo(detail_url):
    # 将detail_url和headers参数，添加进requests.get()中，给赋值给res
    res = requests.get(detail_url, headers=headers)

    # 使用.text属性获取网页内容，赋值给html
    html = res.text

    # 用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
    soup = BeautifulSoup(html, "lxml")

    # 使用find()函数获取class="new_job_name"的节点
    # 使用find()函数获取name="span"的节点
    # 使用.string属性提取出标签内容,赋值给job
    job=soup.find(class_="new_job_name").find(name="span").string

    # TODO 使用find()函数获取class="com-name"的节点
    # 使用.string属性提取出标签内容
    # 使用strip()移除空格，赋值给companyName
    companyName=soup.find(class_="com-name").string.strip()

    # TODO 使用find()函数获取class="job_position"的节点
    # 使用.string属性提取出标签内容，赋值给position
    position=soup.find(class_="job_position").string


    # TODO 使用find()函数获取class="job_time cutom_font"的节点
    # 使用.string属性提取出标签内容，赋值给month
    month=soup.find(class_="job_time cutom_font").string

    # TODO 使用encode()函数对变量month编码，赋值给month
    month=month.encode()

    # 多次使用replace()函数将二进制数据替换成UTF-8编码数字0-5
    month = month.replace(b"\xee\x8b\xbf", b"0").replace(b"\xee\xa2\x9c", b"1").replace(b"\xee\x90\xb7",b"2")
    month = month.replace(b"\xee\x81\xa5",b"3").replace(b"\xee\xad\xb1", b"4").replace(b"\xee\xb2\xae", b"5")

    # TODO 多次使用replace()函数将二进制数据替换成UTF-8编码数字6-9
    month=month.replace(b"\xef\x8a\x98",b"6").replace(b"\xef\x80\xa6",b"7").replace(b"\xee\xa1\xb1",b"8").replace(b"\xee\xbe\xad",b"9")
       


    # TODO 使用decode()函数对替换后的二进制数据进行解码，赋值给month
    month=month.decode()

    # TODO 格式化输出job,companyName,position,month，每个变量之间用","隔开
    print(f"{job},{companyName},{position},{month}")

# for循环遍历range()函数生成的1-5的数字
for i in range(1, 6):

    # 利用格式化字符生成串网站链接 赋值给变量url
    url = f"https://nocturne-spider.baicizhan.com/practise/39/PAGE/{i}.html"
    
    # 将url和headers参数，添加进requests.get()中，将字典headers传递给headers参数，给赋值给res
    res = requests.get(url, headers=headers)

    # 使用.text属性获取网页内容，赋值给html
    html = res.text

    # 用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
    soup = BeautifulSoup(str(html), "lxml")

    # 使用find_all()查询soup中class=title ellipsis font的节点，赋值给titles
    titles = soup.find_all(class_="title ellipsis font")
    #find_all() 函数可以查询 BeautifulSoup 对象中所有符合条件的元素，组成一个列表。
    

    # for循环遍历列表
    for item in titles:
        # 使用.attrs获取href对应的属性值，并赋值给detail_url
        detail_url = item.attrs["href"]

        # 调用getPositionInfo()函数，传入参数detail_url
        getPositionInfo(detail_url)

    # 使用time.sleep()停顿2秒
    time.sleep(2)