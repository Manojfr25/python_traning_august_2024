class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def _str_(self):
        return f"{self.name} is {self.age} years old."

p = Person("Aniruddh", 20)
print(p)