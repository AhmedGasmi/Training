"""
In this example, the Component class defines the interface for objects that can have responsibilities added to them dynamically. 
The ConcreteComponent class is a concrete implementation of the Component class. 
The Decorator class is an abstract class that also implements the Component interface and has a reference to a Component object. 
The ConcreteDecoratorA and ConcreteDecoratorB classes are concrete decorators that add responsibilities to the Component object they decorate. 
In this example the decoratorB is applied to the decoratorA which is applied to the component 
and the final string printed is "ConcreteDecoratorB(ConcreteDecoratorA(ConcreteComponent))"
"""

class Component:
    def operation(self):
        pass

class ConcreteComponent(Component):
    def operation(self):
        return "ConcreteComponent"

class Decorator(Component):
    def __init__(self, component):
        self._component = component

    def operation(self):
        return self._component.operation()

class ConcreteDecoratorA(Decorator):
    def operation(self):
        return f"ConcreteDecoratorA({self._component.operation()})"

class ConcreteDecoratorB(Decorator):
    def operation(self):
        return f"ConcreteDecoratorB({self._component.operation()})"

component = ConcreteComponent()
decoratorA = ConcreteDecoratorA(component)
decoratorB = ConcreteDecoratorB(decoratorA)
print(decoratorB.operation())  # Output: ConcreteDecoratorB(ConcreteDecoratorA(ConcreteComponent))