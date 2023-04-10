def generator(n):
    for i in range(n):
        yield i

a=generator(5)
print(a)
# for i in a:
#     print(i)
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
# for i in a:
#     print(i)