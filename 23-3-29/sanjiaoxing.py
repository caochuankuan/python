def sanjiaoxing(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        if a==b==c:
            print("此三角形是等边三角形")
        elif a==b or a==c or b==c:
            print("此三角形是等腰三角形")
        elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
            print("此三角形是直角三角形")
        else:
            print("此三角形是一般三角形")
    else:
        print("此三边不能组成三角形")
print("三角形形状判断器")
a=int(input("请输入第一边a="))
b=int(input("请输入第二边b="))
c=int(input("请输入第三边c="))
print("根据您输入的结果，得出：")
sanjiaoxing(a,b,c)
