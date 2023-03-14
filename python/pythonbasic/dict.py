# # dictionary
# mydictionary={
#     "Name":"Ria Insitute",
#     # "Name1":"Ria Insitute",
#     "Location":"Marathalli",
#     "Pincode":560032,
#     "IsActive":True,
#     "Courses":["python","Sap","Spoken English"],
#     "Branch":("marathalli","Rt nagar")
# }
# # print(mydictionary)
# # print(type(mydictionary))


# print(mydictionary.keys())
# print(mydictionary.values())
# print(mydictionary.get("Courses"))

# data=mydictionary.items()
# print(data)
# print(type(data))
# # print(data[2])
# # print(mydictionary[2])

# mydictionary.update({"phone Number":9874563210})
# mydictionary.update({"IsActive":False})
# print(mydictionary)
# print(mydictionary.get("anees"))
# print(mydictionary["phone Number"])
# # print(mydictionary["anees"])
# print(len(mydictionary))


thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
thisdict.pop("age")
# # mydictionary.pop("aa")
print(thisdict)
# print(mydictionary)
thisdict.popitem()
print(thisdict)

# # copy
# # clear
# # fromkeys