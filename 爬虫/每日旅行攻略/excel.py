import pandas as pd
list_color=["迈巴赫-黑色",
"迈巴赫-黑色",
"劳斯莱斯-黑色",
"劳斯莱斯-黑色",
"迈巴赫-红色",
"劳斯莱斯-黑色",
"劳斯莱斯-黑色",
"劳斯莱斯-黑色",
"劳斯莱斯-黑色",
"迈巴赫-黑色"]
info=pd.DataFrame(list_color)
writer=pd.ExcelWriter("/Users/生活黑客/OneDrive/桌面/VS code/志伟的劳斯莱斯颜色.xlsx")
info.to_excel(excel_writer=writer,sheet_name="fange's dreamcar")
writer.save()

