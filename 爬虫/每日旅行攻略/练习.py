html = """
<title> Example </title>
<ul class="list">
	<li class="item-0">
		<em>first item</em>
        items
	</li>
	<span><li>second item</li></span>
</ul>
"""
# 使用from...import从bs4模块中导入BeautifulSoup
from bs4 import BeautifulSoup
# 使用BeautifulSoup()读取html，添加lxml解析器，赋值给soup
soup = BeautifulSoup(html, "lxml")
# 使用soup定位到ul节点，使用.name提取节点名称，赋值给content
content = soup.ul.name   
# 使用print()输出content
print(content)
