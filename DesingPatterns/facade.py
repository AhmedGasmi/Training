"""
In this example, the Facade class provides a simplified interface to a complex system of classes (SubsystemA and SubsystemB). 
The Facade class has a reference to the subsystem classes and delegates calls to them, hiding the complexity of the subsystems.
"""


class SubsystemA:
    def operation(self):
        return "Subsystem A"

class SubsystemB:
    def operation(self):
        return "Subsystem B"

class Facade:
    def __init__(self):
        self._subsystem_a = SubsystemA()
        self._subsystem_b = SubsystemB()

    def operation(self):
        return f"Facade({self._subsystem_a.operation()}, {self._subsystem_b.operation()})"

facade = Facade()
print(facade.operation())  # Output: "Facade(Subsystem A, Subsystem B)"
