class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def _repr_(self):
        return f"Person('{self.name}', {self.age})"

p = Person("Rohit", 25)
print(repr(p))