import pytest
import requests


# def fixture_01():
#     print("第⼀个fixture标记的⽅法")
# def test_01():
#     fixture_01()
#     print("第⼀个测试⽤例")
# @pytest.fixture
# def fixture_01():
#     print("第⼀个fixture标记的⽅法")
# def test_01(fixture_01):
#     print("第⼀个测试⽤例")
# @pytest.fixture
# def frist():
#     return "a"
#
#
# @pytest.fixture
# def order(frist):
#     return [frist]
#
#
# def test01(order):
#     order.append("b")
#     print(order)
# class Fruit:
#     def __init__(self, name):
#         self.name = name
#
#     def __eq__(self, other):
#         return self.name == other.name
#
# @pytest.fixture
# def my():
#     return Fruit("apple")
#
# @pytest.fixture
# def your(my):
#     return [my, Fruit("balana")]
#
# def test01(my, your):
#     assert my in your
class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __eq__(self, other):
        return self.name == other.name and self.color == other.color

@pytest.fixture
def my():
    return Fruit("apple","red")

@pytest.fixture
def your():
    return [Fruit("apple", "green"), Fruit("banana", "yellow")]

def test01(my, your):
    assert my in your