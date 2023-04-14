"""
In this example, the Component class defines an interface for objects in a composition 
and the Composite and Leaf classes are classes that implement the Component interface. 
The Composite class is a container class that can hold other Component objects, including other Composite objects. 
The operation() method is overridden in the Composite class to perform the operation on all the children it holds. 
The Leaf class represents the leaf nodes in the composition, which do not have children.

"""


class Component:
    def operation(self):
        pass

class Composite(Component):
    def __init__(self):
        self._children = []

    def operation(self):
        results = []
        for child in self._children:
            results.append(child.operation())
        return "".join(results)

    def add(self, component):
        self._children.append(component)

    def remove(self, component):
        self._children.remove(component)

class Leaf(Component):
    def operation(self):
        return "Leaf"

composite = Composite()
leaf1 = Leaf()
leaf2 = Leaf()
composite.add(leaf1)
composite.add(leaf2)
print(composite.operation())  # Output: "LeafLeaf"
