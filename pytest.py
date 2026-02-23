import pytest


# @pytest.mark.parametrize("data", (1, 2, 3))
# def test01(data):
#     print(data)
# # @pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6),("6*9", 42)])
# # def test_eval(test_input, expected):
# #     assert eval(test_input) == expected
#
# @pytest.mark.parametrize("n,expected", [(1, 2), (3, 4)])
# class TestClass:
#     def test_simple_case(self, n, expected):
#         assert n + 1 == expected
#     def test_weird_simple_case(self, n, expected):
#         assert (n * 1) + 1 == expected

# pytestmark = pytest.mark.parametrize("n,expected", [(1, 2), (3, 4)])
# class TestClass:
#     def test_simple_case(self, n, expected):
#         assert n + 1 == expected
#     def test_weird_simple_case(self, n, expected):
#         assert (n * 1) + 1 == expected
def data():
    return ["1", "2", "3"]

@pytest.mark.parametrize("data", data())
def test(data):
    print(data)
