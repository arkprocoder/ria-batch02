# def add(x,y):
#     print(x+y)
# add(1,2)

add=lambda x,y,z:x+y+z
minus=lambda x,y:x-y
divide=lambda x,y:x/y
multiply=lambda x,y:x*y

res=add(10,20,50)
print(res,"returned")
print(minus(10,20))
print(divide(10,20))
print(multiply(10,20))