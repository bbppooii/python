num1 = float(input())
num2 = float(input())
operation = input()

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        result = "除数不为0"
    else:
        result = num1 / num2
else:
    result = "无效"

print(result)
