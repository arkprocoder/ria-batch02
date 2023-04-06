class Company:
    company_name="Accenture"
    
    def __init__(self,EmployeeName,EmployeeRole,EmployeeSalary):  #this contructor wont get called when you create a object for Employee that is child class
        self.EmployeeName=EmployeeName
        self.EmployeeRole=EmployeeRole
        self.EmployeeSalary=EmployeeSalary

    def CompanyEmployeeDetails(self):
        print(f"\nCompany name is {self.company_name}\nEmployeeName is {self.EmployeeName}\nEmployeeRole is {self.EmployeeRole}\nEmployeeSalary is {self.EmployeeSalary}")

class Employee(Company):
    
    def __init__(self,EmployeeName,EmployeeRole,EmployeeSalary,EmployeeManager,EmployeeTL):
        self.EmployeeName=EmployeeName
        self.EmployeeRole=EmployeeRole
        self.EmployeeSalary=EmployeeSalary
        self.EmployeeManager=EmployeeManager
        self.EmployeeTL=EmployeeTL
    
            
    def EmployeeDetails(self):
        print(f"\nEmployeeName is {self.EmployeeName}\nEmployeeRole is {self.EmployeeRole}\nEmployeeSalary is {self.EmployeeSalary}\nEmployeeManager is {self.EmployeeManager}\nEmployeeTL is {self.EmployeeTL}")



obj1=Employee("Rahul","frontend dev",25000,"Saranya","Raju")
obj1.CompanyEmployeeDetails()
obj1.EmployeeDetails()
# print(obj1.EmployeeName1)

cp1=Company("Rahul","frontend dev",25000)
print(cp1.company_name)
cp1.CompanyEmployeeDetails()
