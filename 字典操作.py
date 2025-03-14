dict_demo = {'k1':'v1','k2':'v2','k3':'v3'}
for key in dict_demo.keys():
    print(key,end=' ')
print()
for value in dict_demo.values():
    print(value,end=' ')
print()
for key,value in dict_demo.items():
    print(f'{key}:{value}',end=' ')
print()
dict_demo['k4'] = 'v4'
dict_demo['k5'] = 'v6'
print("添加后:", dict_demo)
dict_demo["k5"] = "v5"
print("修改后:", dict_demo)
dict_demo.clear()
print("清空后:", dict_demo)
