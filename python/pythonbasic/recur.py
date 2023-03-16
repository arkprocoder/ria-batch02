def factorial(n):
    if n==1 or n==0:
        return 1  
    return n*factorial(n-1)

returnVal=factorial(5)
print(returnVal)

# # tracing
# def factorial(5):
#     if 5==1 or 5==0:#false
#         return 1  
#     return 5*factorial(5-1)
#     return 5*factorial(4)

# returnVal=factorial(5)

# def factorial(4):
#     if 4==1 or 4==0:#false
#         return 1  
#     return n*factorial(n-1)
#     return 5* 4*factorial(4-1)
#     return 5* 4* factorial(3)

# returnVal=factorial(3)

# def factorial(3):
#     if 3==1 or 3==0:#false
#         return 1  
#     return n*factorial(n-1)
#     return 5* 4* 3*factorial(3-1)
#     return 5* 4* 3* factorial(2)

# returnVal=factorial(3)


# def factorial(2):
#     if 2==1 or 2==0:#false
#         return 1  
#     return n*factorial(n-1)
#     return 5* 4* 3*2* factorial(2-1)
#     return 5* 4* 3* factorial(1)

# returnVal=factorial(2)


# def factorial(1):
#     if 1==1 or 1==0:#false
#         return 1  
#     return n*factorial(n-1)
    
#     return 5* 4* 3* 2*1

# returnVal=factorial(1)

# print(120)