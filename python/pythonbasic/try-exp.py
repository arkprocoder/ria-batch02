num1=int(input("enter the num1\n"))
num2=int(input("enter the num2\n"))
try:
    # print("i am a try if no error i will execute")
    print("divide res",num1/num2)

except Exception as e:
    pass
    print("exception was ",e)
    # print("i will execute only if there is a exception")