class Person:
    def __init__(self, age, name, origin):
        self.age = age
        self.name = name
        self.origin = origin

    def __str__(self):
        return f"Hi, my name is {self.name}. I'm {self.height} tall.\
                I'm from {self.origin} and I'm {self.age} years old."

    def get_height(self, height):
        self.height = height
        return height


person = Person(30, "Jake", "Australia")
person.get_height(6.1)


print(person)
