# mytup=(1,2,3,4,5,6,7,8,9,10)

# def functionArguments(*args):
#     for i in args:
#         print(i)
#     print(args)
#     print(type(args))

# functionArguments(mytup)

# # mylist=[1,2,3,4,5,6,7,8,9,10]
# # def functionArguments(name,*args):
# # # def functionArguments(*args,name):
# #     for i in args:
# #         print(i)
# #         print(type(i))
# #     print(args)
# #     print(type(args))
# #     print(type(name))
# #     print(name)

# functionArguments(mylist,"ark")

# myset={1,2,3,4,5,6,7,8,9,10}
# def functionArguments(name,*args):
# # def functionArguments(*args,name):
#     for i in args:
#         print(i)
#         print(type(i))
#     print(args)
#     print(type(args))
#     print(type(name))
#     print(name)

# functionArguments("ark",myset)

# keyword args

mydict={
    "name":"ria institute",
    "established":2012,
    "courses":["python","java"],
    "isActive":True
}

course=["Sap","spoken english","hindi"]
location="Bangalore"

# def keywordargs(*args):
#     pass
# keywordargs(course)

# def keywordargs(loc,*args):
#     pass
# keywordargs(location,course)


# def keywordargs(**kwargs):
#     pass
# keywordargs(mydict)

# def keywordargs(loc,**kwargs):
#     pass
# keywordargs(location,mydict)


# def keywordargs(**mydict):
#     print(mydict)

#     for i,j in mydict.items():
#         print(i,j)


# keywordargs(**mydict)

def keywordargs(loc,**mydict):
    print(mydict)
    print(loc)

    for i,j in mydict.items():
        print(i,j)


# keywordargs(location,**mydict)

# def keywordargs(loc,*args,**kwargs):
#     print(kwargs)
#     print(kwargs)
#     print(loc)

#     for i,j in kwargs.items():
#         print(i,j)


# keywordargs(location,course,**mydict)


# n = 5
# k = 5
# for i in range(0,n+1):
#     for j in range(k-i,0,-1):
#         print(j,end=' ')
#     print()

# # # tracing
# # for i in range(0,6):
# #     for j in range(5,0,-1):
# #         print(j,end=' ')
# #     print()

# # for j in range(5,0,-1):
# #     print(j,end=' ')

# for i in range(1,6):
#     for j in range(4,0,-1):
#         print(j,end=' ')
#     print()

# for j in range(4,0,-1):
#     print(j,end=' ')

# for i in range(5,6):
#     for j in range(1,0,-1):
#         print(j,end=' ')
#     print()

# for j in range(4,0,-1):
#     print(j,end=' ')