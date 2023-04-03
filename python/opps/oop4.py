
class Employee:
    company="T.C.S"
    employeeName="default name"  #data members of the class varaiables
    salary="default salary"


    def employeeDetails(self):  #default self we have to pass compulsory whenever we are creating a method inside the class 
        print(f"\nEmployee is working at {self.company}\nemployee name is {self.employeeName}\nemployee salary is {self.salary}")
    
class Company:
    no_of_employee="2 lakhs"

    def companyDetails(self):
        print("Company is accenture it will fired 20,000 employees",self)



emp1=Employee()
emp1.employeeName="rohan"
emp1.salary=50000
emp1.company="Infosys"  #instance class level varaibles
emp1.employeeDetails()


emp2=Employee()
emp2.employeeDetails()

print("\n")
obj1=Company()
print(obj1.no_of_employee)
obj1.companyDetails()