class 账户:
    def __init__(self, 账户名):
        self.账户名 = 账户名
        self.余额 = 0
        self.锁定 = False

    def 存款(self, 金额):
        self.余额 += 金额
        print(f"{self.账户名} 存款 {金额}，当前余额：{self.余额}")

    def 取款(self, 金额):
        if self.锁定:
            print("账户已锁定，无法取款")
        elif 金额 > self.余额:
            print("余额不足")
        else:
            self.余额 -= 金额
            print(f"{self.账户名} 取款 {金额}，当前余额：{self.余额}")

    def 转账(self, 目标账户, 金额):
        if self.锁定:
            print("账户已锁定，无法转账")
        elif 金额 > self.余额:
            print("余额不足")
        else:
            self.余额 -= 金额
            目标账户.余额 += 金额
            print(f"{self.账户名} 向 {目标账户.账户名} 转账 {金额}，当前余额：{self.余额}")

    def 锁定账户(self):
        self.锁定 = True
        print(f"账户 {self.账户名} 已锁定")

    def 解锁账户(self):
        self.锁定 = False
        print(f"账户 {self.账户名} 已解锁")

    def 查询(self):
        状态 = "锁定" if self.锁定 else "正常"
        print(f"账户: {self.账户名}, 余额: {self.余额}, 状态: {状态}")


银行系统 = {}

while True:
    选择 = input("\n1. 开户 2. 查询 3. 存款 4. 取款 5. 转账 6. 锁定 7. 解锁 8. 退出\n请选择操作：")

    if 选择 == "1":
        账户名 = input("请输入开户名：")
        银行系统[账户名] = 账户(账户名)
        print(f"账户 {账户名} 开户成功")

    elif 选择 == "2":
        账户名 = input("请输入账户名：")
        if 账户名 in 银行系统:
            银行系统[账户名].查询()
        else:
            print("账户不存在")

    elif 选择 == "3":
        账户名 = input("请输入账户名：")
        金额 = int(input("存款金额："))
        if 账户名 in 银行系统:
            银行系统[账户名].存款(金额)
        else:
            print("账户不存在")

    elif 选择 == "4":
        账户名 = input("请输入账户名：")
        金额 = int(input("取款金额："))
        if 账户名 in 银行系统:
            银行系统[账户名].取款(金额)
        else:
            print("账户不存在")

    elif 选择 == "5":
        转出账户 = input("请输入转出账户名：")
        转入账户 = input("请输入转入账户名：")
        金额 = int(input("转账金额："))
        if 转出账户 in 银行系统 and 转入账户 in 银行系统:
            银行系统[转出账户].转账(银行系统[转入账户], 金额)
        else:
            print("账户不存在")

    elif 选择 == "6":
        账户名 = input("请输入要锁定的账户名：")
        if 账户名 in 银行系统:
            银行系统[账户名].锁定账户()
        else:
            print("账户不存在")

    elif 选择 == "7":
        账户名 = input("请输入要解锁的账户名：")
        if 账户名 in 银行系统:
            银行系统[账户名].解锁账户()
        else:
            print("账户不存在")

    elif 选择 == "8":
        print("退出银行管理系统")
        break

    else:
        print("无效输入")
