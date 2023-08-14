import os
dir_str=os.path.dirname(__file__)
os.system("cls")
os.system("mkdir 321")
os.system("copy a.txt 321\\aa.txt")
file_name=dir_str+"321\\aa.txt"
os.system("notepad"+file_name)