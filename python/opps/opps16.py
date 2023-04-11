from abc import ABC,abstractmethod

class Shape(ABC):

    @abstractmethod
    def mandatory(self):
        pass
    
    @abstractmethod
    def greet(self):
        pass
    
    def hello(self):
        print("hello")


class Circle(Shape):


    def mandatory(self):
        print("i have implemened the logic for mandatory abstract method")

    def greet(self):
        print("good morning")

    def Course(self):
        print("i am course")
# obj1=Shape()
# print(obj1)

obj2=Circle()