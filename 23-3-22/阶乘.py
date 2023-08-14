def jiecheng(n):
    if n==1:
        return 1
    else:
        return  n*jiecheng(n-1)
x=int(input("请输入一个正整数:"))
print(x,"的阶乘:=",jiecheng(x))
