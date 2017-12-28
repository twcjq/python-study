# -*- coding: UTF-8 -*-
#定义一个学生类
class Student():

    #初始化学生类
    def __init__(self,student_id,name,grade):
        self.student_id = student_id #为学生的学号赋值
        self.name = name #为学生的名字赋值
        self.grade = grade #为学生的年级赋值

    #创建“去上学”这个行为    
    def goto_school(self):
        print(self.name+"去上学了!!!!!!!!!!") #代表去上学了


if __name__ == "__main__":
    #创建xiaoMing这个对象
    xiaoHong = Student(1,"小红","三年级")
    #xiaoMing去上学
    xiaoHong.goto_school()