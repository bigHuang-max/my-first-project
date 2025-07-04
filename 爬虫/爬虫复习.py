###分析网页
#一般的网页信息就在网页源代码中，我们只要找到网页源代码，根据节点就能提取到信息
想要提取节点，我们需要先导入相关的模块解析网页  -----EX BeautifulSoup

创建一个 BeautifulSoup 对象，传入变量 xml 和解析器 lxml，在赋值给变 soup。
soup = BeautifulSoup(xml,"lxml")
接着使用 find_all() 函数中，传入 name 参数，其参数值为 d 。将返回的由所有 d 节点组成的###列表###，赋值给变量 content_all。
.content 属性的作用获取二进制数据；.text 属性的作用是获取网页内容；.encoding 属性的作用是找出 requests 模块使用了什么编码方式
1. 一般的网页信息就在网页源代码中，我们只要找到网页源代码，根据节点就能提取到信息。

例如：
课程中的网页有豆瓣网项目、马蜂窝项目、飞猪项目等；
百题斩中的有网易新闻、糗事百科、百度百科、百度贴吧、应届生求职网等等。
#2. 部分网站的数据是通过调用 API接口 来展示的，在爬取这类网站时，我们要分析信息存储地址，找到对应的 API接口 去请求数据。
2. 部分网站的数据是通过调用 API接口 来展示的，在爬取这类网站时，我们要分析信息存储地址，找到对应的 API接口 去请求数据。

例如：
课程中学到的获取B站弹幕项目，类似的网站还有腾讯视频、爱奇艺、优酷等视频网站的弹幕数据。
#3. 还有一些网页会使用动态加载技术，将信息存储在JavaScript文件中。
3. 还有一些网页会使用动态加载技术，将信息存储在JavaScript文件中。

在爬取这类网站中的内容时，我们要在开发者模式中，找到文件类型为script，数据格式为JSON格式，请求文件链接解析JSON数据。

例如：
课程中学到的爬取商品评论项目，类似的还有B站视频评论数据，也需要找到JavaScript文件再请求和提取信息。
###请求网页
URL全称为Uniform Resource Locator，即统一资源定位符，指定了我们要查找资源的地址。 URL组成结构：访问协议 + : + // + 主机名 + / + 文件路径名（可省略）
1. 请求网页需要导入 requests模块 ，并调用该模块中的 get() 函数，少数网站我们直接使用requests.get()请求URL获取内容。

例如：
课程中案例网站直接请求URL就能获取数据，百题斩中的糗事百科和百度贴吧网站。
2. 但大部分网站都设有反爬虫机制，所以请求网页时需要设置请求头参数，常见的在headers中以字典的格式带上User-Agent即可。

例如：
课程中的豆瓣电影评论、批量提取海报图片和实习僧岗位项目，添加User-Agent就可以访问。
3. 还有许多网页设有其他反爬虫措施，不仅检查User-Agent信息还会检查请求头中的Cookie信息，用于辨别用户的身份。
例如：
课程中学习的爬取商品信息项目，请求头中的Cookie会直接影响返回的数据信息。类似的网站有各种涉及到账号和密码登录的购物网站。
在我们浏览网站时，某些网站的服务器会给用户浏览器发送一小块数据，用于辨别用户身份，这个就是Cookie，作用是保存用户的浏览数据，对用户身份起到辨识作用。
在进行 HTTP 请求的时候，除了请求指定的 url 信息之外，还会告诉服务端“我是谁”，“我支持哪些特性”，这些信息就是 HTTP 请求的头部 ，其中声明“我是谁”的就是 HTTP 请求头部的 User-Agent

例如：
课程中学习的爬取商品信息项目，请求头中的Cookie会直接影响返回的数据信息。类似的网站有各种涉及到账号和密码登录的购物网站。
###提取数据
1. 拿到网页源代码后，常见的HTML格式的网页需要导入bs4模块来解析网页内容，课程中绝大部分项目都可以使用bs4模块来解析。
全称为HyperText Markup Language，超文本标记语言，它定义了网页内容和结构。
HTML是由一系列的元素组成，这些元素组合起来就是我们浏览器看到的网页。
Beautiful Soup是Python的一个HTML或XML的解析模块，可以用它来从网页中提取想要的数据。

使用 BeautifulSoup() 函数，创建一个 BeautifulSoup 对象，传入 HTML 文本和解析器 lxml。   
例如：
豆瓣电影评论、批量提取海报图片项目等等。
#BeautifulSoup案例
from bs4 import BeautifulSoup
html = '''
<title>网络爬虫课程</title>
<body>
    <h1 align="center">我的第一个标题-居中显示</h1>
    <h2>我的第二个标题，不居中显示</h2>
    <p>我的第一个段落
    </p>
'''
soup = BeautifulSoup(html, "lxml")
print(soup)
<html><head><title>网络爬虫课程</title>
</head><body>
<h1 align="center">我的第一个标题-居中显示</h1>
<h2>我的第二个标题，不居中显示</h2>
<p>我的第一个段落
    </p>
</body></html>
2. 但有时我们获取到的数据是乱码的，这是由于网页编码和字体反爬虫等原因造成的。

例如：
课程中获取B站弹幕项目中，直接提取的网页内容是乱码的，这是需要先对网页转码。
在实习僧岗位项目中，需要对字体进行解码再提取内容。
encoding 属性，找出 requests 模块使用了什么编码方式，

