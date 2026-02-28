import pytest
import requests
# @pytest.fixture
# #
# def operator():
#     print("qainz")
#
#     yield
#
#     print("houz")
#
# def test01(operator):
#     print(1)
# @pytest.fixture
# def operator():
#     print("qian")
#
#     yield 100
#
#     print("hou")
#
# def test01(operator):
#     print(100 + operator)
#     assert 100 == operator
@pytest.fixture
def operator():
    print("open")
    fo = open("test.txt","r",encoding="utf-8")
    yield fo
    fo.close()

@pytest.fixture
def write():
    print("write")
    fo = open("test.txt","w",encoding="utf-8")
    yield fo
    fo.close()

def test01(operator,write):
    w = write
    w.write("111")
    w.close()
    r = operator
    print(r.read(10))

