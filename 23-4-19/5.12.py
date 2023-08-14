class Student(object):
    def __init__(self,sno,name,score):
        self.__sno=sno
        self.__name=name
        self.__score=score
    def print_score(self):
        print("学号:%s\t,姓名:%s\t,成绩:%s\t"%(self.__sno,self.__name,self.__score))
        return "hello"
    def get_name(self):
        print(self.__name)
    def set_name(self,name):
        self.__name=name
    def get_grade(self):
        if self.__score>=90:
            return 'A'
        elif self.__score>=80:
            return 'B'
        elif self.__score>=70:
            return 'C'
        elif self.__score>=60:
            return 'D'
        else:
            return 'E'


stu1=Student(21101,"张三",66)
stu2=Student(21102,"李四",77)
stu3=Student(21103,"王五",88)
# print(stu1.print_score())
# print(stu2.print_score())
# print(stu3.print_score())
# print(stu1.get_grade())
# print(stu2.get_grade())
# print(stu3.get_grade())
# stu1.__name
stu1.get_name()
stu2.set_name("111")
stu2.get_name()
