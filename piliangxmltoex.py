#https://www.cnblogs.com/fnng/p/3581433.html
#https://blog.csdn.net/yourgreatfather/article/details/84031289
import os
import os.path
import xml.dom.minidom
import pandas as pd

path = 'E:/senior/traffic prediction\data/traffic-matrices-anonymized-v2/traffic-matrices/'
files = os.listdir(path)  # 得到文件夹下所有文件名称
dst_list=[]
date_list=[]
for xmlFile in files:  # 遍历文件夹
        #if not os.path.isdir(xmlFile):  # 判断是否是文件夹，不是文件夹才打开
        #print (xmlFile)
        # xml读取操作
        # 将获取到的xml文件名送入到dom解析
        # 错误代码：dom=xml.dom.minidom.parse(xmlFile)
        dom = xml.dom.minidom.parse(os.path.join(path, xmlFile))
        root = dom.documentElement

        dstt = root.getElementsByTagName('dst')
        dst = dstt[0]
        dst = dst.firstChild.data

        datee = root.getElementsByTagName('date')
        date = datee[0]
        date = date.firstChild.data

        dst_list.append(dst)  # 将获得的数据存入列表
        date_list.append(date)

all_dict={'date':date_list,'dst':dst_list} #将列表存储为字典
df = pd.DataFrame(all_dict) #将字典转换为DataFrame

#将DataFrame数据写入excel表中
with pd.ExcelWriter('E:/senior/traffic prediction/data/test.xlsx') as Writer:
    df.to_excel(Writer,'Sheet1',index=False)
