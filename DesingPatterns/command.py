"""
In this example, the Command class defines an interface for executing an operation. 
The ConcreteCommand class is a concrete implementation of the Command class that holds a reference to the Receiver object and an argument. 
The execute() method calls the action() method on the Receiver object with the argument. 
The Receiver class is the object that knows how to perform the operation. 
The Invoker class holds a reference to a Command object and calls its execute() method when it wants the operation to be performed. 
This way, the Invoker class is decoupled from the Receiver class and the operation being performed.
"""



class Command:
    def execute(self):
        pass

class ConcreteCommand(Command):
    def __init__(self, receiver, arg):
        self.receiver = receiver
        self.arg = arg

    def execute(self):
        self.receiver.action(self.arg)

class Receiver:
    def action(self, arg):
        print(f"Receiver: working on({arg}).")

class Invoker:
    def __init__(self, command):
        self.command = command

    def execute(self):
        self.command.execute()

receiver = Receiver()
command = ConcreteCommand(receiver, "Hello World")
invoker = Invoker(command)
invoker.execute()  # Output: Receiver: working on(Hello World).