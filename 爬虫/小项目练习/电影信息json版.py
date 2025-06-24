import requests
import json

for i in range(0,20):
    page=i*10
    
   
    url=f"https://spa1.scrape.center/api/movie/?limit=10&offset={page}"
    response=requests.get(url)
    html=response.text
    #转换成字典格式
    json_data=json.loads(html)
    data=json_data["results"]
    for content in data:
        name=content["name"]
        time=content["published_at"]
        cover_url=content["cover"]
        print(f"{name} {time} {cover_url}")
        
    