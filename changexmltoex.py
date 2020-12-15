#从xml文件里获得数据
import  xml.dom.minidom
import xlwt
import xml.etree.ElementTree as ET
import pandas as pd

#打开xml文档
dom = xml.dom.minidom.parse('E:/senior/traffic prediction/data/traffic-matrices-anonymized-v2/traffic-matrices/IntraTM-2005-01-01-00-30.xml')

#得到文档元素对象
root = dom.documentElement

dstt = root.getElementsByTagName('dst')
dst= dstt[0]
#print(b.firstChild.data)
dst=dst.firstChild.data

datee = root.getElementsByTagName('date')
date= datee[0]
#print(c.firstChild.data)
date=date.firstChild.data


dst_list=[]
date_list=[]
dst_list.append(dst) #将获得的数据存入列表
date_list.append(date)

all_dict={'date':date_list,'dst':dst_list} #将列表存储为字典
df = pd.DataFrame(all_dict) #将字典转换为DataFrame

#将DataFrame数据写入excel表中
with pd.ExcelWriter('E:/senior/traffic prediction/data/test.xlsx') as Writer:
    df.to_excel(Writer,'Sheet1',index=False)
