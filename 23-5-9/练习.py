file_name="aa.txt"
with open(file_name,"w") as f1:
    f1.write("我会使用python程序设计")
    f1.write("\n")
    f1.write("我来教大家学习python程序设计")
    f1.write("\n")
    f1.close()

with open("aa.txt","r") as f2:
    for line in f2.readlines():
        line_str=line.rstrip("\n")
        print(line_str)
        f2.close()