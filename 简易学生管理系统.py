students = {}

def add_student():
    student_id = input("请输入学生ID：")
    if student_id in students:
        print("该学生ID已存在！")
        return
    name = input("请输入学生姓名：")
    age = input("请输入学生年龄：")
    major = input("请输入学生专业：")
    students[student_id] = {"姓名": name, "年龄": age, "专业": major}
    print("学生信息添加成功！")

def delete_student():
    student_id = input("请输入要删除的学生ID：")
    if student_id in students:
        del students[student_id]
        print("学生信息删除成功！")
    else:
        print("未找到该学生！")

def update_student():
    student_id = input("请输入要修改的学生ID：")
    if student_id in students:
        print("当前信息：", students[student_id])
        name = input("请输入新的姓名（留空则不修改）：")
        age = input("请输入新的年龄（留空则不修改）：")
        major = input("请输入新的专业（留空则不修改）：")

        if name:
            students[student_id]["姓名"] = name
        if age:
            students[student_id]["年龄"] = age
        if major:
            students[student_id]["专业"] = major

        print("学生信息修改成功！")
    else:
        print("未找到该学生！")

def query_student():
    student_id = input("请输入要查询的学生ID：")
    if student_id in students:
        print("学生信息：", students[student_id])
    else:
        print("未找到该学生！")

def main():
    while True:
        print("\n=== 学生管理系统 ===")
        print("1. 添加学生")
        print("2. 删除学生")
        print("3. 修改学生信息")
        print("4. 查询学生信息")
        print("5. 退出系统")
        choice = input("请选择操作（1-5）：")
        if choice == "1":
            add_student()
        elif choice == "2":
            delete_student()
        elif choice == "3":
            update_student()
        elif choice == "4":
            query_student()
        elif choice == "5":
            print("退出系统，感谢使用！")
            break
        else:
            print("无效选择，请输入 1-5 之间的数字！")

main()
