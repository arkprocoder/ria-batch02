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

    
    def getemployeeSalary(self):
        print(f"\nsalary is {self.salary}")
    
    @staticmethod
    def employeeBank():
        print(f"Company uses default ICIC Bank for all the employees ")
    
    @staticmethod
    def employee(name,salary):
    # def employee(self,name,salary):
        mylisSal=[]
        print(f"\nEmployee {name}\n Salary Credited {salary}")
        bonus=15000
        salary=salary+bonus
        mylisSal.append(salary)
        if salary<50000:
            print("total salary is ",salary)
            return salary,bonus
        else:
            print("Total salary is greater than 50000",salary)
            return salary,bonus
     

    @classmethod
    def changeDetails(self,name,role):
        self.name=name
        self.role=role
        print(f"i have changed the role {self.role} for {self.name} it will work only in this method call and it wont change in the constructor init method")


emp1=Employee("Rohan","front-end dev",23,50000) #step-1
emp1.employeeDetails()  #step-4
# emp2=Employee("mohan","back-end dev",24,60000)
# emp2.employeeDetails()
# emp1.employeeBank()
# emp1.getemployeeSalary()
# emp1.employeeBank()
# emp1.employee("anees",40000)
emp1.changeDetails("ark","Full stack dev")
emp1.employeeDetails()

emp2=Employee("Shreya","database engineer",21,50000)
emp2.employeeDetails()
emp2.changeDetails("Shreya","backend dev")