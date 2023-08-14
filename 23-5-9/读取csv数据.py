# csv.reader函数
import csv
file_name ="shuiguo.csv"
with open(file_name, 'r') as f:
    reader = csv.reader(f)
    # 链式编程 等价于
    # for wordfreq_item in reader:
    #     wordfreq = [wordfreq_item]
    wordfreq = [wordfreq_item for wordfreq_item in reader]
    print(wordfreq)
