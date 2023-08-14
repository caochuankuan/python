def digui(n):
    if n<0:
        return 0
    else:
        return  n+digui(n-1)
x=int(input("请输入一个正整数:"))
print("1加到",x,"等于：",digui(x))
