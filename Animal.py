class Animal:
    name = ""
    age = 0

    def __init__(self, name = "", age = 0):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f'Name: {self.name}, Age: {self.age}'

class Dog(Animal):
    def bark(self):
        print("A dog can bark.")

class Lion(Animal):
    def roar(self):
        print("This animal can roar very loudly.")

class Fish(Animal):
    def swim(self):
        print("This animal can swim.")

class Shark(Fish):
    def devour(self):
        print("This animal belongs to the fish family. It devours objects very quickly.")

