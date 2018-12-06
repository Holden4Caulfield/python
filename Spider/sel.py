import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://weibo.com/"
browser = webdriver.Chrome()
browser.get(url)
wait=WebDriverWait(browser,10)

# 设置浏览器需要打开的 url

name=wait.until( EC.presence_of_element_located((By.ID, "loginname")))
pw=wait.until( EC.presence_of_element_located((By.NAME, "password")))
# name=browser.find_element_by_id('loginname')
# pw=browser.find_element_by_name('password')
print('hello')
name.send_keys('18350177980')
pw.send_keys('qwer12345')
try:
    submit=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="pl_login_form"]/div/div[3]/div[6]/a')))
    #submit=browser.find_element_by_class_name('btn_32px')
    submit.click()
except:
    print('zaobudao')
print (browser.title)  # title方法可以获取当前页面的标题显示的字段
print(browser.current_url)
#time.sleep(5)
try:
    print(0)
    #winput=browser.find_element_by_xpath('//*[@id="v6_pl_content_publishertop"]/div/div[2]/textarea')
    send=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="v6_pl_content_publishertop"]/div/div[3]/div[1]/a')))
    print(2)
    winput=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="v6_pl_content_publishertop"]/div/div[2]/textarea')))
    print(1)

    winput.send_keys('hello')
    #send.click()
except:
    print('cuowu')
    pass

print(1)
browser.refresh()
for item in browser.get_cookies():
    print(item)
