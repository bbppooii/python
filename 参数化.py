import pytest
import requests
# def test02_01():
#     print('test01')
#
# def test02_02():
#     print('test02')
#     a = 1
#     b = 2
#     # assert a == b
#     c = 'qwe'
#     d = 'qwa'
#     # assert c == d
#     #断言列表
#     expect_list = [1,'asd',2.56]
#     actual_list = [1,'asd',2.56]
#     assert expect_list == actual_list
#     #断言元组
#     except_tuple = (1,'qwe',1.23)
#     actual_tuple = (1,'qwe',1.23)
#     assert except_tuple == actual_tuple
# def chu(a,b):
#     assert b != 0, "除数不能为0"
#     return a/b
# def test02_03():
#     print(chu(4,0))
# def test():
#     url = "http://jsonplaceholder.typicode.com/posts/1"
#     r = requests.get(url=url)
#     print(r.json())
#     except_data = {
#       "userId": 1,
#       "id": 1,
#       "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
#       "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
#     }
#     actual_data = r.json()
#     assert except_data == actual_data
#
# def test02_04():
#     url = "https://jsonplaceholder.typicode.com/posts"
#     r = requests.get(url=url)
#     print(r.json()[0]['id'])
#     assert r.json()[0]['id'] == 2
# def test02_05():
#     url='https://jsonplaceholder.typicode.com/'
#     r = requests.get(url=url)
#     text = ' and a simple GitHub repo, you can have your own fake online REST server in seconds.'
#     assert text in r.text
#     # print(r.text)\
# pytestmark = pytest.mark.parametrize("data",(1,2))
# #同类型
# @pytest.mark.parametrize("data",(1,2,3))
# def test01(data):
#     print(data)
# #不同类
# @pytest.mark.parametrize("data",(1,2,'data',54.21))
# def test02(data):
#     print(data)
# @pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6),("6*9", 42)])
# def test(test_input, expected):
#     assert eval(test_input) == expected
# def data_provider():
#     return ["a", "b"]
# # 定义⼀个测试函数，它依赖于上⾯函数的返回值
# @pytest.mark.parametrize("data", data_provider())
# def test_data(data):
#     assert data != None
#     print(f"Testing with data provider: {data}")
# @pytest.fixture()
# def fixture01():
#     print("fixture")
#
# def test(fixture01):
#     print(1)
# @pytest.fixture
# def first():
#     print(1)
# @pytest.fixture
# def second(first):
#     print(2)
# def test(second):
#     print(3)
# @pytest.fixture
# def first():
#     return 'a'
# @pytest.fixture
# def second(first):
#     return [first]
# def test(second):
#     second.append('b')
#     print(second)
# class Fruit:
#     def __init__(self, name):
#         self.name = name
#     def __eq__(self, other):
#         return self.name == other.name
# @pytest.fixture
# def my_fruit():
#     return Fruit("apple")
# @pytest.fixture
# def fruit_basket(my_fruit):
#     return [Fruit("banana"), my_fruit]
# def test_my_fruit_in_basket(my_fruit, fruit_basket):
#     assert my_fruit in fruit_basket
# @pytest.fixture
# def operator():
#     print(1)
#     yield [54]
#     print(2)
# def test(operator):
#     operator.append(44)
#     print(operator)
# @pytest.fixture
# def read():
#     print("打开")
#     fo = open("test.txt","r",encoding='utf-8')
#     yield fo
#     print("关闭")
#     fo.close()
#
# @pytest.fixture
# def write():
#     print("打开")
#     fo = open("test.txt","w",encoding='utf-8')
#     yield fo
#     print("关闭")
#     fo.close()
#
# def test(read,write):
#     write.write("不好 ")
#     write.close()
#     print(read.read())
