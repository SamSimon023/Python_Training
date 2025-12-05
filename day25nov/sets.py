#sets
'''
nums{10,20,30,40,}

#sets dont allow duplicates
data={1,2,2,3,3,3}
print(data)

#how to create a set
s2={10,20,30}
empty=set{} #create empty set

#add operations
s={1,2,3}
s.add(4)
print(s)
s.update([5,6])
print(s)

#remove operations
s.remove(3) #raises error if not found
print(s)
s.discard(10) #does nothing if not found
print(s)

a={1,2,3}
b={3,4,5}
print(a|b) #{1,2,3,4,5}

#intersection
print(a&b) #{3}

#difference
print(a-b) #{1,2}

#symmetric difference
print(a^b) #{1,2,4,5}'''

s={10,20,30}
print(20 in s) #True

for item in{4,8,12}:
    print(item)

nums=[1,2,2,3,3,3]
unique=list(set(nums))

print(unique)