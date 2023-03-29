# fruits=["apple","orange","banana","grapes"]
# separator="#"
# res=separator.join(fruits)
# print(res)
# print(type(res))

# fruits={"apple","orange","banana","grapes"}
# separator="#"
# res=separator.join(fruits)
# print(res)
# print(type(res))

# fruits=("apple","orange","banana","grapes")
# separator="/"
# res=separator.join(fruits)
# print(res)
# print(type(res))

# mydict={"employeName":"Anees","employeeSalary":"12345","isActive":"True"}
# seprator="ria"
# newmydict=seprator.join(mydict.keys())
# print(newmydict)

print("*************")
mylist=[]
fName=input("enter your first name \n")
lName=input("enter your last name \n")
mylist.append(fName)
mylist.append(lName)
name="".join(mylist)
mylist.clear()
mylist.append(name)
mylist.append("")
sep="@gmail.com"
print(mylist)
print(sep.join(mylist))