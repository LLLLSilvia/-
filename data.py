import csv

import pandas as pd
import numpy as np
import os
##  ['0385ba42' '05a1ddaf' '19b5c196' '25c17efe' '3813d557' '5d955804' '98eb6753'  'befdbef1' 'd55fdd84']

train = pd.read_csv('F:/Facebook/05a1ddaf_25c17efe.csv', delimiter=',',index_col=False)
train.columns = ["timestamp","packet length","src pod","dst pod"]
#train = np.array(train)
groupby_train_agg = train.groupby(['timestamp'])[('packet length')].agg(['sum'])
#groupby_train_agg = train.groupby(['timestamp']).sum()
print(groupby_train_agg )
# index参数设置为False表示不保存行索引,header设置为False表示不保存列索引
groupby_train_agg.to_csv("F:/Facebook/test.csv",  header=False)




'''
train_col = train[:, 12]
mark = np.where(train_col == '05a1ddaf')
a = train[mark, :].squeeze()
'''
'''

##new_train = np.delete(train, mark,axis = 0)
np.savetxt('F:/Facebook/test.csv', groupby_df_agg, fmt='%s', delimiter=',')
'''


#print(train[:, 13:14])


################################################################################################
import os, sys
import pandas as pd
import numpy as np
path = 'F:/Facebook/CCafterStep/'  # 新建文件夹所在路径
all_files=['0385ba42', '05a1ddaf', '19b5c196' ,'25c17efe', '3813d557' ,'5d955804' ,'98eb6753'  ,'befdbef1' ,'d55fdd84']
all=['25c17efe', '3813d557' ,'5d955804' ,'98eb6753'  ,'befdbef1' ,'d55fdd84']
for src in all:
    for dst in all_files:
        file_name = path + src+'_'+dst
        # 新建文件夹
        os.mkdir(file_name)
        files = os.listdir('F:/Facebook/CCafter/'+src)
        for xmlFile in files:  # 遍历文件夹
            train = pd.read_csv('F:/Facebook/CCafter/'+src+'/' + xmlFile, delimiter=',',header=None, index_col=False)
            train = np.array(train)
            '''
        # 删除intercluster
        train_col = train[:, 13]
        mark_train = np.where(train_col == 1)
        new_train = np.delete(train, mark_train, axis=0)
        # 删除interdatacenter
        train_col = new_train[:, 14]
        mark_train = np.where(train_col == 1)
        new_train = np.delete(new_train, mark_train, axis=0)
            '''
            train = train[:, (0, 1, 12)]
            train_col = train[:, 2]
            mark = np.where(train_col == dst)
            a = train[mark, :].squeeze() # a的目的为dst
            a=np.delete(a,-1,axis=1)
            np.savetxt(file_name+'/'+xmlFile+'.csv', a, fmt='%s', delimiter=',')

################################################################################################
import csv

import pandas as pd
import numpy as np
import os
##  ['0385ba42' '05a1ddaf' '19b5c196' '25c17efe' '3813d557' '5d955804' '98eb6753'  'befdbef1' 'd55fdd84']

train = pd.read_csv('F:/Facebook/1.csv', delimiter=',',header=None,index_col=False)
train = np.array(train)
train_col = train[:, 12]
train_col=np.unique(train_col)
train_time = train[:, 0]
train_time=np.unique(train_time)


print(train_time.size)
'''
mark = np.where(train_col == 1)
## a = train[mark, :].squeeze()

new_train = np.delete(train, mark,axis = 0)
np.savetxt('F:/Facebook/1.csv', new_train, fmt='%s', delimiter=',')
'''

#print(train[:, 13:14])

################################################################################################
import csv
import pandas as pd
import numpy as np
import os
## ['25c17efe','0385ba42','98eb6753','d55fdd84','05a1ddaf','5d955804','befdbef1','19b5c196','3813d557','dcc3db06']
all_files=['0385ba42', '05a1ddaf', '19b5c196' ,'25c17efe', '3813d557' ,'5d955804' ,'98eb6753'  ,'befdbef1' ,'d55fdd84']

for dst in all_files:
    file_name = 'F:/Facebook/CCafterStep/05a1ddaf_' + dst
    # 新建文件夹
    files = os.listdir(file_name)
    for xmlFile in files:  # 遍历文件夹
        train = pd.read_csv('F:/Facebook/CCafter/' + src + '/' + xmlFile, delimiter=',', header=None, index_col=False)
        train = np.array(train)
        '''
    # 删除intercluster
    train_col = train[:, 13]
    mark_train = np.where(train_col == 1)
    new_train = np.delete(train, mark_train, axis=0)
    # 删除interdatacenter
    train_col = new_train[:, 14]
    mark_train = np.where(train_col == 1)
    new_train = np.delete(new_train, mark_train, axis=0)
        '''
        train = train[:, (0, 1, 12)]
        train_col = train[:, 2]
        mark = np.where(train_col == dst)
        a = train[mark, :].squeeze()  # a的目的为dst
        a = np.delete(a, -1, axis=1)
        np.savetxt(file_name + '/' + xmlFile + '.csv', a, fmt='%s', delimiter=',')



'''
train = pd.read_csv('F:/Facebook/10000000_101807750289815_2824765029545410560_n.csv', delimiter=',',header=None,index_col=False)
train = np.array(train)
train_col = train[:, 12]
train = np.unique(train_col)
print(train)
'''


