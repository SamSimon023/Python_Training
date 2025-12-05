#reads a file and counts the number of words in it.

with open("notes.txt","r") as f:
    count=0
    line=f.read()
    list=line.split()
    print("Number of words : ",len(list))

f.close()
