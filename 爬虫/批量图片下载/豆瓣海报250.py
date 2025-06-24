import requests




session = requests.session()
# 使用from..import从bs4模块导入BeautifulSoup
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings()
requests.adapters.DEFAULT_RETRIES = 5
from lxml import etree #数据预处理
from urllib import request #下载方法

# 将User-Agent以字典键对形式赋值给headers
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
    
# 使用for循环遍历range()函数生成的0-1的数字
for i in range(0, 11):

    # 取遍历中的每个数和25相乘计算每页的数值，并赋值给page
    page = i * 25

    # 用"https://movie.douban.com/top250?start="和page转换成的字符串格式相连，接着连上"&filter="，并赋值给url
    url = "https://movie.douban.com/top250?start=" + str(page) + "&filter="

    # 将字典headers传递给headers参数，添加进requests.get()中，赋值给response
    
    
    response = requests.get(url, headers=headers,verify=False, timeout=5) 

    # 将服务器响应内容转换为字符串形式，赋值给html
    html = response.text

    # 使用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
    soup = BeautifulSoup(html, "lxml")

    # 使用find_all()查询soup中class="pic"的节点，赋值给content_all
    content_all = soup.find_all(class_="pic")

    # for循环遍历content_all
    for content in content_all:

        # 使用find()查询content中的img标签，并赋值给imgContent
        imgContent = content.find(name="img")

        # 使用.attrs获取alt对应的属性值，并赋值给imgName
        imgName = imgContent.attrs["alt"]
        print(imgName)

        # 使用.attrs获取src对应的属性值，并赋值给imgUrl
        imgUrl = imgContent.attrs["src"]

        # 使用replace()函数将链接中的s_ratio_poster替换成m，并赋值给imgUrlHd
        imgUrlHd = imgUrl.replace("s_ratio_poster", "m")

        # 将链接添加进requests.get()中，赋值给imgResponse
        imgResponse = requests.get(imgUrlHd)
        print(imgUrlHd)

        # 使用.content属性将响应消息转换成图片数据，赋值给img
        img = imgResponse.content

        # 使用with语句配合open()函数以图片写入的方式打开文件
        # 用格式化将图片名字和.jpg格式组合
        # 打开的文件赋值为f
        with open(f"/Users/生活黑客/OneDrive/桌面/VS code/web crawl 图片/{imgName}.jpg", "wb") as f:
            # 使用write()将图片写入
            f.write(img)
print("爬取成功")     
print("小黑子666*10086")       