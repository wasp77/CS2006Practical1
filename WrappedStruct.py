


class WrappedStructure:
    def __init__(self, n):
        self.n = n
    def __str__(self):
        return "<" + str(list(range(self.n))) + ">"
    def Size(self):
        return self.n

a = WrappedStructure(10)
print(a)
