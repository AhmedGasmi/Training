"""
In this example, the Abstraction class defines an interface for the Implementation class and has a reference to an object of the Implementation class. 
The Implementation class defines an interface for the operations that can be implemented. 
The ConcreteImplementationA and ConcreteImplementationB classes are concrete implementations of the Implementation class. 
By separating the interface from the implementation, the Abstraction class can work with any implementation of the Implementation class, 
making it more flexible and allowing for easy changes to the implementation without affecting the Abstraction.
"""

class Abstraction:
    def __init__(self, implementation):
        self._implementation = implementation

    def operation(self):
        return f"Abstraction({self._implementation.operation_implementation()})"

class Implementation:
    def operation_implementation(self):
        pass

class ConcreteImplementationA(Implementation):
    def operation_implementation(self):
        return "ConcreteImplementationA"

class ConcreteImplementationB(Implementation):
    def operation_implementation(self):
        return "ConcreteImplementationB"

abstraction = Abstraction(ConcreteImplementationA())
print(abstraction.operation())  # Output: "Abstraction(ConcreteImplementationA)"
abstraction = Abstraction(ConcreteImplementationB())
print(abstraction.operation())  # Output: "Abstraction(ConcreteImplementationB)"
