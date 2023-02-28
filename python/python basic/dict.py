# dictionary
mydictionary={
    "Name":"Ria",
    "Name":"Ria Insitute",
    "Location":"Marathalli",
    "Pincode":560032,
    "IsActive":True,
    "Courses":["python","Sap","Spoken English"],
    "Branch":("marathalli","Rt nagar")
}
print(mydictionary)
print(type(mydictionary))


print(mydictionary.keys())
print(mydictionary.values())
print(mydictionary.get("Courses"))

data=mydictionary.items()
# print(data)
# print(data[2])
# print(mydictionary[2])

mydictionary.update({"phone Number":9874563210})
mydictionary.update({"IsActive":False})
print(mydictionary)
print(mydictionary.get("anees"))
print(mydictionary["phone Number"])
# print(mydictionary["anees"])
print(len(mydictionary))


thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
mydictionary.pop("IsActive")
# mydictionary.pop("aa")
print(mydictionary)
mydictionary.popitem()
print(mydictionary)

# copy
# clear
# fromkeys