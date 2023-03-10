# f=open("ria.txt","r")
# print(type(f))
# content=f.read()
# print(type(content))
# print(content)
# f.close()


# f=open("ria.txt","r")
# print(f.read())

# f=open("ria.txt","r")
# print(type(f))
# content=f.read()

# for i in content:
#     print(i)


# print(type(content))
# print(content)
# f.close()

# f=open("ria.txt","r")
# content1=f.readline()
# content2=f.readline()
# content3=f.readline()
# content4=f.readline()
# print(content1)
# print(content2)
# print(content3)
# print(content4)
# f.close()

# f=open("ria.txt","r")
# content=f.readlines()
# print(content)
# f.close()

# f=open("ria.txt","r")
# content=f.readlines()
# print(content[3])
# f.close()


# f=open("ria.txt","r")
# content=f.readlines()
# print(content[3])
# f.close()

# f=open("ria.txt","r")
# content=f.readlines()
# print(content[2:5])
# f.close()


# f=open("ria.txt","r")
# content=f.readlines()
# for i in content[2:5]:
#     print(i)
# f.close()

# f=open("ria.txt","w")
# f.write("hello world")
# f.close()


# f=open("ria.txt","a")
# f.write("\nhello world")
# f.close()


# f=open("ria.txt","r+")
# content=f.read()
# print(content)
# f.write("\ni am new text")
# f.close()

f=open("ria.txt","r+")
f.write("i am new text write and read\n")
content=f.read()
print(content)
f.close()

f=open("ria.txt","r+")
f.seek(125)
print(f.tell())
print(f.readlines())
f.close()