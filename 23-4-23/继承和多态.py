class Student(object):
    def speak(self):
        print("ababababababababababababababa")
class Daxuesheng(Student):
    def speak(self):
        print("I am daxuesheng")
    def func1(self):
        print("666")
class Zhongxuesheng(Student):
    def speak(self):
        print("I am zhongxuesheng")

def speak_twice(s):
    s.speak()
    s.speak()

s1=Student()
s1.speak()
s2=Daxuesheng()
s2.speak()
s2.func1()
s3=Zhongxuesheng()
s3.speak()
print("========")
speak_twice(Student())
speak_twice(Daxuesheng())

a=list()
b=Student()
c=Daxuesheng()
print(isinstance(a,list))
print(isinstance(b,list))
print(isinstance(b,Student))
print(isinstance(c,Daxuesheng))