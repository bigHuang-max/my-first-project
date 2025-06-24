import requests 
import json 
#如果在 soup 里 find_all("class_=tag-1)返回的是空列表  因为html 只是框架，内容是JavaScript ，用浏览器渲染出的
# 获取步骤 ： 商品评价页面 - network - js - productPageComments -copy link 
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
url="https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=1178886&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1"
res=requests.get(url,headers=headers)
html=res.text

html=html.lstrip("fetchJSON_comment98(")
# url 是 获取的js文件 评论数据链接 ：JS 提供动态效果 ex: 骨骼 + 肌肉
html=html.rstrip(");")
#####移除左右两边的内容后，剩下的内容结构与Python中的字典数据类似。

#####而输出的数据类型是字符串str，我们需要将获取到的str数据转换成字典数据类型。
#json.loads() 函数能够对数据进行解码，将JSON数据与Python的数据类型进行转化，目的是能在Python中处理JSON数据 。
#解码成的数据类型需要看JSON对应的格式，格式为字典就会转成字典，为列表就会转成列表。

#print(type(html))======str
json_data=json.loads(html)
#print(type(json_data))    
#print(json_data)
data = json_data["hotCommentTagStatistics"]
#print(data)---------------输出的内容是列表类型，列表中的每一项是一个商品评价标签。



#输出的内容data是列表类型，列表中的每一项是一个商品评价标签。
#使用for循环逐个遍历列表中的每项，并输出查看内容结构。
for item in data:
    name=item["name"]
    count=item["count"]
    print(f"{name} {count}" )
    

