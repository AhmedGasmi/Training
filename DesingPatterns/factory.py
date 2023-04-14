"""
In this example, the get_pet() function acts as a factory that returns a Dog or Cat object based on the pet_type argument. 
The get_pet() function is decoupled from the classes, 
so new classes can be added without modifying the factory.
"""


class Dog:
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof!"

class Cat:
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow!"

def get_pet(pet_type):
    if pet_type == "dog":
        return Dog("Hope")
    elif pet_type == "cat":
        return Cat("Peace")

"""
or other way:

def get_pet(pet="dog"):
    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))
    return pets[pet]
"""

d = get_pet("dog")
print(d.speak())  # Output: Woof!

c = get_pet("cat")
print(c.speak())  # Output: Meow!
