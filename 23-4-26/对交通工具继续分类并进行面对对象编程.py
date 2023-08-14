class vehicle(object):
    def printm(self):
        print("%s"% "能移动")

class train(vehicle):
    def printt(self):
        print("%s"% "有轨道")

class automobile(vehicle):
    def printw(self):
        print("%s"% "有轮子")

class aircraft(vehicle):
    def printf(self):
        print("%s"% "有翅膀")

class car(automobile):
    def color(self,color):
        self.color=color
    def print_color(self):
        print("颜色:",self.color)
    def printn(self):
        print("%s"% "只载人")

class truck(automobile):
    def printg(self):
        print("%s"% "可以载货物")

class aircraft_car(car,aircraft):
    def printaa(self):
        print("%s"% "可以天上飞可以地上跑")

print("\033[0;33;44m=====火车=====\033[0m")
train1=train()
train1.printm()
train1.printt()
print("\033[0;35;44m=====小车=====\033[0m")
car1=car()
car1.printm()
car1.printw()
car1.printn()
car1.color="红色"
car1.print_color()
print("\033[0;33;44m=====卡车=====\033[0m")
truck1=truck()
truck1.printg()
truck1.printm()
truck1.printw()
print("\033[0;35;44m=====飞机=====\033[0m")
aircraft1=aircraft()
aircraft1.printm()
aircraft1.printf()
print("\033[0;33;44m=====飞车=====\033[0m")
ac=aircraft_car()
ac.printf()
ac.printm()
ac.printw()
ac.printaa()
ac.color="蓝色"
ac.print_color()
ac.printn()