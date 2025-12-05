#reads a text file and prints only those lines that contain the word "Python" .

with open("notes.txt","w") as f:
    f.write("This is line 1 of Python \nThen comes line 2\nThen there is a 3rd line\nWhich is followed by the second last line\nand finally the 5th and final line using Python.")

f.close()

with open("notes.txt","r") as f:
    lines=f.readlines()
    for line in lines:
        if "Python" in line:
            print(line)

f.close()
