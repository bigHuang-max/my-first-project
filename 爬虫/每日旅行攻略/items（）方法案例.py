mail_dict = {"桐桐":"abd123@yequ.com", "小倩":"def456@yequ.com"}
# 使用items()函数将字典转成可遍历的列表，赋值给mail_list
mail_list = mail_dict.items()
print(mail_list)
for key ,value in mail_list :
    print(f"{key} {value}")