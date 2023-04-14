"""
In this example, the Adaptee class has an existing interface (specific_request()) that is not compatible with the Target interface. 
The Adapter class is used to adapt the Adaptee interface to the Target interface by implementing the request() method in terms of 
the specific_request() method.
"""

class Adaptee:
    def specific_request(self):
        return ".eetpadA eht fo roivaheb laicepS"

class Target:
    def request(self):
        pass

class Adapter(Target):
    def __init__(self, adaptee):
        self._adaptee = adaptee

    def request(self):
        return self._adaptee.specific_request()[::-1]

adaptee = Adaptee()
adapter = Adapter(adaptee)
print(adapter.request())  # Output: "Special adapter for the Adaptee"
