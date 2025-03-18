contacts = []
while True:
    print("通讯录功能菜单:")
    print("1. 添加联系人")
    print("2. 查看所有联系人")
    print("3. 删除联系人")
    print("4. 修改联系人")
    print("5. 查找联系人")
    print("6. 退出")
    choice = input("请输入操作序号: ")
    if choice == "1":
        contact = {}
        contact["姓名"] = input("请输入姓名: ")
        contact["手机号"] = input("请输入手机号: ")
        contact["邮箱"] = input("请输入邮箱: ")
        contact["地址"] = input("请输入地址: ")
        contacts.append(contact)
        print("联系人已添加!")
    elif choice == "2":
        print("所有联系人:")
        for contact in contacts:
            print(contact)
    elif choice == "3":
        name = input("请输入要删除的联系人姓名: ")
        contacts = [c for c in contacts if c["姓名"] != name]
        print("联系人已删除")
    elif choice == "4":
        name = input("请输入要修改的联系人姓名: ")
        for contact in contacts:
            if contact["姓名"] == name:
                contact["手机号"] = input("请输入新的手机号: ")
                contact["邮箱"] = input("请输入新的邮箱: ")
                contact["地址"] = input("请输入新的地址: ")
                print("联系人信息已更新")
                break
    elif choice == "5":
        name = input("请输入要查找的联系人姓名: ")
        for contact in contacts:
            if contact["姓名"] == name:
                print("查找到的联系人:", contact)
                break
        else:
            print("未找到联系人")
    elif choice == "6":
        print("程序已退出")
        break
    else:
        print("无效输入，请重新输入")