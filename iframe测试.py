from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

options = webdriver.EdgeOptions()
options.page_load_strategy = 'eager'
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()),options=options)
driver.get("https://example.com")

# 等待 iframe 加载，并切换
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "myIframe")))

# 在 iframe 内部查找元素并点击
element = driver.find_element(By.ID, "insideElement")
element.click()

# 切回主页面
driver.switch_to.default_content()
