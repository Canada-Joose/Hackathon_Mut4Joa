from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import csv

 
file = open('business.csv', mode='w', newline='', encoding='UTF-8')
writer = csv.writer(file)
writer.writerow(["title","source","date","link"])

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://biz.korea.ac.kr/undergraduate/notice.html")

NoticeList = driver.find_element(By.CLASS_NAME, 'type_line')
notices = NoticeList.find_elements(By.CLASS_NAME, 'cont')
for notice in notices:

    title = notice.find_element(By.CLASS_NAME,'tit')
    date = notice.find_element(By.CLASS_NAME,'date')

    info = {
            'title' : title.text,
            'date' : date.text
            }       
    info['link'] = "https://portal.korea.ac.kr/front/Intro.kpd"
    info['source'] = "경영학과"

    row = []   
    row.append(info['title'])
    row.append(info['date'])
    row.append(info['link'])
    row.append(info['source'])
    writer.writerow(row)