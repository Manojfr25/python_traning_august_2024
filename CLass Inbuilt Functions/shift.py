class Number:
    def __init__(self, value):
        self.value = value

    def __lshift__(self, other):
        return Number(self.value << other)

n = Number(10)
n2 = n << 2
print(n2.value)



class Number:
    def __init__(self, value):
        self.value = value

    def __rshift__(self, other):
        return Number(self.value >> other)

r = Number(40)
r2 = r >> 2
print(r2.value)