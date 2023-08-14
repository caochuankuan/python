print("三角形判断")
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
if a+b>c or a+c>b or b+c>a:
    if a==b==c:
        print("等边三角形")
    elif a==b or a==c or b==c:
        print("等腰三角形")
    else:
        print("其他三角形")
