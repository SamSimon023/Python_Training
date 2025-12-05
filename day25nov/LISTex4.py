strings=["apple", "banana", "cherry","fo","fe","fu"]
filtered_list = []
for s in strings:
    if len(s) >= 3:
        filtered_list.append(s)

print("Filtered list:", filtered_list)


