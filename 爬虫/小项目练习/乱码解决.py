#如果出现乱码的问题，尝试使用 response.encoding = 'utf-8' 或许可以解决乱码哟。
#出现乱码的原因是网页编码和爬取下来后的编码转换不一致。

#网页编码和 requests 模块编码分别是什么呢？在这里，我们可以使用相关属性获取编码方式。
#requests.get()请求发出后，requests 模块会基于 HTTP 头部作出推测。

#在使用 .text 属性前，requests 模块会使用推测出来的文本编码。

#我们可以使用 .encoding 属性，找出 requests 模块使用了什么编码。
#print(response.encoding)
#ISO-8859-1
#.apparent_encoding 属性会从网页的内容中分析网页编码的方式。

#print(response.apparent_encoding)
#utf-8
###############字体反爬虫######
#所谓字体反爬虫，就是一些关键数据在网页上查看时，它是正常显示的；而当查看网页的 HTML 代码时，却呈现出一个个的方块。这样我们就没办法将网页上的数据直接爬取下来。

#虽然有字体反爬虫，我们也有办法破解它。HTML 代码中的小方格与网页中数字的对应一定存在某种规则。

#这种规则是网站自己的一套编码方式，在这里我们可以绕道而行。
##################
#我们可以先把小方格用其他的编码方式重新编码，比如说“UTF-8”编码。
#字母和数字经过编码后格式不变；每个中文字符对应三个“\”分割的字符内容
#想要将字符串转换成二进制数据，在这里我们可以使用 encode() 函数，实现“编码”。

#在 encode() 函数中默认 UTF-8 编码，由于它是针对英语设计的，中英文字符转码后会有差异。
alp = "yequ"
num = "666"
word = "夜"
words = "夜曲" 
print(alp.encode())
print(num.encode())
print(word.encode())
print(words.encode())
b'yequ'
b'666'
b'\xe5\xa4\x9c'
b'\xe5\xa4\x9c\xe6\x9b\xb2'
#替换完成后，接下来就要将新的二进制数据转换成字符串，这个过程就叫做“解码”，我们可以使用 decode() 函数。

#decode() 函数默认 UTF-8 方式解码，要注意的是编码 encode() 函数和解码的方式需要保持一致，不然程序会报错哦～

#找到编码后的二进制数据与网页薪资数字之间的对应关系，然后将它们进行替换。
words = "I Love 夜曲"
words_bytes = words.encode()
print(words_bytes)
words_new = words_bytes.decode()
print(words_new)
#b'I Love \xe5\xa4
#I Love 夜曲
#课程中的编码和解码方法是通用的，但是对应的编码会不定时更新，在做练习时需要自己获取哦～


#接着将二进制数据，再转换成字符串，就可以破解字体反爬虫机制，获取到薪资数据啦～
#当我们使用 .text 属性获取网页内容的时候，使用的是 .encoding 进行编码，但是基于 HTTP 头部分析出来的编码不一定正确，就造成了乱码。

#.apparent_encoding 是通过内容分析出编码，有一定准确率。遇到乱码的时候，可以作为爬虫备选的编码方式
#requests模块使用了 ISO-8859-1 编码，网页使用了 utf-8 编码，编码方式不一样，难怪会出现中文乱码。

#在这里，我们可以对 response.encoding 属性重新赋值，即可修改编码。
###########解决方案
#response.encoding = response.apparent_encoding
#######################################     EX   ###############
# 使用import导入requests模块
import requests

# 将https://comment.bilibili.com/218710655.xml赋值给变量url
url = "https://comment.bilibili.com/218710655.xml"

# 将变量url作为参数，添加进requests.get()中，给赋值给response
response = requests.get(url)

# 使用.apparent_encoding属性获取网页编码方式
# 将网页编码方式赋值给response.encoding
response.encoding = response.apparent_encoding

# 使用.text属性获取response内容，赋值给xml
xml = response.text

# 使用print输出xml
print(xml)
