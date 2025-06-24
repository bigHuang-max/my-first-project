#1. 首先使用class="product-wrap clear-fix"找到所有景点信息；

#2. 使用class="tag"找到含有A级景点节点，获取景点标签，如：5A景区、4A景区、AAA景区；

#3. 使用class="main-title"属性找到景点名称；

#4. 使用text属性获取各节点的文字内容；

#5. 使用strip()函数消除字符串中的空格；

#6. 格式化输出景点名称和A级标签。
#注意：有一些景区没有标签要剔除掉哦～
# 导入requests模块
import requests

# 从bs4中导入BeautifulSoup模块
from bs4 import BeautifulSoup

# 将User-Agent以字典键对形式赋值给headers
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}

# 利用格式化字符生成串网站链接 赋值给变量url
url = f"https://nocturne-spider.baicizhan.com/practise/59.htm"

# 将url和headers参数，添加进requests.get()中，将字典headers传递给headers参数，给赋值给res
res = requests.get(url, headers=headers)

# 使用.text属性获取网页内容，赋值给html
html = res.text

# 用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
soup = BeautifulSoup(html, "lxml")

# find_all()获取class="product-wrap clear-fix"的全部节点
items = soup.find_all(class_="product-wrap clear-fix")

# for循环遍历tags中的元素item
for item in items:
    # TODO 使用find获取class=tag的子节点，赋值给tag
    tag=item.find(class_="tag")

    # TODO 如果tag不是空值None
    if tag!=None:
        # TODO 将tag元素中的文本内容，消除空格，赋值给tag_new
        tag_new=tag.text.strip()

        #  TODO 使用find_next获取main-title的子节点，赋值给title
        title=item.find(class_="main-title")

        #  TODO 将title元素中的文本内容，消除空格，赋值给title_text
        title_text=title.text.strip()

        #  TODO 格式化输出tag_new title_text，用空格隔开
        print(f"{tag_new} {title_text}")
 

