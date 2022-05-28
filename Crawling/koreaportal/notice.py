from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import csv


#1번째 일반공지사항
file = open('portalnotice.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(["title","source","date","link"])


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://portal.korea.ac.kr/front/Intro.kpd")

loginid = driver.find_element(By.NAME, "id")
password = driver.find_element(By.NAME, "pw")
loginid.send_keys("badr1108")
password.send_keys("monstax0528")
time.sleep(5)
loginbutton = driver.find_element(By.NAME, "loginsubmit").click()
time.sleep(3)
mainNoticeList = driver.find_element(By.ID, 'mainNoticeList')
notices = mainNoticeList.find_elements(By.TAG_NAME, 'li')

for notice in notices:
    title = notice.find_element(By.TAG_NAME, 'a')
    source = notice.find_element(By.CLASS_NAME,'txt_right')

    source = source.text


    info = {
            'title' : title.text,     
            'source' : source.split(' ')[0],
            'date' : source.split(' ')[-1]
            }

    info['link'] = "https://portal.korea.ac.kr/front/Intro.kpd"

    row = []   
    row.append(info['title'])
    row.append(info['source'])
    row.append(info['date'])
    row.append(info['link'])
    writer.writerow(row)

#2번째 규정예고 및 공지
file = open('portalnotice_rules.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(["title","source","date","link"])

notice_rules = driver.find_element(By.XPATH, '//*[@id="main_contents2"]/div/div[2]/div[2]/div[2]/div[1]/ul/li[2]/a').click()
time.sleep(2)
Notice_Rules = driver.find_element(By.ID, 'portlet_EM_NOTC_POS')
rule_notices = Notice_Rules.find_elements(By.TAG_NAME, 'li')

for notice in rule_notices:
    title = notice.find_element(By.TAG_NAME, 'a')
    source = notice.find_element(By.CLASS_NAME,'txt_right')

    source = source.text


    info2 = {
            'title' : title.text,     
            'source' : source.split(' ')[0],
            'date' : source.split(' ')[-1]
            }

    info2['link'] = "https://portal.korea.ac.kr/front/Intro.kpd"

    row = []   
    row.append(info2['title'])
    row.append(info2['source'])
    row.append(info2['date'])
    row.append(info2['link'])
    writer.writerow(row)


#3번째 교내외 행사

file = open('portalnotice_events.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(["title","source","date","link"])



notice_events = driver.find_element(By.XPATH, '//*[@id="main_contents2"]/div/div[2]/div[2]/div[2]/div[1]/ul/li[3]/a').click()
time.sleep(2)
Notice_Events = driver.find_element(By.ID, 'portlet_EM_NOTC_POS')
rule_notices = Notice_Rules.find_elements(By.TAG_NAME, 'li')

for notice in rule_notices:
    title = notice.find_element(By.TAG_NAME, 'a')
    source = notice.find_element(By.CLASS_NAME,'txt_right')

    source = source.text


    info3 = {
            'title' : title.text,     
            'source' : source.split(' ')[0],
            'date' : source.split(' ')[-1]
            }

    info3['link'] = "https://portal.korea.ac.kr/front/Intro.kpd"

    print(info3)
    row = []   
    row.append(info3['title'])
    row.append(info3['source'])
    row.append(info3['date'])
    row.append(info3['link'])
    writer.writerow(row)

#4번째 장학금 공지사항

file = open('portalnotice_tuition.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(["title","source","date","link"])



notice_events = driver.find_element(By.XPATH, '//*[@id="main_contents2"]/div/div[2]/div[2]/div[2]/div[1]/ul/li[4]/a').click()
time.sleep(2)
Notice_Events = driver.find_element(By.ID, 'portlet_EM_NOTC_POS')
rule_notices = Notice_Rules.find_elements(By.TAG_NAME, 'li')

for notice in rule_notices:
    title = notice.find_element(By.TAG_NAME, 'a')
    source = notice.find_element(By.CLASS_NAME,'txt_right')

    source = source.text


    info4 = {
            'title' : title.text,     
            'source' : source.split(' ')[0],
            'date' : source.split(' ')[-1]
            }

    info4['link'] = "https://portal.korea.ac.kr/front/Intro.kpd"

    print(info4)
    row = []   
    row.append(info4['title'])
    row.append(info4['source'])
    row.append(info4['date'])
    row.append(info4['link'])
    writer.writerow(row)