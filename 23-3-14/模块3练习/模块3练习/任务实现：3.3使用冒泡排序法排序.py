#coding: utf-8
###############################################################################
####################               正文代码                 ####################
###############################################################################
###冒泡排序
mppx = [1,8,2,6,3,9,4,12,0,56,45]             #定义列表
for i in range(len(mppx)):
    for j in range(i+1):
        if mppx[i] < mppx[j]:
            mppx[i],mppx[j] = mppx[j],mppx[i] # 实现两个变量的互换
            
print(mppx)
#result:[0, 1, 2, 3, 4, 6, 8, 9, 12, 45, 56]
