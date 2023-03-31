salary=int(input("enter your salary\n"))
tax=0

def tax(salary):
    if salary<=10000:
        return 0
    elif (salary>10000 and salary<=20000):
        y=salary-10000
        y=(y*10)/100
        return y
    else:
        z=salary-20000
        x=1000 
        y=(z*20)/100
        y=y+x
        return y
        
tax=tax(salary)
print("tax is ",tax)