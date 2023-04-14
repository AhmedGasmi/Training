"""
In this example, the Subject class defines an interface for the RealSubject and Proxy classes. 
The RealSubject class is the class that does the actual work, 
while the Proxy class controls access to the RealSubject class and can add additional functionality. 
In this example, the Proxy class simply forwards the request to the RealSubject. 
But in other cases, the proxy can add some functionality or control the access to the RealSubject like adding some security checks 
before forwarding the request.

These are some of the most widely used design patterns in software development, 
and understanding how and when to use them can help you write more maintainable and flexible code.
"""

class Subject:
    def request(self):
        pass

class RealSubject(Subject):
    def request(self):
        return "RealSubject"

class Proxy(Subject):
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        return self._real_subject.request()

real_subject = RealSubject()
proxy = Proxy(real_subject)
print(proxy.request())  # Output: "RealSubject"
