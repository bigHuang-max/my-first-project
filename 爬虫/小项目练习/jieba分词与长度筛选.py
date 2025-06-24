# -*- coding: utf-8 -*- 
import jieba

contents=["小王子是一个超凡脱俗的仙童，他住在一颗只比他大一丁点儿的小行星上。",
"陪伴他的是一朵他非常喜爱的小玫瑰花，但玫瑰花的虚荣心伤害了小王子对她的感情。",
"小王子告别小行星，开始了遨游太空的旅行。",
"他先后访问了六个行星，各种见闻使他陷入忧伤，他感到大人们荒唐可笑、太不正常。",
"只有在其中一个点灯人的星球上，小王子才找到一个可以作为朋友的人。",
"但点灯人的天地又十分狭小，除了点灯人他自己，不能容下第二个人。",
"在地理学家的指点下，孤单的小王子来到人类居住的地球。"]
#len()
#使用len()函数计算词语的长度，如果长度等于1，说明该为单字或标点。

# 定义字符串name = "Joy"
#name = "joy"

# 使用len()函数计算name的长度
#name_len = len(name)

# 使用print()输出长度
#print(name_len)

#输出结果
#3
#jieba 不是一个内置模块，所以在使用前要先通过代码 pip install jieba 在终端中进行安装。

#如果在自己电脑上安装不上或安装缓慢，可在命令后添加 -i https://pypi.tuna.tsinghua.edu.cn/simple/ 进行加速。

for content in contents():
    words=jieba.lcut(content)
    for word in words:
        if len(word)>1:
            print(word)
        else:
            continue    
