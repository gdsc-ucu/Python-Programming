class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

mike=Dog("Mike",15)
     

print(mike.name)
print(mike.age)