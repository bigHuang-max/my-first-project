path="/Users/生活黑客/OneDrive/桌面/VS code/商品信息.txt"        
#aim : 一些商品中，出现频率高的内容。
from pyecharts.charts import Bar
  
with open(path, "r") as f:

    # 使用readlines()函数读出商品信息文档中的内容，赋值给read_content
    read_content = f.readlines()
    

# TODO 使用for循环遍历read_content
comment_dict={}    
for content in read_content :
   
    
  
    # TODO 使用strip()将\n移除，并赋值给content
    content=content.strip("\n")
    # TODO 使用print()输出数据类型
    #print(type(content)) -------str
    content=eval(content)
    #print(type(content))-------dict
    # 使用items()将字典转成列表形式，并赋值给content_list
    content_list=content.items()
    # 使用for循环遍历content_list
    for key, value in content_list:
        if key not in comment_dict:
            comment_dict[key]=1
        else:
            comment_dict[key]+=1
bar=Bar()
# 使用list()将字典comment_dict所有键转换成列表，传入add_xaxis()中
bar.add_xaxis(list(comment_dict.keys()))
# 使用add_yaxis()函数，将数据统称设置为"评价频次"
# 将字典comment_dict所有值，作为参数添加进函数中
bar.add_yaxis("评价频次", list(comment_dict.values()))
# 使用render()函数存储文件，设置文件名为"comments.html"
bar.render("comments.html")         



        
    

