# 使用import导入requests模块
import requests
# 使用from..import从bs4模块导入BeautifulSoup
from bs4 import BeautifulSoup
# 导入pandas模块并以pd调用
import pandas as pd

# 创建用来存入标题，链接，天数的列表
titlist = []
linguist = []
daylit = []

# 将User-Agent以字典键对形式赋值给headers
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

# 使用for循环和range()生成1-5的变量并遍历
for i in range(1, 25):

    # 使用格式化组合链接，赋值给url
    url = f"https://nocturne-spider.baicizhan.com/practise/56/PAGE/{i}.html"
    # 使用request()函数，将url作为参数传入，并将返回值赋值给变量response
    response = requests.get(url,headers=headers)
    # 将服务器响应内容转换为字符串形式，赋值给html
    html = response.text
    # 用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
    soup = BeautifulSoup(html,"lxml")

    # 使用find_all()查询soup中class=list_item的节点，赋值给booklist
    bookList = soup.find_all(class_="list_item")

    # 使用for循环遍历booklist
    for book in bookList:

        # TODO 使用节点选择器，选择到book.h2.a["href"]
        # 并与"https://travel.qunar.com"拼接后赋值给link
        # 使用append()将拼接后的链接添加进linklist
        link = "https://travel.qunar.com" + book.h2.a["href"]
        linguist.append(link)
        
        # TODO 使用节点选择器，选择到book.h2.a.text，并赋值给title
        # 使用append()将title添加进titlelist
        title = book.h2.a.text
        titlist.append(title)
        

        # TODO 使用find()查询book中class="days"的节点
        # 使用.string获取days节点中的文本内容，赋值给days
        # 使用append()将days添加进dayslist
        days = book.find(class_="days")
        days = days.string
        daylit.append(days)
        


# TODO 将标题，链接和天数转换成字典类型数据，赋值给total
# "标题":titlelist,"链接":linklist,"天数":dayslist
total = {"标题":titlist,"链接":linguist,"天数":daylit}
# TODO 使用pd.DataFrame()函数，将参数传入函数中，对数据进行转化，赋值给info
info = pd.DataFrame(total)
# TODO 使用pd.ExcelWriter()函数打开/Users/去哪儿旅游.xlsx，赋值给writer
writer = pd.ExcelWriter("/Users/生活黑客/OneDrive/桌面/VS code//去哪儿旅游.xlsx")
# TODO 使用to_excel将数据info写入writer文档中，并设置sheet_name为上海
info.to_excel(excel_writer=writer,sheet_name="上海")

# 保存文件
writer.save()
print("生成over")