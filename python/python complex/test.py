
# kwargs
mydict={
"name":"rohan",
"age":25,
"phone":7895463210,
"salary":7894.52
}
mylist=[1,2,3,4,5,6,7,8,9,10]

def keywordArgsFunction(greet,*args,**kwargs):
    print(kwargs)
    for i in args:
        print(i)

    for k,v in kwargs.items():
        print("key is ",k,"value is ",v)
    
    print(greet,"good morning")


keywordArgsFunction("ark",mylist,mydict)

