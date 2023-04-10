# mylist=[]
# for i in range(11):
#     print(i)
#     if i%2==0:
#         mylist.append(i)

# print(mylist)

# mylistcompres=[i for i in range(11) ]
# print(mylistcompres)

# mylistcompres=[i for i in range(11) if i%2==0]
# print(mylistcompres)

# mysetcompres={i for i in range(11) if i%2==0}
# print(mysetcompres)

# mytupcompres=(i for i in range(11) if i%2==0)
# print(mytupcompres)
# for i in mytupcompres:
#     print(i)


# mydictwithoutcompress={}
# for i in range(100):
#     mydictwithoutcompress.update({i:f'Name {i}'})

# print(mydictwithoutcompress)

# dictCompress={i:f'Name {i}' for i in range(100)}
# print(dictCompress)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)