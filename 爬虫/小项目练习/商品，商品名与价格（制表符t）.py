#制表符
print("学号\t姓名\t语文\t数学\t英语")
print("2017001\t曹操\t99\t88\t0")
print("2017002\t周瑜\t92\t45\t93")
print("2017008\t黄盖\t77\t82\t100")
# 使用import导入requests模块
import requests

# 使用from...import从bs4模块中导入BeautifulSoup
from bs4 import BeautifulSoup

# 复制网页链接赋值给变量url
url = "https://nocturne-spider.baicizhan.com/practise/54.html"

# 将User-Agent以字典键值对形式赋值给headers
# 将cookie以字典键值对形式赋值给headers
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
"cookie": "shshshfpa=59756f24-6de8-90a9-92f3-022a321cbcaa-1589969605; __jdu=1589969605288365795565; shshshfpb=fZNp5OzH0j2T%20X%20WnJhzrBg%3D%3D; qrsc=3; user-key=b05356ef-c40b-44d2-a837-60df17e9b74e; cn=0; _pst=jd_51aaae03cedfa; unick=jd_51aaae03cedfa; pin=jd_51aaae03cedfa; _tp=FNP1fTo2ON7jgdbikn0lWAbSqMI20pF0xO0Iq%2FccQVc%3D; pinId=qN40m03yULDpSLzjaHwm07V9-x-f3wj7; __jdc=122270672; rkv=1.0; 3AB9D23F7A4B3C9B=DVCEDHG6BLYWMZMJIWNBOSTWP7GOWK77C5VJKGVQO7F3JHUFZVL5V5B5UKDYLF2LK5VAEIOSN2YRG33EJLXR6ZJ2TU; __jdv=122270672|direct|-|none|-|1602475191357; areaId=22; ipLoc-djd=22-1930-50947-0; __jda=122270672.1589969605288365795565.1589969605.1602487075.1602569356.29; shshshfp=b393a5ab6c1163583435b3a90574cb22; shshshsID=ef428a912dae95ba61fd7ac2ee0af172_9_1602570753319; __jdb=122270672.9.1589969605288365795565|29.1602569356"}

# 使用get()函数请求链接，并且带上headers
response = requests.get(url, headers=headers)

# 使用.text属性将服务器相应内容转换为字符串形式，赋值给html
html = response.text

# 使用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
soup = BeautifulSoup(html, "lxml")

# 使用find_all()查询soup中class="gl-item"的节点，赋值给content_all
content_all = soup.find_all(class_="gl-item")

# 使用for循环遍历content_all
for content in content_all:

    # TODO 提取商品的价格，价格的格式为￥x.xx
    # 找到价格所在节点strong，使用.text属性可直接获取该节点中所有的内容
    # 使用strip()可去掉获取内容中头尾的空格，将价格赋值给变量price
    p_price = content.find(class_="p-price")
    price = p_price.strong.text.strip()
    price = price


    # TODO 提取商品的名称，名称包括<em></em>标签中的所有文字
    # 需要用到.text属性提取所有的内容，例如 京东超市 的文字也需要提取
    # 提取到的内容有\n和\t，需要用replace("\n","")  replace("\t", "")，将价格赋值给name
    p_name = content.find(class_="p-name p-name-type-2")
    name = p_name.em.text
    #name = name.replace("\n","").replace("\t","")
    name=name.replace("\n","").replace("\t","")
    


    # TODO 格式化输出name price，中间空一格
    print(f"{name} {price}")