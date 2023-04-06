# single level inheritance

class Company:
    company_name="Accenture"
    
    def __init__(self,location,branch,no_of_block):
        self.location=location
        self.branch=branch
        self.no_of_block=no_of_block

    def companyDetails(self):
        print(f'Company is {self.company_name}\nLocation is {self.location}\nBranch is {self.branch}\nNo of building blocks is {self.no_of_block}')
    
    @staticmethod
    def companyBaseSalary():
        print("Base salary is 4LPA")

class Employee(Company):
    
    def __init__(self,EmployeeName,EmployeeRole,EmployeeSalary):
        self.EmployeeName=EmployeeName
        self.EmployeeRole=EmployeeRole
        self.EmployeeSalary=EmployeeSalary
        
    def EmployeeDetails(self):
        print(f"EmployeeName is {self.EmployeeName}\nEmployeeRole is {self.EmployeeRole}\nEmployeeSalary is {self.EmployeeSalary}")

    
    def EmployeeInsurance(self):
        print(f"{self.company_name} has HIP policy")



emp1=Employee("harsith","dev",23000)
print(emp1.company_name)
emp1.companyBaseSalary()
emp1.EmployeeDetails()
emp1.EmployeeInsurance()

cp1=Company("Bangalore","Infy",7)
cp1.companyDetails()
cp1.companyBaseSalary()
