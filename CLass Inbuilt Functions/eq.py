class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def _eq_(self, other):
        return self.name == other.name and self.age == other.age

p1 = Person("Tejas", 19)
p2 = Person("Tejas", 19)
print(p1 == p2)
