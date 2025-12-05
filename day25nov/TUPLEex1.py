t=(1,"hello",2,"world",3,"Go",4,"Bye")
strings=()
integers=()
for i in t:
    if type(i)==int:
        integers+=(i,)
    if type(i)==str:
        strings+=(i,)
print(integers)
print(strings)