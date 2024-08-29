class Prod:
    def _init_(self, x, y):
        self.x = x
        self.y = y

    def _mul_(self, other):
        return Prod(self.x * other, self.y * other)

P = Prod(2, 3)
P2 = P * 2
print(P2.x)
print(P2.y)