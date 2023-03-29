
class Employee:
    company="T.C.S"
    employeeName="default name"
    salary="default salary"


    def employeeDetails(self):
        print(f"\nEmployee is working at {self.company}\nemployee name is {self.employeeName}\nemployee salary is {self.salary}")
    
     

emp1=Employee()
emp1.employeeName="rohan"
emp1.salary=50000
emp1.company="Infosys"
emp1.employeeDetails()


emp2=Employee()
emp2.employeeDetails()
