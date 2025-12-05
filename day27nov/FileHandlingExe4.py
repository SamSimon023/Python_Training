#counts the number of lines in a given file.

with open("notes.txt","r") as f:
    print("Number of lines : ",len(f.readlines()))

f.close()