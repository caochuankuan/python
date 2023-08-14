import os
file_name="rename.txt"
file_name_new="rename.txt"
if os.path.exists(file_name):
    os.rename(file_name,file_name_new)
    print("文件重命名为："+file_name_new)
else:
    print(file_name+"文件不存在")