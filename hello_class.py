class BasicMath:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def mult(self):
        return self.a * self.b

if __name__ == '__main__':
    b = BasicMath(10, 14)
    print b.add()
    print b.mult()