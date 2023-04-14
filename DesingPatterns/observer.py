"""
In this example, the Subject class maintains a list of observers and notifies them when its state changes. 
The Observer class defines an update() method that is called by the subject. 
In this example, a ConcreteObserver class that inherits from the observer class and overrides the update method to print "Received update."
"""

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()

class Observer:
    def update(self):
        pass

class ConcreteObserver(Observer):
    def update(self):
        print("Received update.")

subject = Subject()
concrete_observer = ConcreteObserver()
subject.attach(concrete_observer)
subject.notify()  # Output: Received update.