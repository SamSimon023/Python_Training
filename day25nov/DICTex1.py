x={"A": 85, "B": 88, "C": 98, "D": 82}
m = 0
c=""
for i,j in x.items():
    if j > m:
        m = j
        c=i
print(c)