'''
train_col = train[:, 11]
mark = np.where(train_col == '05a1ddaf')
a = train[mark, :].squeeze()

np.savetxt('F:/Facebook/3.csv', a, fmt='%s', delimiter=',')
'''



#print(train[:, 13:14])
################################################################################################
import csv
import pandas as pd
import numpy as np
import os
b = np.zeros((1, 15))
files = os.listdir('F:/Facebook/CC')
all_src=['19b5c196', '25c17efe' ,'3813d557' ,'5d955804' ,'98eb6753' ]
for xmlFile in files:  # 遍历文件夹
    train = pd.read_csv('F:/Facebook/CC/'+xmlFile, sep='\t',header=None,index_col=False)
    train = np.array(train)
    # 删除intercluster
    train_col = train[:, 13]
    mark_train = np.where(train_col == 1)
    new_train = np.delete(train, mark_train, axis=0)
    # 删除interdatacenter
    train_col = new_train[:, 14]
    mark_train = np.where(train_col == 1)
    new_train = np.delete(new_train, mark_train, axis=0)

    train_col = new_train[:, 11]
    for src in all_src:
        mark = np.where(train_col == src)
        a = new_train[mark, :].squeeze()  # a的源为05a1ddaf
        np.savetxt('F:/Facebook/CCafter/'+src+'/' + xmlFile + '.csv', a, fmt='%s', delimiter=',')


    '''
    b = np.append(b, a, axis=0)

b = b[1:, :]
np.savetxt('F:/Facebook/C_intercluster.csv', b, fmt='%s', delimiter=',')


#print(train[:, 13:14])
    
    
    '''
################################################################################################
import os, sys
import pandas as pd
import numpy as np
path = 'F:/Facebook/CCafterStep/'  # 新建文件夹所在路径
all_files=['0385ba42', '05a1ddaf', '19b5c196' ,'25c17efe', '3813d557' ,'5d955804' ,'98eb6753'  ,'befdbef1' ,'d55fdd84']

for src in all_files:
    for dst in all_files:
        file_name = path + src+'_'+dst
        files = os.listdir(file_name)
        for xmlFile in files:  # 遍历文件夹
            train = pd.read_csv(file_name+'/' + xmlFile, delimiter=',',header=None, index_col=False)
            train.columns = ["timestamp", "packet length"]
            # train = np.array(train)
            groupby_train_agg = train.groupby(['timestamp'])[('packet length')].agg(['sum'])
            # groupby_train_agg = train.groupby(['timestamp']).sum()
            # print(groupby_train_agg)
            # index参数设置为False表示不保存行索引,header设置为False表示不保存列索引
            groupby_train_agg.to_csv(file_name+'/' + xmlFile, header=False)

'''
#新建文件夹
for file in all_files:
    for file1 in all_files:
        file_name = path + file +'_'+file1
        os.mkdir(file_name)
'''
################################################################################################
import csv
import pandas as pd
import numpy as np
import os
'''
Folder_Path = r'F:\Facebook\C1'          #要拼接的文件夹及其完整路径，注意不要包含中文
SaveFile_Path =  r'F:\Facebook\C3'       #拼接后要保存的文件路径
SaveFile_Name = r'1.csv'              #合并后要保存的文件名
files = os.listdir(Folder_Path)
for xmlFile in files:  # 遍历文件夹
    train = pd.read_csv(Folder_Path + '/' + xmlFile, delimiter=',', header=None, index_col=False)
    train.to_csv(SaveFile_Path + '\\' + SaveFile_Name, encoding="utf_8_sig", index=False, header=None,mode='a+')
'''
##  ['0385ba42' '05a1ddaf' '19b5c196' '25c17efe' '3813d557' '5d955804' '98eb6753'  'befdbef1' 'd55fdd84']

path = 'F:/Facebook/CCafterStep1/'  # 拼接后要保存的文件路径
Folder_Path = 'F:/Facebook/CCafterStep/'          # 要拼接的文件夹及其完整路径
all_files=['0385ba42', '05a1ddaf', '19b5c196' ,'25c17efe', '3813d557' ,'5d955804' ,'98eb6753'  ,'befdbef1' ,'d55fdd84']
for src in all_files:
    for dst in all_files:
        files = os.listdir(Folder_Path + src+'_'+dst)
        SaveFile_Name = src+'_'+dst+'.csv'  # 合并后要保存的文件名
        for xmlFile in files:  # 遍历文件夹
            train = pd.read_csv(Folder_Path + src+'_'+dst+'/' + xmlFile, delimiter=',',header=None, index_col=False)
            train.to_csv(path + SaveFile_Name, encoding="utf_8_sig", index=False, header=None, mode='a+')
'''
train = pd.read_csv('F:/Facebook/C2/10000000_174071089663970_5594620096212369408_n', sep='\t',header=None,index_col=False)
train = np.array(train)
train_col = train[:, 9]
train_col=np.unique(train_col)

train_col=np.unique(train_col)


print(train_col.size)


mark = np.where(train_col == 1)
## a = train[mark, :].squeeze()

new_train = np.delete(train, mark,axis = 0)
np.savetxt('F:/Facebook/1.csv', new_train, fmt='%s', delimiter=',')
'''

#print(train[:, 13:14])








