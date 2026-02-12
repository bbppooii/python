import requests
# r = requests.get('https://www.baidu.com')
# #状态码
# print(r.status_code)
# #响应头
# print(r.headers)
# #响应体
# print(r.text)
# # print(r.json())
# get = requests.get('https://www.baidu.com')
# post =requests.post('https://www.baidu.com')
# req_get = requests.request('GET','https://www.baidu.com')
# req_post = requests.request('POST','https://www.baidu.com')
# req_random = requests.request(url='https://www.baidu.com',method='POST')
# print(get)
# print(post)
# print(req_get)
# print(req_post)
# print(req_random)
# url = 'http://8.137.19.140:9090/blog/getBlogDetail?blogId=158477'
# url = 'http://8.137.19.140:9090/blog/getBlogDetail'
# param = {
#     'blogId' : 158477
# }
# header = {
#     'user_token_header' : "eyJhbGciOiJIUzI1NiJ9.eyJpZCI6MiwidXNlck5hbWUiOiJsaXNpIiwiZXhwIjoxNzU4NDY4NzI2fQ.YfAnKaLyQbX1yjtr3sXraH6GKDd0KBU2ulZoysmNMe4"
# }
# r = requests.request(method='GET',url=url,headers=header,params=param)
# print(r.json())
# url = 'http://8.137.19.140:9090/user/login'
# date = {
#     'username':'zhangsan',
#     'password':'123456'
# }
# r = requests.request(url=url,data=date,method='post')
# print(r.json())
# def chu(a, b):
#     assert b != 0, "除数不能为0"
#     return a / b
#
# def test02_03():
#     print("开始测试除法函数")
#     print("调用chu(4,1):", chu(4,1))  # 正常情况
#     print("调用chu(4,0):", end=' ')
#     try:
#         print(chu(4,0))  # 应该触发断言
#     except AssertionError as e:
#         print(f"捕获到AssertionError: {e}")
#     except Exception as e:
#         print(f"捕获到其他异常: {type(e).__name__}: {e}")
#     else:
#         print("没有异常发生")
#
# if __name__ == '__main__':
#     test02_03()
#     print("\n断言检查:")
#     try:
#         assert False, "测试断言是否工作"
#     except AssertionError as e:
#         print(f"断言正常工作: {e}")
#     else:
#         print("断言被禁用!")