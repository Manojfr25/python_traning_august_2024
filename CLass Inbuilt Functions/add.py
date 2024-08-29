class Add:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Add(self.x + other.x, self.y + other.y)

A1 = Add(2, 3)
A2 = Add(4, 5)
A3 = A1 + A2
print(A3.x)
print(A3.y)
