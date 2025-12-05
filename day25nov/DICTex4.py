items = {"apple": 50, "orange": 80, "mango": 150}


items = {k: v for k, v in items.items() if v >= 100}

print(items)