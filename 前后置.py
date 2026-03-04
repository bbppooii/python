# class Test01:
#     def test_01(self):
#         print("test_01")
#         a = 1
#         b = 1
#         assert a == b
#         str1 = "bbb"
#         str2 = "bbb"
#         assert str1 == str2
#         expect_list01 = ["01","aaa","02"]
#         expect_list02 = ["01","bbb","01"]
#         assert expect_list01 == expect_list02
import requests


def test_01():
    # url = '	https://jsonplaceholder.typicode.com/posts/1'
    # r = requests.request(method='get',url=url)
    # expect = {
    #   "userId": 1,
    #   "id": 1,
    #   "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    #   "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    # }
    # actual = (r.json())
    # assert expect == actual
    # url = 'https://jsonplaceholder.typicode.com/posts/1/comments'
    # r = requests.request(method='get', url=url)
    # assert r.json()[0]["id"] == 1
    url = 'https://jsonplaceholder.typicode.com/'
    r = requests.request(method='get', url=url)
    text = 'Use your own data'
    assert text in r.text