.apparent_encoding 属性会从网页的内容中分析网页编码的方式。
3. 但当我们从JavaScript文件中提取信息时，由于该文件中的内容使用JSON格式存储数据，这时需要根据JSON格式来提取内容。
JavaScript的缩写为JS，JavaScript是一门编程语言，当应用在HTML文档时，可为网站提供动态交互效果。
JSON是JavaScript Object Notation的缩写，是一种用来存储和传输数据的格式，通常用于服务端向网页传递数据。
数据以 {键:值} 的形式呈现，数据与数据之间以逗号分隔，方括号[]表示数组，大括号{}用于保存对象
json.loads()函数能够对数据进行解码，将JSON数据与Python的数据类型进行转化。
例如：
课程中学习的爬取商品信息项目，需要从JSON数据中提取评论信息。
# .string 属性， .text 属性和 .contents 属性。区别
.string 属性是用来获取节点中标签内容。
.text 属性能够获取该节点下所有的文字内容。
想要获取子节点，我们可以访问 .contents 属性，得到的结果是包含子节点的列表。
1. .string提取单个节点中的文本内容，若存在多个节点就会输出None；
2. .text即可提取单个节点，也可提取多个节点信息，以字符串格式输出；
3. .contents提取多个节点信息，并以列表形式输出。
html="""
<ul>some text</ul>
<ul></ul>
<ul><li>more text</li></ul>
<ul>even <li>more text</li></ul>
"""
# 使用from...import从bs4导入BeautifulSoup
from bs4 import BeautifulSoup

# 使用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
soup = BeautifulSoup(html, "lxml")

# 使用find_all()查询ul标签，赋值给content_all
content_all = soup.find_all("ul")

# 使用for循环遍历每项内容
for content in content_all:
    print(content.string)-----
some text
None
more text
None
从输出结果中可以看到，代码中第2、4行的<ul>标签中信息是可以提取的，第3行中的标签为空返回了None；第5行中even和more text包含在两个标签中，返回None。

原因是.string遇到标签中没有信息会返回None，遇到多个标签中都有文本信息时，不知道提取哪个就返回None。

for content in content_all:
    print(content.text)    
some text

more text
even more text
从输出结果可以看出，代码中第2、4行信息输出与.string内容一致，第3行<ul></ul>中没有内容则返回空的。

第5行的even和more text在<ul>中，就会返回<ul>中所有的信息，包括它的下级节点中的信息。
['some text']
[]
[<li>more text</li>]
['even ', <li>more text</li>]    
从输出结果可以看出，.contents以列表的形式返回每个<ul>标签中的信息，标签中无信息就返回空列表，代码中第4行的标签中嵌套了一个<li>标签，就将内容和<li>标签全部返回。

第5行的<ul>标签中嵌套了多个元素，就将多个元素以列表的形式返回。
###保存分析
提取到数据后，可以直接输出或将数据保存到文档中，课程中讲解了两种保存方式，使用with...as语句配合open()函数来保存文件，使用pandas模块将数据写入到Excel文档中。

例：
我们使用with...as语句在实习僧岗位项目中提取岗位信息保存为txt文档。   这种方法自带close函数，防止文件损坏
使用pandas在每日报表项目将提取到的旅游信保存到Excel中。
####
这段时间我们学到的知识仅支持我们爬虫入门，课程案例没有覆盖所有网站，所教方法不能爬所有内容。

我们在课下练习时，一定会遇到更多的反爬虫策略，反爬虫是动态的，不可能穷举，需要具备获取新知识的能力。

这里的搜索引擎我们希望有条件的同学可以使用Google搜索引擎搜索错误类型和知识点，要知道你踩过的坑大家都踩过。
优先谷歌，其次百度，最后必应
###
我们在用代码实现某一功能的时候，很难一次性将代码就写得完全没有错误。

当错误出现的时候，如何去定位并解决错误，也是一个需要掌握的技能。

我们在日常练习中要尝试去Debug，定位报错信息找到错误。(Debug就是抓虫，定位报错信息并解决)

如果遇到自己无法解决的错误类型就去浏览器检索该错误，找到解决方案，要知道你遇到的bug敲过代码的都会遇到。
###
最后的最后，我们来聊聊数据可视化，课程中大部分项目都会对爬取到的数据进行处理，目的是将提取到的内容进行可视化展示。

但Python网络爬虫的核心作用是从网页中获取信息，爬虫是获取信息的渠道之一。

如果你想要对数据进行进步处理，还需要去了解数据分析和数据可视化的知识点。
########常见函数
将分隔符作为参数传入到split()函数中，即可把字符串按照指定分隔符切分成多个字符串组成的列表。
data = "43.49200,1,25,16777215,1596185022,0,a9d6f86d,36198336480935939"

dataList = data.split(",")

print(dataList)

code editor
data = "43.49200,1,25,16777215,1596185022,0,a9d6f86d,36198336480935939"

dataList = data.split(",")

print(dataList)

['43.49200', '1', '25', '16777215', '1596185022', '0', 'a9d6f86d', '36198336480935939']
time = data.split(",")[0]

43.49200
############数据处理
#如果strip()的参数为空，那么会默认删除字符串头和尾的空白字符(包括\n，\r，\t这些)。