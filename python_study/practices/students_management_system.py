'''
系统功能：
1、新增学生信息
2、修改学生信息
3、删除学生信息
4、查询学生信息
5、显示全部学生信息
6、退出
'''

def print_menu():
    '''打印系统功能'''
    print("="*50)
    print("学生管理系统V1.0")
    print("1、新增学生信息")
    print("2、修改学生信息")
    print("3、删除学生信息")
    print("4、查询学生信息")
    print("5、显示全部学生信息")
    print("6、退出")
    print("="*50)


def input_num():
    '''提示用户选择相应的功能，以功能序号代替'''
    while True:
        num = input("请输入功能序号：")
        if num.isdigit():
            num = int(num)
            return num
        else:
            print("只能输入数字1-6，请重新输入")

def input_message(prompt):
    '''输入学生信息，过滤空值'''
    while True:
        msg = input(prompt)
        if msg != "":
            return msg
        else:
            print("输入不能为空，请重新输入")




if __name__ == '__main__':
    students = []
    while True:
        print_menu()
        num = input_num()

        if num == 1:
            name = input_message("请输入学生姓名：")
            sex = input_message("请输入学生性别：")
            age = input_message("请输入学生年龄：")

            student = {}
            student["name"] = name
            student["sex"] = sex
            student["age"] = age
            students.append(student)
            print(student.items())
            print(students)
        elif num == 2:
            pass
        elif num == 3:
            pass
        elif num == 4:
            pass
        elif num == 5:
            print("姓名\t性别\t年龄")
            for temp in students:
                for name,sex,age in temp.items():
                    print("%s\t%s\t%s"%(name,sex,age))
        elif num == 6:
            break
        else:
            print("只能输入数字1-6，请重新输入")
