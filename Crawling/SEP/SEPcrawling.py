from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import csv

file = open('SEP_notice.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(["title","source","date","link"])


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://studyabroad.korea.ac.kr/studyabroad/index.do")
time.sleep(5)

#menubutton = driver.find_element(By.XPATH, '//*[@id="wrap"]/header/nav/a').click()
#time.sleep(5)

noticebutton = driver.find_element(By.XPATH, '//*[@id="wrap"]/header/nav/div/ul/li[5]/a').click()
time.sleep(5)
noticebutton2 = driver.find_element(By.XPATH, '//*[@id="wrap"]/header/nav/div/ul/li[5]/ul/li[1]/a').click()
time.sleep(3)

loginid = driver.find_element(By.NAME, "member_id")
password = driver.find_element(By.NAME, "member_pw")
loginid.send_keys("badr1108")
password.send_keys("monstax0528")
time.sleep(3)
loginbutton = driver.find_element(By.CLASS_NAME, "btn_login").click()
time.sleep(3)

NoticeList = driver.find_element(By.CLASS_NAME, 't_list')
notices = NoticeList.find_elements(By.TAG_NAME, 'tr')
notices = notices[1:]
for notice in notices:
    title = notice.find_element(By.CLASS_NAME,'txt_left')
    source = notice.find_element(By.XPATH,'//*[@id="jwxe_main_content"]/div/div/div/div[2]/table/tbody/tr/td[3]')
    date = notice.find_element(By.XPATH, '//*[@id="jwxe_main_content"]/div/div/div/div[2]/table/tbody/tr/td[5]')

    info = {
            'title' : title.text,     
            'source' : source.text,
            'date' : date.text
            }

    info['link'] = "https://portal.korea.ac.kr/front/Intro.kpd"

    row = []   
    row.append(info['title'])
    row.append(info['source'])
    row.append(info['date'])
    row.append(info['link'])
    writer.writerow(row)

