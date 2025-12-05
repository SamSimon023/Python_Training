student={
    "name":"Sam",
    "age":22,
    "city":"Trivandrum"
}

for key in student.keys():
    print(key)
for value in student.values():
    print(value)
for key,value in student.items():
    print(key,value)

print(student["name"])
print(student["age"])

print(student.get("name"))

student["email"]="test@example.com"


student["city"]="Kochi"

print(student)

student.pop("age")      #remove by key
del student["city"]     #delete
student.clear()         #empty dictionary