def xunhuang(n):
    sum1=0
    for i in range(n+1):
        sum1+=i
    return sum1
x=int(input("请输入一个正整数:"))
print("1加到",x,"等于：",xunhuang(x))

# 偶数
def xunhuang1(n):
    sum1=0
    for i in range(0,n+1,2):
        sum1+=i
    return sum1
x=int(input("请输入一个正整数:"))
print("1加到",x,"(偶数)等于：",xunhuang1(x))