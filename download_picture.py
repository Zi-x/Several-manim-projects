import requests
import os
import csv
import pandas as pd
import time

csv = pd.read_csv('E:\FansData.csv')

root="D://pics//"   #根目录'
print(len(csv))
for i in range(len(csv)):
    url = csv['face'][i]
    path=root+url.split('/')[-1] #根目录加上url中以反斜杠分割的最后一部分，即可以以图片原来的名字存储在本地
    print(i)
    try:
        if not os.path.exists(root):#判断当前根目录是否存在
            os.mkdir(root)          #创建根目录
        if not os.path.exists(path):#判断文件是否存在
            r=requests.get(url)
            time.sleep(0.05)
            with open(path,'wb')as f:
                f.write(r.content)
                
                print("文件保存成功")
        else:
            print("文件已存在")
    except:
        print("爬取失败")
