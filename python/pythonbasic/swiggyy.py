'''
2)write a python program to order the food in the swiggy
a)display the menue for the user
1. Dosa 40
2. Idli 30
3. Pizza 150
4. Burgers 150
5. Chicken 200
6. Biryani 250
7. Ice Cream 80
8. Place order

#calling to swigy........
example : press 1 to order Dosa

if i press 4.
your order is been added to cart

if i press 6.
your order is been added to the cart 

if i press 8
your order is placed.
items : list
your total amount is :  '''


''''
menuitems={1:'rice',2:'idli',3:'burger',4:'pizza',5:'chicken',6:'dosa',7:'tea',8:'exit'}



orderItems=[]


def store(data):
    orderItems.append(data)
    menu()

def handleMenu():
    inp=int(input("Enter : "))
    data=menuitems.get(inp)
    if inp>len(menuitems) or inp==8:
        print("Ordered Items are ",orderItems)
    else:
        store(data)


def menu():    
    print("Welcome to swiggy")
    for i,j in menuitems.items():
        print(f'Press : {i} to Order {j}')
    

    handleMenu()

menu()
'''


import time

items=[]
totalAmount=[]

def Dosa(item,price):
    items.append(item)
    totalAmount.append(price)
    print("Added to Cart",item)
    time.sleep(2)
    Swiggy()

def Burger(item,price):
    items.append(item)
    totalAmount.append(price)
    print("Added to Cart",item)
    time.sleep(2)
    Swiggy()

def Pizza(item,price):
    # """ aa"""
    items.append(item)
    totalAmount.append(price)
    print("Added to Cart",item)
    time.sleep(2)
    Swiggy()

def Chicken(item,price):
    items.append(item)
    totalAmount.append(price)
    print("Added to Cart",item)
    time.sleep(2)
    Swiggy()

def PlaceOrder():
    print("Your Order is Placed:")
    print("Ordered Items are:")
    for i in items:
        print(i)
    print("Total Amount to be Paid : ",sum(totalAmount))
   
def Swiggy():
    print("Select the Items Menu:")
    print("1. Dosa")
    print("2. Burger")
    print("3. Pizza")
    print("4. Chicken")
    print("5. Place Final Order")
    n=int(input("Select the Number: "))
    if(n>0 and n<=5):
        if(n==1):
            Dosa("Dosa",50)        
        elif(n==2):
            Burger("Burger",150)
        elif(n==3):
            Pizza("Pizza",250)
        elif(n==4):
            Chicken("Chicken",350)
        elif(n==5):
            PlaceOrder()
        else:
            pass



print("Welcome to Swiggy")
Swiggy()