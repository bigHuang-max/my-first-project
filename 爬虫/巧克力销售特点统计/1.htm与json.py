from urllib import response
#当我们使用 requests 模块请求 HTML 内容时，只能获得 HTML 代码，不会进一步请求 JavaScript 文件。
# 浏览器会先请求html文件，在请求js文件
#JS 文件是需要请求加载的，我们不点击查看这栏息就不会加载评价。

#1. 先点击 Network ；

#2. 然后选择 JS ；

#3. 点击商品评价加载相应的 JS 文件；

#4. 就能查看目前加载的 JS 文件
##查看 .js 文件中的内容：

##如图所示，逐个点开 JS 文件，选择右侧的 Preview 预览页面，查看预览代码（如果有三角折叠的信息，也要展开查看）。

##那么怎么确定哪个文件中存储的是评价标签信息呢？
###如何查找网站的 JS 文件呢？
###网站不同，数据位置和链接也不同，命名方式也不同，因此，网站存储数据没有统一的规律。
###我们先逐个查看 JS 文件中存储的内容，如图所示：

###名为 productPageComments 的文件，就是我们要找的存储商品评价的 JS 文件。
####找到文件后，点击文件，右键选择 Copy ，再选择 Copy link address 。
import requests
#ctrl +F 搜索标签 ex ： .tag-1
from bs4 import BeautifulSoup 
url="https://item.jd.com/1178886.html"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
response=requests.get(url,headers=headers)
#print(response)  = 200   使用.text属性将服务器相应内容转换为字符串形式，赋值给html
html=response.text
print(html)

soup=BeautifulSoup(html,"lxml")
content_all=soup.find_all(class_="tag-1")
print(content_all)