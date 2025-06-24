
import requests
import json

headers = {
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
}
#找到json文件链接
resp=requests.get('https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=70313165327&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',headers=headers)
html=resp.text
# resp=html.replace("fetchJSON_comment98(",""),replace(");"'")
#resp=content.replace("fetchJSON_comment98("," ")
#resp=content.replace(");"," ")
html=html.lstrip("fetchJSON_comment98(")
# url 是 获取的js文件 评论数据链接 ：JS 提供动态效果 ex: 骨骼 + 肌肉
html=html.rstrip(");")

#json_data=json.loads(resp)
json_data=json.loads(html)
#coc=json_data['coc']
coc=json_data["comments"]
#print(coc)

for item in coc:
    prodcutcolor=item["productColor"]
    print(f"{prodcutcolor}")
    

