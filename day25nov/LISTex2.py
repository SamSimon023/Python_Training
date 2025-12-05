list=[1, 2, 3, 2, 4, 1, 5, 1]
duplicate=[]
for i in list:
    for j in list:
        if i not in duplicate and list.count(i)>1:
            duplicate.append(i)
print(duplicate)