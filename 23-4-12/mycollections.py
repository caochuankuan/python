from collections import Counter
ct=Counter()
for le in "hello world":
    ct[le]+=1
print(ct)