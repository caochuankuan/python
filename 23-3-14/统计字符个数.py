space=0
digit=0
letters=0
str1=input("please input some str:")
for i in str1:
    if i.isalpha():
        letters+=1
    elif i.isspace():
        space+=1
    else:
        digit+=1
print("字母{}个，空格{}个，数字{}个".format(letters,space,digit))
