# def greeting():
#     print("Good Morning Ria")
 
# greeting()


# def greeting(name):
#     print("Good Morning",name)
 
# greeting("anees")
# greeting("Subendru")

# def greeting(name="gobin"):
#     print("Good Morning",name)
 
# greeting()
# greeting("anaya")


# def greeting(name="gobin",salary=15000):
#     print("Good Morning",name,"\n Salary credited ",salary)
 
# greeting()
# greeting("anaya",50000)
# greeting(50000,"meghana")

# def greeting(name,salary):
#     print("Good Morning",name,"\n Salary credited ",salary)
 
# greeting()
# greeting("anaya",50000)
# x=200
# a=20 # global
# b=30
# def sum(a,b): #sum(20,30)
#     print(a,b)
#     a=40 #local variable
#     b=60
#     # c=150
#     print(a+b)
#     x=300
#     print(x)

# sum(a,b)
# print(a,b)
# print(c)

mylisSal=[]

def employee(name,salary):
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

a,b=employee("Anees",125000) #AneesSal=40000
print(a,b)
# print("outside the function anees sal",AneesSal)
# GobinSal=employee("Gobin",35000) #GobinSal=50000
# print("outside the function gobin sal",GobinSal)
# MeghanaSal=employee("Meghana",45000) #MeghanaSal=60000
# print("\n")
# print(AneesSal,GobinSal,MeghanaSal)
# print((AneesSal+GobinSal+MeghanaSal)/3)
# print(mylisSal)

# 1)write a 4 functions
# a)to find the area of circle
# b) to find the area of rectangle
# c)to find the area of square
# d)find the area of triangle
# use return statements and print it 
# for taking the inputs use input()


# 2)write a python program to order the food in the swiggy
# a)display the menue for the user
# 1. Dosa 40
# 2. Idli 30
# 3. Pizza 150
# 4. Burgers 150
# 5. Chicken 200
# 6. Biryani 250
# 7. Ice Cream 80
# 8. Place order

# #calling to swigy........
# example : press 1 to order Dosa

# if i press 4.
# your order is been added to cart

# if i press 6.
# your order is been added to the cart 

# if i press 8
# your order is placed.
# items : list
# your total amount is : amount