# hello world 
import requests
from bs4 import BeautifulSoup
headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
}
url="http://cet-bm.neea.edu.cn"
response=requests.get(url,headers=headers)
print(response.status_code)