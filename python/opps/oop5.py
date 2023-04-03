# constructors - it is a init method inside a class which is going to call whenever the object is created and set the values for the varaibles for specific object

class Employee:
    company="Infosys"

    def __init__(self,name,role,age,salary): #consructors #step-2
        print("i am constructor i am gonna set the values")
        self.name=name
        print(self.name)
        self.role=role
        self.age=age
        self.salary=salary
        print("i have set the values to specific object") #step-3

    def employeeDetails(self): #step-5
        print(f"\nEmployee name is {self.name} \nAge is {self.age} \nRole is {self.role}\nSalary is {self.salary}")

class Student:
    insititue="ria"

    def __init__(self,name,age): #consructors
        self.name=name  #set the values
        self.age=age


    def studentDetails(self):
        print(f"Student name is {self.name} \nAge is {self.age}")



emp1=Employee("Rohan","front-end dev",23,50000) #step-1
emp1.employeeDetails()  #step-4
emp2=Employee("mohan","back-end dev",24,60000)
emp2.employeeDetails()

stud1=Student("anees",12)
stud1.studentDetails()
print(stud1.fullname)