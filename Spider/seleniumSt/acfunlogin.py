import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# opt = webdriver.ChromeOptions()
#
# # 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
# opt.set_headless()
url='https://www.acfun.cn/'
cookie_list=[]
browser=webdriver.Chrome()
browser.get('http://www.acfun.cn/')
#预处理，去掉data页
wait=WebDriverWait(browser,10)
#selenium 模拟登陆抓取cookie
login_1=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="header-guide"]/li[1]/a[2]')))
login_1.click()
print('11')
print(browser.window_handles)
browser.switch_to_window(browser.window_handles[1])
try:
    print(browser.current_window_handle)
    login_2=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="login-account-switch"]')))
    login_2.click()
except:
    print('error')
user_name=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="ipt-account-login"]')))
pass_word=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="ipt-pwd-login"]')))
user_name.send_keys('18604016946')
pass_word.send_keys('1041432518qq')
login=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="form-login"]/div[4]/div')))

login.click()
cookiess=browser.get_cookies()
print(browser.page_source[0:500])
print(browser.current_url)
browser.quit()
for item in cookiess:
    cook=item['name']+'='+item['value']
    cookie_list.append(cook)


header_cookies=';'.join(cookie_list)
print(header_cookies)
headers = {
        'Referer': 'http://www.acfun.cn/member/',
        'Cookie':header_cookies,
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
html=requests.get('http://www.acfun.cn/',headers=headers)
print(html.status_code)
html.encoding='utf-8'
print(html.text[0:500])
print(html.url)
print(html.cookies.get_dict())
