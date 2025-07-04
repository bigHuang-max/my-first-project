#她想到可以从《后浪》这个视频中，找出发弹幕最积极的10个用户，邀请他们做访谈。

#在“后浪（上）”我们已经获取到了 XML 代码，在这里我们可以继续编写，获取发弹幕数最多的10个用户。
#from collections import Counter
#wordList = ['html', 'js','js', 'css', 'python' 'python' 'python']
#word_counts = Counter(wordList)
#print(word_counts)
#top_two = word_counts.most_common(2)
#print(top_two)-----------------[('python', 3), ('js', 2)]
import requests

# 从bs4中导入BeautifulSoup模块
from bs4 import BeautifulSoup

# TODO 从collections中导入Counter模块

from collections import Counter
# 将获取到的含有cid的xml地址，赋值给变量url
url = "https://nocturne-spider.baicizhan.com/practise/30.xml"

# 将变量url作为参数，添加进requests.get()中，给赋值给response
response = requests.get(url)

# 使用.text属性获取response内容，赋值给xml
xml = response.text

# 使用BeautifulSoup()读取xml，添加lxml解析器，赋值给soup
soup = BeautifulSoup(xml,"lxml")

# 使用find_all()查询soup中d的节点，赋值给content_all
content_all = soup.find_all("d")

# TODO 创建一个空白列表userList
userList=[]
# TODO for循环遍历content_all
for content in content_all:

    # TODO 使用.attrs获取p对应的属性值，并赋值给data
    data=content.attrs["p"]

    # TODO 使用split()函数分割data，把第7个元素赋值给userID
    userID=data.split(",")[6]

    # TODO 在列表中加入userID
    userList.append(userID)

# TODO 使用Counter()函数统计userList中的词语个数,赋值给user_counts
user_counts=Counter(userList)

# TODO 使用user_counts.most_common()计算出现频率最高的10个用户，赋值给top_ten_user
top_ten_user=user_counts.most_common(10)

# TODO 输出结果top_ten_user
print(top_ten_user)