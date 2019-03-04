def input_message(prompt):
    '''输入学生信息，过滤空值'''
    while True:
        msg = input(prompt)
        if msg == "":
            print("输入不能为空，请重新输入")
        else:
            return msg

name = input_message("请输入学生姓名：")
print(name)

class People():
    def hand(self,a,b):
        return a+b
    def add(self,a,b):
        return a+b