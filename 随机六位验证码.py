import random
import string



chars_list = []
for _ in range(6):
    chars_list.append(random.choice(string.ascii_letters + string.digits))
a = ''.join(chars_list)
print("生成的验证码：", a)
