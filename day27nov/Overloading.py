'''static polymorphism'''

class MathOps:
    def add(self,a,b=0,c=0):
        return a+b+c

m=MathOps()
print(m.add(5))
print(m.add(5,10))
print(m.add(5,10,20))


#another method
'''dynamic polymorphism'''

class MathOps:
    def add(self, *args):
        return sum(args)

m=MathOps()
print(m.add(2))
print(m.add(2,3))
print(m.add(2,3,4))