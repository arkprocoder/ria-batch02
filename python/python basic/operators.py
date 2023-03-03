x=10
x+=20 # x=x+20
print(x)

y=20
y%=2 #y=y%2 #y=20%2
print(y)

y=20
y%=20
print(y)

y=20
y%=3
print(y)

y=20
y%=30
print(y)

# Logical OR and  Not
'''
True =1
False=0

# and as multiplication
True and True = True
True and False = False
False and True = False
False and False = False

# or as addition
True or True = True
True or False = True
False or True = True
False or False = False 

!False=True
!True =False

'''


print(True and True )
print(True and False )
print(False and True )
print(False and False )

print(True or True )
print(True or False )
print(False or True )
print(False or False )

print(not False)
print(not True)

print( "is and is not")

a=20
b=30
d=20
print(a is b)
print(a is d)
print(a is not d)
print(True is not False)
print(True is  False)
print(10 is not 10)

print("membership ")
mylist=[2,3,45,6,"ria"]
print(5 in mylist)
print(45 in mylist)
print(45 not in mylist)
print("ria"  in mylist)
print(6/2  in mylist)

print(0 and 0)
print(0 & 1)
print(1 & 0)
print(1 & 1)

print(0 | 0)
print(0 | 1)
print(1 | 0)
print(1 or 1)

print(a!=b)
print(a==d)