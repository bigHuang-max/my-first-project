#通过对解题思路的分析，我们就得到了帮助小倩解决问题的步骤：
# ctrl +/ ==多行注释
# 1.完成一张图片的下载保存；

# 2.分析网页结构，找到图片所在位置；

# 3.请求图片链接，下载图片；

# 4.使用循环，批量下载该页所有的图片；

# 5.通过链接找到图片的高清图下载；

# 6.通过翻页实现图片的批量下载。
# 使用import导入requests模块
import requests
session = requests.session()

# 使用from..import从bs4模块导入BeautifulSoup
from bs4 import BeautifulSoup

# 将电影URL地址，赋值给变量url
url = "https://movie.douban.com/top250?"

# 将User-Agent以字典键对形式赋值给headers
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

# 将字典headers传递给headers参数，添加进requests.get()中，赋值给response
import urllib3
urllib3.disable_warnings()
requests.adapters.DEFAULT_RETRIES = 5

response = requests.get(url, headers=headers,verify=False, timeout=5)

# TODO 将服务器响应内容转换为字符串形式，赋值给html
html=response.text

# TODO 使用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
soup=BeautifulSoup(html,"lxml")

# TODO 使用find_all()查询soup中class="pic"的节点，赋值给content_all
content_all=soup.find_all(class_="pic") #python 环境要加下划线

# TODO for循环遍历content_all
for content in content_all:

    # TODO 使用find()查询content中的img标签，并赋值给imgContent
    imgContent=content.find(name="img")

    # TODO 使用.attrs获取alt对应的属性值，并赋值给imgName
    imgName=imgContent.attrs["alt"]

    # TODO 使用.attrs获取src对应的属性值，并赋值给imgUrl
    imgUrl=imgContent.attrs["src"]
    print(imgName)
    # 使用replace()函数将链接中的s_ratio_poster替换成m，并赋值给imgUrlHd
    imgUrlHd = imgUrl.replace("s_ratio_poster", "m")

    # 使用print输出imgUrlHd
    print(imgUrlHd)

    # TODO 将链接添加进requests.get()中，赋值给imgResponse
    imgResponse=requests.get(imgUrlHd)

    # TODO 使用.content属性将响应消息转换成图片数据，赋值给img
    img=imgResponse.content
    with open(f"/Users/生活黑客/OneDrive/桌面/VS code/{imgName}.jpg","wb") as f :
        f.write(img)

    # TODO 使用with语句配合open()函数以图片写入的方式打开文件
    # 用格式化将图片名字和.jpg格式组合
    # 打开的文件赋值为f
    #with  open(f"C:/Users/生活黑客/OneDrive/桌面/VS code/web crawl 图片/{imgName}.jpg","wb") as f :

        # Windows + r 防止转义ex: downloadPath = r"D:\yequ\Downloads"
        # 唯一问题，r 的位置
        # TODO 使用write()将图片写入
        # wb 二进制写入，不存在自动创建

        
        
        
print("success")        
#案例分析 <img width="100" alt="肖申克的救赎" src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p480747492.webp" class="">
# <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p480747492.webp" title="点击看更多海报" alt="The Shawshank Redemption" rel="v:image">
# <img style="display: block;-webkit-user-select: none;margin: auto;cursor: zoom-in;background-color: hsl(0, 0%, 90%);transition: background-color 300ms;" src="https://img2.doubanio.com/view/photo/m/public/p480747492.webp" width="480" height="711">
# 观察网址 s_ratio_poster  & m
