class Vehicle:
    def __init__(self):
        self._speed = 0
        self.__price = 60
    def _accelerate(self, amount):
        self._speed += amount
        return self._speed
class Car(Vehicle):
    def accelerate(self, amount):
        print(self._accelerate(amount))
        print(self._Vehicle__price)


car = Car()
car.accelerate(70)

u = []

