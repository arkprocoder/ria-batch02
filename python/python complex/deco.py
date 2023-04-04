# def Orders(handlerequest):
#     pass

# @Orders
# def handlerequest():
#     pass


# def Orders(handlerequest):
#     def takeOrder():
#         print("Order is taken")

#         handlerequest(100)
#     return takeOrder


# @Orders
# def handlerequest(id):
#     print("the order id is",id)

# handlerequest()


def ria(student): #step-3
    def employee(): #step-5
        print("i am part time employee in ria")
        student("gobin") #step-6
        print("done the job") #step-8
    return employee  #step-4
    
@ria #step-2
def student(name): #step-7
    print("i am student at ria my name is ",name)

student()  #step-1