#我们还会接触到许多的第三方模块。这些非内置的模块由其他的开发者所编写，提供给公众免费使用，功能更加个性化。同学们可以从Python Package Index上找到自己需要的模块。
#python package Index 需要科学上网  https://pypi.org/
#内置模块可以直接导入后使用，而非内置的模块则需要先进行安装，然后才能导入使用。
哥的地址/Users/生活黑客/OneDrive/桌面/VS code
#####################随机数
import random
randomNum = random.random()
print(randomNum)
import random
randomNum = random.randint(1,7)
print(randomNum)
##############
#如何一次性替换多个字符？

#多次使用replace()函数替换字符串

#代码示例
str = "this is string example....wow!!! this is really string"
str.replace("is", "was").replace("this", "that")
print(str)

#输出结果
#that was string example....wow!!! that was really string
#########################
#split()函数默认分割任意形式的空白字符：空格、tab、换行、回车以及formfeed，并将结果返回一个列表。

str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
num -- 分割次数。默认为 -1, 即分隔所有
str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print str.split( );       # 以空格为分隔符，包含 \n
print str.split(' ', 1 ); # 以空格为分隔符，分隔成两个
以上实例输出结果如下：

['Line1-abcdef', 'Line2-abc', 'Line4-abcd']
['Line1-abcdef', '\nLine2-abc \nLine4-abcd']
####################
#join()函数

"".join(list)能够将list列表转换成字符串。

num = ["a", "b", "c", "d", "e"]
string = "".join(num)
print(string)
输出结果
abcde

####
quote()函数#######################################################################################

位于urllib.parse模块中的quote()函数可以将中文参数转换为URL编码的格式。

代码示例：
# 使用import导入urllib.parse模块
import urllib.parse

# 使用urllib.parse.quote()函数
chengdu = urllib.parse.quote("成都")

# 输出url
print(chengdu)


输出结果：
%E6%88%90%E9%83%BD
常用反爬虫机制#######################################
headers = { "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
"cookie":"shshshfpa=59756f24-6de8-90a9-92f3-022a321cbcaa-1589969605; __jdu=1589969605288365795565; shshshfpb=fZNp5OzH0j2T%20X%20WnJhzrBg%3D%3D; qrsc=3; user-key=b05356ef-c40b-44d2-a837-60df17e9b74e; cn=0; _pst=jd_51aaae03cedfa; unick=jd_51aaae03cedfa; pin=jd_51aaae03cedfa; _tp=FNP1fTo2ON7jgdbikn0lWAbSqMI20pF0xO0Iq%2FccQVc%3D; pinId=qN40m03yULDpSLzjaHwm07V9-x-f3wj7; __jdc=122270672; rkv=1.0; 3AB9D23F7A4B3C9B=DVCEDHG6BLYWMZMJIWNBOSTWP7GOWK77C5VJKGVQO7F3JHUFZVL5V5B5UKDYLF2LK5VAEIOSN2YRG33EJLXR6ZJ2TU; __jdv=122270672|direct|-|none|-|1602475191357; areaId=22; ipLoc-djd=22-1930-50947-0; __jda=122270672.1589969605288365795565.1589969605.1602487075.1602569356.29; shshshfp=b393a5ab6c1163583435b3a90574cb22; shshshsID=ef428a912dae95ba61fd7ac2ee0af172_9_1602570753319; __jdb=122270672.9.1589969605288365795565|29.1602569356"}
##################爬表格 or 遇到多个名称一样的标签页，用contents[]函数，不过要填奇数！！！！！
content:
  <td> 广东</td>
  <td> 审计署驻深圳特派员办事处</td>
  <td class="job_name"> 审计业务处一级主任科员及以下</td>
  <td> 计算机科学与技术</td>
  <td> 本科或硕士研究生</td>
print(content.contents[1] content.contents[2] content.contents[3])
结果：
    广东   审计署驻深圳特派员办事处
#################### sorted函数: 可以对字典进行排序
# 定义知识点和平均扣分的字典
knowledge = {"圆锥曲线":7.5,"直线与圆":5.0,"立体几何":10.1,"空间向量":3.2,"数列":14.5,"解三角":1.9,"导数":28.5,"函数模型":3.3,"二项式定理":3.0,"线性规划":4.0,"平面向量":3.5,"复数":1.3,"集合":1.9}
result= sorted(knowledge.items(),key=lambda item:item[1],reverse=True)
print(result)
[('导数', 28.5), ('数列', 14.5), ('立体几何', 10.1), ('圆锥曲线', 7.5), ('直线与圆', 5.0), ('线性规划', 4.0), ('平面向量', 3.5), ('函数模型', 3.3), ('空间向量', 3.2), ('二项式定理', 3.0), ('解三角', 1.9), ('集合', 1.9), ('复数', 1.3)]
