#前5页的地区、部门、用人司局和职位名称。
#1. Excel文档保存路径：/Users/公务员职位信息.xlsx

#2. 工作表命名：计算机科学与技术

#3. 写入顺序为：地区、部门、用人司局和职位名称

##################4. 直接提取<tbody>标签输出内容为空，需要提取<tr>标签；

#5. 取出文字内容写入即可，不需要去除文字中的空格；

#6. 最后生成的Excel格式预览：
import requests
import pandas as pd
from bs4 import BeautifulSoup
headers=headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
areaList = []
departmentList =[]
companyList = []
positionList = []
for page in range(1,6):
    url=f"https://nocturne-spider.baicizhan.com/practise/60/PAGE/{page}.html"
    response=requests.get(url,headers=headers)
    html=response.text
    soup=BeautifulSoup(html,"lxml")
    content_all=soup.find_all("tr")
    for content in content_all:
        if content.find("td")!=None:
            areaList.append(content.contents[1].string)
            departmentList.append(content.contents[3].string)
            companyList.append(content.contents[5].string)
            positionList.append(content.contents[7].string)
            total={"地区":areaList,"部门":departmentList,"用人司局":companyList,"职位名称":positionList}
       
writer=pd.ExcelWriter("/Users/生活黑客/OneDrive/桌面/VS code/公务员职位信息.xlsx")
info=pd.DataFrame(total)
info.to_excel(writer,sheet_name="计算机科学与技术")
writer.save()
writer.close()
print("successfully")