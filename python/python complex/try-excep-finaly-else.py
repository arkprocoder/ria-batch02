try:
    pass #run the code when there is no error
except:
    pass # executes when try block fails
else:
    pass #executes when try block has no errors and except block is not used
finally:
    pass # i dont care about try except and else i am going to execute compulsory


def Divide(a,b):   

    try:
        # print("i am a try if no error i will execute")
        print("divide res",a/b)

    except Exception as e:        
        print("exception was ",e)
            
    else:
        print(" i am else block ")
    
    finally:
        print("i am finally block",num1+num2)

num1=int(input("enter the numerator value\n"))
num2=int(input("enter the denominator value\n"))
Divide(num1,num2)