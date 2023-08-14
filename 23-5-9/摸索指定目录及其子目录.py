import os
cur_path=os.path.dirname(__file__)
cur_path+="/321"
sample_tree=os.walk(cur_path)
for dir_name,sub_dir,files in sample_tree:
    print("文件路径",dir_name)
    print("目录列表",sub_dir)
    print("文件列表",files)