list =[["fruit","price","num","total"],["apple","30","1.5","45"],["banana","10","3","30"]]
f3_name="shuiguoqingdan.csv"
f3=open(f3_name,"w")
for row in list:
    f3.write(",".join(row)+"\n")
print("数据写入",f3_name,"成功。")
f3.close()

f4_name="shuiguoqingdan.csv"
f4=open(f4_name,"r")
list=[]
for line in f4:
    list.append(line.strip("\n").split(","))
f4.close()
print(list)