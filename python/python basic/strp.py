# strings in python
mystr="ria university "
print(mystr,"1")
print(mystr.capitalize(),"2")
mystr=mystr.capitalize()
print(mystr.upper(),"3")
print(mystr,"4")
print(mystr.lower(),"5")

print(mystr.count("2"))
print(mystr.count("r"))
print(mystr.count("i"))
print(mystr.count(" "))
print(mystr.count("university "))
print(len(mystr))
print(mystr.find("ark"))
print(mystr.find("university"))
print(mystr.replace("university","Institute"))
mystr=mystr.replace("university ","Institute")
print(mystr)
print(mystr.endswith("tute"))
print(mystr.startswith("ria"))
print(mystr.startswith("Ria"))
print(mystr.index("i"))
print(mystr.isdigit())
z="a"
a="10"
print(z.isalpha())
print(a.isdigit())