import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.edge.service import Service
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
#
# # 启动浏览器
# options = webdriver.EdgeOptions()
# options.page_load_strategy = 'eager'
# # options.add_argument('-headless')
# edgeins = EdgeChromiumDriverManager().install()
# driver = webdriver.Edge(service=Service(edgeins),options=options)
# driver.get('http://8.137.19.140:9090/blog_login.html')
# driver.find_element(By.CSS_SELECTOR,'#username').send_keys('lisi')
# driver.find_element(By.CSS_SELECTOR,'#password').send_keys('123456')
# driver.find_element(By.CSS_SELECTOR,'#submit').click()
#
# # 访问目标网页
# driver.get("http://8.137.19.140:9090/blog_list.html")
#
# # 等待加载
# time.sleep(3)
#
# # 获取 `div.right` 初始的内容数量
# previous_count = 0
#
# while True:
#     # 获取当前 `div.right` 里加载的内容数量
#     elements = driver.find_elements(By.CSS_SELECTOR, "body > div.container > div.right > *")
#     current_count = len(elements)
#
#     # 如果内容数量不再增加，则停止滚动
#     if current_count == previous_count:
#         break
#
#     previous_count = current_count  # 更新计数
#
#     # 向下滚动一屏，触发加载
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(2)  # 等待新内容加载
#
# print(f"总共有 {current_count} 页（或内容块）")
#
# # 关闭浏览器
# driver.quit()
