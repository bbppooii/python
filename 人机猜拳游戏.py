import random

class 猜拳游戏:
    def __init__(self):
        self.选项 = ["石头", "剪刀", "布"]

    def 开始(self):
        while True:
            电脑出拳 = random.choice(self.选项)
            玩家出拳 = input("请输入 石头、剪刀 或 布（输入 '退出' 结束游戏）：")

            if 玩家出拳 == "退出":
                print("游戏结束")
                break

            if 玩家出拳 not in self.选项:
                print("无效输入，请重新输入")
                continue

            print(f"电脑出拳：{电脑出拳}")

            if 玩家出拳 == 电脑出拳:
                print("平局")
            elif (玩家出拳 == "石头" and 电脑出拳 == "剪刀") or \
                 (玩家出拳 == "剪刀" and 电脑出拳 == "布") or \
                 (玩家出拳 == "布" and 电脑出拳 == "石头"):
                print("你赢了！")
            else:
                print("你输了！")

游戏 = 猜拳游戏()
游戏.开始()
