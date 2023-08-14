list=["苹果","葡萄","香蕉","西瓜"]
f1=open("shuiguo.csv","w")
f1.write(",".join(list)+"\n")
f1.close()

f2=open("shuiguo.csv","r")
txt=f2.read()
list1=txt.strip("\n").split(",")
print(txt)
print(list1)
f2.close()