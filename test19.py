# 19、 定义一个学生类，实例属性有name(姓名)，age（年龄），提示用户分别输入3个学生信息（姓名以及年龄），
# 根据用户输入的信息创建3个学生对象，将这3个学生对象存入列表，遍历列表删除年龄小于18岁的学生对象，
# 最后输出列表中剩余的学生信息
# 示例如下：
class Student(object):
    list = []
    def __init__(self):
        self.name = input("请输入学生姓名：")
        self.age = int(input("请输入学生年龄："))

        self.dict = {}
    def add_student(self):

        self.dict["姓名"] = self.name
        self.dict["年龄"] = self.age
        Student.list.append(self.dict)

    def remove_18(self):
        for index,i in enumerate(Student.list):
            if i["年龄"] < 18:
                del Student.list[index]

    def show_info(self):
       for self.dict in Student.list:


           self.remove_18()
       print(Student.list)




xiaohong = Student()
xiaohong.add_student()
xiaohong.show_info()
xiaowang = Student()
xiaowang.add_student()

xiaowang.show_info()

xiaoli = Student()
xiaoli.add_student()
xiaoli.show_info()
xiaowang.remove_18()
xiaohong.remove_18()
xiaoli.remove_18()










