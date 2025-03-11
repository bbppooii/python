import datetime
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager
options = webdriver.EdgeOptions()
options.page_load_strategy = 'eager'
options.add_argument('-headless')
edgeins = EdgeChromiumDriverManager().install()
driver = webdriver.Edge(service=Service(edgeins),options=options)
# driver.get("https://www.bilibili.com/")
# driver.find_element(By.XPATH,'//*[@id="nav-searchform"]/div[1]/input').send_keys('1')
# time.sleep(3)
# a = driver.find_element(By.XPATH,'//*[@id="nav-searchform"]/div[1]/input')
# driver.execute_script("arguments[0].value = '';", a)
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR,'#nav-searchform > div.nav-search-content > input').send_keys('青雀0金0t')
# time.sleep(2)
# text = driver.find_element(By.XPATH,'//*[@id="nav-searchform"]/div[1]/input').text
# print(text)
# driver.find_element(By.CSS_SELECTOR,'#nav-searchform > div.nav-search-btn > svg').click()
# time.sleep(2)
# print(driver.title)
# print(driver.current_url)
# curwindow = driver.current_window_handle
# allwindows = driver.window_handles
# for window in allwindows:
#     if window != curwindow:
#         driver.switch_to.window(window)
# driver.close()
# filename = 'autotest' + datetime.datetime.now().strftime('%Y-%m-%d-%H%M%S')+'.png'
# driver.save_screenshot('C:/Users/31173/Desktop/python/images/' + filename)
# time.sleep(1)
# driver.maximize_window()
# time.sleep(1)
# driver.minimize_window()
# time.sleep(1)
# driver.fullscreen_window()
# time.sleep(1)
# driver.set_window_size(1024,500)
# time.sleep(1)
#driver.implicitly_wait(3)
# driver.switch_to.alert.accept()
# driver.find_element(By.XPATH,'//*[@id="nav-searchform"]/div[1]/input').send_keys('1')
# a = driver.find_element(By.XPATH,'//*[@id="nav-searchform"]/div[1]/input')
# driver.execute_script("arguments[0].value = '';", a)
# wait = WebDriverWait(driver,2)
# wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#nav-searchform > div.nav-search-content > input')))
# driver.find_element(By.CSS_SELECTOR,'#nav-searchform > div.nav-search-content > input').send_keys('青雀0金0t')
# driver.find_element(By.CSS_SELECTOR,'#nav-searchform > div.nav-search-btn > svg').click()
driver.get('https://legacy.cplusplus.com/')
wait = WebDriverWait(driver,2)
a = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#I_nav > div.sect.root > ul > li.folder.doc > a')))
a.click()
time.sleep(1)
driver.back()
time.sleep(1)
driver.forward()
time.sleep(1)
driver.refresh()
print(driver.title)
time.sleep(1)
driver.quit()