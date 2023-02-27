'''
mylist=[1,2,3.567,"python","java",True,[2,3,4,5,1,8]]
print(type(mylist))
print(mylist)
print(mylist[3])
print(mylist[5])
print(mylist[6])
print(mylist[6][2])
'''
# inbuilt method
mychar=["anees","aadithyaa","cat","bat"]
mychar.sort()
print(mychar)
mychar.reverse()
print(mychar)
mychar.append("ria")
print(mychar)

mylist2=[2,3,4,5,1,6,7,8]
mylist2.sort()
print(mylist2)
# mylist2.reverse()
# print(mylist2)
mylist2.append(9)
mylist2.append(10)
print(mylist2)
mylist2.remove(1)
mylist2.remove(7)
print(mylist2)
mylist2.remove(mylist2[4])
print(mylist2)
mylist2.insert(0,1)
mylist2.insert(1,1)
mylist2.insert(2,1)
print(mylist2.count(1))
print(mylist2)
mylist2.pop()
print(mylist2)
mylist3=mylist2.copy()
print(mylist3)
mylist3.clear()
print(mylist3)
l1=[1,2,3]
l2=[4,5,6]
l1.extend(l2)
print(l1)
mylist2.extend(l1)
print(mylist2)

# mutable="we can update or change any value"
newList=[1,2,3]
newList[0]=10
newList[1]=20
newList[2]=30
print(len(newList))
