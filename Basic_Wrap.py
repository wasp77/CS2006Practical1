
class WrappedObject(WrappedStructure):
    def __init__(self, obj1, obj2):
        self.object1 = obj1
        self.object2 = obj2
    def __str__(self): # overwrite "print"
        return "<" + str(self.object1) + ":" + str(self.object2) + ">"
    def __add__(self,other):
        return WrappedObject(max(self.object1,other.object1), self.object2)
    def __mul__(self,other):
        return WrappedObject((self.object1 + other.object1) % self.object2, self.object2)
