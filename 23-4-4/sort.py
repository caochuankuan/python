from pypinyin import pinyin

list1 = [1, 4, 7, 4, 8, 66, 88, -77]
print(sorted(list1))
print(sorted(list1, key=abs))
print(sorted(list1, key=abs, reverse=True))

a = ["曹传宽", "于逸风", "张三", "李四", "王五"]
print(sorted(a, key=pinyin))
