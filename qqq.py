a, b = 1, 2
print(a, b)
print(type(a))
a = float(input("请输入第一个数: "))
b = float(input("请输入第二个数: "))
operator = input("请输入运算符 (+, -, *, /): ")
if operator == "+":
    print("结果:", a + b)
elif operator == "-":
    print("结果:", a - b)
elif operator == "*":
    print("结果:", a * b)
elif operator == "/":
    if b != 0:
        print("结果:", a / b)
    else:
        print("除数不能为 0")
else:
    print("无效的运算符")
s = 'qweaasd'
print(s[:3])
s1 = "hello"
s2 = " world"
print(s1 + s2)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in a[2:8]:
    print(i)
a[3] = 0
a.append(10)
print(a)
a.pop(5)
print(a)
b = [1, 2, 3, 4, 5]
print(a == b)
z = {1: "apple", 2: "banana"}
z[1] = "orange"
print(z[1])
x = {1, 2, 3, 4, 5}
print(3 in x)
print(10 in x)
