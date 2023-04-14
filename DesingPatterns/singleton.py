"""
In this example, the Singleton class ensures that only one instance of it is created. 
The __new__ method checks if an instance already exists and if not, creates a new one, 
ensuring that there is only one instance throughout the program.
"""

class Singleton:
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # Output: True