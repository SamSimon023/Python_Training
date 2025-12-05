#write the squares of numbers from 1 to 10 into a file ( numbers.txt ), one per
#line.

with open("numbers.txt","w") as f:
    for i in range(1,11):
        sq=i**2
        f.write(str(sq))
        f.write("\n")
f.close()

with open("numbers.txt","r")as f:
    print(f.read())
