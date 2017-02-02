class SimpleWrap:
    def __init__(self, obj1, obj2):
        self.object1 = obj1
        self.object2 = obj2
    def __str__(self): # overwrite "print"
        return "<" + str(self.object1) + ":" + str(self.object2) + ">"
    def __add__(self,other):
        return SimpleWrap(max(self.object1,other.object1), self.object2)
    def __mul__(self,other):
        return SimpleWrap((self.object1 + other.object1) % self.object2, self.object2)

a = SimpleWrap(2,5)
print(a)
b = SimpleWrap(4,5)
print(b)
print(a+b)
print(a*b)
