import os
file_name="aaa.txt"
if os.path.exists(file_name):
    os.remove(file_name)
    print(file_name+"删除成功")
else:
    print(file_name+"不存在")

dir_str=os.getcwd()
my_dir="Pythonfile"
if not os.path.exists(my_dir):
    os.mkdir(my_dir)

dir_str1=os.getcwd()
my_dir1="Pythonfile"
if os.path.exists(my_dir1):
    os.rmdir(my_dir1)
    print(my_dir1+"目录删除成功")
else:
    print(my_dir1+"目录未找到")
