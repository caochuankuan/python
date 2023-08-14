def lsbj():
    i=int(input("please input a num range between in 0-10:"))
    if 0<=i<5:
        print(i)
    elif 5<=i<8:
        print(i)
    elif 8<=i<10:
        print(i)
    else:
        print("error,please input again:")
        lsbj()
lsbj()
