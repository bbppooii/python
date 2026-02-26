import pytest
import requests
# @pytest.fixture(scope="function")
# def din():
#     print("qian")
#     yield
#     print("hou")
# class Test01:
#     def test01(self,din):
#         print(1)
#     def test02(self,din):
#         print(2)
# @pytest.fixture(scope="class")
# def din():
#     print("qian")
#     yield
#     print("hou")
# class Test01:
#     def test01(self,din):
#         print(1)
#     def test02(self,din):
#         print(2)
# class Test02:
#     def test01(self,din):
#         print(1)
#     def test02(self,din):
#         print(2)
# @pytest.fixture(scope="module")
# def din():
#     print("qian")
#     yield
#     print("hou")
# class Test01:
#     def test01(self,din):
#         print(1)
#     def test02(self,din):
#         print(2)
# class Test01:
#     def test01(self,din):
#         print(1)
#     def test02(self,din):
#         print(2)
# class Test01:
#     def test01(self):
#         print(1)
#     def test02(self):
#         print(2)
# @pytest.mark.parametrize("data",[1,2,3])
# def test01(data):
#     print(data)
# def para():
#     return [1,2,3]
# @pytest.mark.parametrize("data",para())
# def test01(data):
#     print(data)
@pytest.fixture(params=[1,2,3])
def data(request):
    return request.param
def test01(data):
    print(data)