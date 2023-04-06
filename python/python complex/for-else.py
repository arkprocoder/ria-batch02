# mylist=["a","b","c","d","e","f"]
# for i in mylist:
#     print(i)
# else:
#     print("i am a else block of for loop")




items=["pizza","burger","frice"]

for j in items:
    if j=="chiken":
        print(j,"is tasty")
        break
    else:
        print("item not found")


items=["pizza","burger","frice","chiken"]

for j in items:
    if j=="chiken":
        print(j,"is tasty")
        break
    # print(j)
else:
    print("item not found")