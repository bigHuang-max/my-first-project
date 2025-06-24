

# 导入requests模块
import requests

# 从bs4中导入BeautifulSoup模块
from bs4 import BeautifulSoup

# 导入time模块
import time
from pyecharts.charts import Bar
# 将User-Agent以字典键对形式赋值给headers
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}

# 定义一个新函数getPositionInfo，包含参数detail_url
def getPositionInfo(detail_url):
    #job 运行不了，没办法
    name="产品经理"
    # 将detail_url和headers参数，添加进requests.get()中，给赋值给res
    res = requests.get(detail_url,headers=headers)

    # 使用.text属性获取网页内容，赋值给html
    html = res.text

    # 用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
    soup = BeautifulSoup(html, "lxml")
    

    # 使用find()函数获取class="new_job_name"的节点
    # 使用attrs属性提取出title的属性值,赋值给变量job
    
    #job = soup.find(class_="new_job_name").attrs["title"]
    

    # 使用find()函数获取class="com-name"的节点
    # 使用.string属性提取出标签内容
    # 使用strip()移除换行符，赋值给companyName
    companyName = soup.find(class_="com-name").string.strip()
    

    # 使用find()函数获取class="job_position"的节点
    # 使用.string属性提取出标签内容，赋值给position
    position = soup.find(class_="job_position").string
    salary=soup.find(class_="job_money cutom_font").string
    salary=salary.encode()
    salary = salary.replace(b"\xee\x8b\xbf", b"0")
    salary = salary.replace(b"\xee\xa2\x9c", b"1")
    salary = salary.replace(b"\xee\x90\xb7", b"2")
    salary = salary.replace(b"\xee\x81\xa5", b"3")
    salary = salary.replace(b"\xee\xad\xb1", b"4")
    salary = salary.replace(b"\xee\xb2\xae", b"5")
    salary = salary.replace(b"\xef\x8a\x98", b"6")
    salary = salary.replace(b"\xef\x80\xa6", b"7")
    salary = salary.replace(b"\xee\xa1\xb1", b"8")
    salary = salary.replace(b"\xee\xbe\xad", b"9")
    salary=salary.decode()
    #注意，课程中的编码和解码方法是通用的，但是对应的编码会不定时更新，在做练习时需要自己获取哦～
     # 使用with...as配合open()函数以a方式，打开路径为"/Users/tongtong/职位数据.txt"的文件，并赋值给f 
    with open("/Users/生活黑客/OneDrive/桌面/VS code/职位数据.txt", "a") as f:
        # 使用write()函数写入job,companyName,position,salary
        # 变量之间以逗号相连，在数据末尾添加换行符
        f.write(name+","+companyName+","+position+","+salary+"\n")


    


    # 使用print格式化输出job,companyName,position
    

# for循环遍历range()函数生成的1-6的数字
for i in range(2,6):

    # 利用格式化字符生成串网站链接 赋值给变量url
    url = f"https://www.shixiseng.com/interns?page={i}&type=intern&keyword=%E4%BA%A7%E5%93%81%E7%BB%8F%E7%90%86&area=&months=&days=&degree=&official=entry&enterprise=&salary=-0&publishTime=&sortType=&city=%E5%85%A8%E5%9B%BD&internExtend="
    
    # 将url和headers参数，添加进requests.get()中，将字典headers传递给headers参数，给赋值给res
    res = requests.get(url, headers=headers)
    
    # 使用.text属性获取网页内容，赋值给html
    html = res.text

    # 用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
    soup = BeautifulSoup(html,"lxml")
    
    # 使用find_all()查询soup中class=title ellipsis font的节点，赋值给titles
    titles = soup.find_all(class_ = "title ellipsis font")

    # for循环遍历列表titles
    for item in titles:

        # 使用.attrs获取href对应的属性值，并赋值给detail_url
        detail_url = item.attrs["href"]

        # 调用getPositionInfo()函数，传入参数detail_url
        getPositionInfo(detail_url)
    
    # 使用time.sleep()停顿2秒
    time.sleep(2)
# 从pyecharts.charts中导入Bar模块


# 使用with...as语句配合open()函数以r方式，打开路径为“/Users/tongtong/职位数据.txt”的文件，赋值给f
with open("/Users/生活黑客/OneDrive/桌面/VS code/职位数据.txt", "r") as f:

    # 使用readlines()读取f中的所有行，赋值给dataList
    dataList = f.readlines()

# 新建一个字典cityDict
cityDict = {}

# for循环遍历列表dataList中的每个元素data
for data in dataList:

    # 如果"薪资面议"在元素中
    if "薪资面议" in data:
        # 就跳过
        continue

    # 使用split()以逗号分隔data，索引第3项元素，赋值给city
    city = data.split(",")[2]

    # 使用split()以逗号分隔data，索引第4项元素，赋值给salary
    salary = data.split(",")[3]

    # 使用split()以斜杠分隔salary，索引第1项元素，赋值给daily
    daily = salary.split("/")[0]

    # 使用split()以短横线分隔daily索引第1项，赋值给start
    start = daily.split("-")[0]
    # 使用split()以短横线分隔daily索引第2项，赋值给end
    end = daily.split("-")[1]

    # 将start和end转换成整型相加后除以2，并赋值给average
    average = (int(start)+int(end))/2

    # 如果city不在字典cityDict的键中
    if city not in cityDict.keys():

        # 将字典中键所对应的值设置为空列表
        cityDict[city] = []

    # 使用append()函数往字典键所对应的值中添加average
    cityDict[city].append(average)

# 新建一个字典city_num_dict
city_num_dict = {}

# for循环遍历cityDict.items()中的key,value
for key,value in cityDict.items():

    # 使用sum()函数将列表value求和
    # 使用len()函数计算列表value长度
    # 使用//运算符计算列表value的平均值，赋值给average_value
    average_value = sum(value)//len(value)

    # 将字典cityDict的键对应的值设置为average_value
    cityDict[key] = average_value

    # 将字典city_num_dict的键设置为不同城市
    # 将对应的值设置为len(value)
    city_num_dict[key] = len(value)

# 创建Bar对象，赋值给bar
bar = Bar()

# 使用list()将字典cityDict所有键转换成列表，传入add_xaxis()中
bar.add_xaxis(list(cityDict.keys()))

# 使用add_yaxis()函数，将数据统称设置为"工资平均值"
# 将字典cityDict所有值转换成列表，作为参数添加进函数中
bar.add_yaxis("工资平均值",list(cityDict.values()))

# 使用render()函数存储文件，设置文件名为salary.html
bar.render("salary.html")

# 创建Bar对象，赋值给bar_city
bar_city = Bar()

# 使用list()将字典city_num_dict所有键转换成列表，传入add_xaxis()中
bar_city.add_xaxis(list(city_num_dict.keys()))

# 使用add_yaxis()函数，将数据统称设置为"职位数量市"
# 将字典city_num_dict所有值转换成列表，作为参数添加进函数中
bar_city.add_yaxis("职位数量",list(city_num_dict.values()))

# 使用render()函数存储文件，设置文件名为positions.html
bar_city.render("positions.html")    
print("success")    
