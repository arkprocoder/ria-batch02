'''
iterable=[2,4,6,8,10]
# odd=list(map(function,iterable))
listodd=list(map(lambda x:x-1,iterable))
setodd=set(map(lambda x:x-1,iterable))
tupodd=tuple(map(lambda x:x-1,iterable))
mapodd=map(lambda x:x-1,iterable)
print(listodd,type(listodd))
print(setodd,type(setodd))
print(mapodd,type(mapodd))
print(tupodd,type(tupodd)) '''


def square(n):
    return n*n

def cube(n):
    return n*n*n

def power(n):
    return n**n

def circle(n):
    return 3.14*n*n
    # return 3.14*square(n)

iterable=[square,cube,power,circle]

start=int(input("enter the start value\n"))
stop=int(input("enter the stop value\n"))

for i in range(start,stop):
    res=list(map(lambda x:x(i),iterable))
    print(res)
    # res=list(map(lambda x:square(2),square))
    # res=list(map(lambda x:cube(2),cube))
    # res=list(map(lambda x:power(2),power))
    # res=list(map(lambda x:circle(2),circle))
    # [2,23,34,55]
