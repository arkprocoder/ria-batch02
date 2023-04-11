# property,inspect,setter and deleter
import inspect

class Person:
    def __init__(self,fname,lname):
        print("create constructor")
        self.fname=fname
        print("set fname")
        self.lname=lname
        print("set lname")
        self.email=f"{self.fname}.{self.lname}@infosys.com"
        print("email is set")
    

    def printDetails(self):
        return f"The person first name & last name is {self.fname} {self.lname} "


    @property
    def email(self):
        if self.fname==None and self.lname==None:
            print("Email is not set please use setters to set the email")
        
        print("i am passing email")
        return f"{self.fname}.{self.lname}@gmail.com"
    

    @email.setter
    def email(self,email):
        #anees.rehman@infosys.com
        print("setting the property for this email :",email) 
        fullname=email.split("@")[0]
        self.fname=fullname.split(".")[0]
        self.lname=fullname.split(".")[1]
        print("email is set")

    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None
        print("email is deleted")

obj1=Person("anees","rehman")
# print(obj1.email)
print(obj1.printDetails())

print(obj1.email)
print(obj1.fname)
print(obj1.lname)
print('\n\n\n')

obj1.email="ria.institute@gmail.com"
print(obj1.email)
print(obj1.fname)
print(obj1.lname)

del obj1.email
print(obj1.email)

print("\n\n\n\n")

# obj1.email="ria.institute@gmail.com"
# print(obj1.email)
# print(obj1.fname)
# print(obj1.lname)
print(inspect.getmembers(obj1))
# print(inspect.Arguments())