words = ["hello","python","world"]

unique_char = set()

for i in words:
    for j in i:
        unique_char.add(j)
print(unique_char)