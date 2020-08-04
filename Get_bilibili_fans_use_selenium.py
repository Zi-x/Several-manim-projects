from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import time
import json
import pandas as pd
import math
options = webdriver.ChromeOptions()
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36')
driver = webdriver.Chrome(options=options)
driver.get("https://member.bilibili.com/x/h5/data/fan/list?ps=500")
cookies = {}    # 'name':'value',......
for (k, v) in cookies.items():
    driver.add_cookie({'name': k, 'value': v})
link_first = "https://member.bilibili.com/x/h5/data/fan/list?ps=500"
number = 4982 #粉丝数

def get_data(link):    
    driver.get(link)
    time.sleep(0.5)
    html =  driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    ss = soup.select('pre')[0]
    res = json.loads(ss.text)
    return (res)

def save_data(mid,name, sex,motto,face,mtime):
    data = pd.DataFrame()
    data['uid'] = uid 
    data['name'] = name 
    data['sex'] = sex 
    data['motto'] = motto
    data['face'] =face
    data['mtime'] = mtime
    data.to_excel('FansData.xlsx') 

if __name__ == "__main__":
    flag = False
    uid = [];name = [];sex = [];mtime = [];motto=[];face=[]  
    for n in range(math.ceil(number/500)): 
            link = link_first
            if flag == True:
                link = link + "&last_id=" + LastMID
            while True: #判断网页是否成功加载数据
                res = get_data(link)
                if ('data' in res):
                    break
                else:
                    continue
            for i in res['data']['result']:
                uid.append(i['card']['mid'])
                name.append(i['card']['name'])
                sex.append(i['card']['sex'])
                motto.append(i['card']['sign'])
                face.append(i['card']['face'])
                mtime.append(i['mtime'])       
            print(res['data']['result'][-1]['card']['name'],res['data']['result'][-1]['card']['sex'],res['data']['result'][-1]['mtime'])
            flag = True
            LastMID = res['data']['result'][-1]['mtime_id']
            save_data(uid, name, sex,motto,face, mtime)
