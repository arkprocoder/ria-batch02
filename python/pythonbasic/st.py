# s={1,2,3,4,5,6,4,5,6}
# print(type(s))
# print(s)

s=set()
print(type(s))
s.add(1)
s.add(9)
s.add(8)
s.add(3)
s.add(2)
print(s)
# print(s[3])
print(len(s))
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.clear())
print(s.remove(8))
# print(s.remove(18))
print(s)

s1={1,2,3,4,5,6,"ria",True,2.568,None}
s2={2,3,7,8,9}
s3={2,3,7,8,9,10}
print(s1.union(s2).union(s3))
print(s1.intersection(s2))
print(s1.isdisjoint(s2))
print(s1.issubset(s2))
print(s1.issuperset(s2))

# for i in s1:
#     print(i)

# l1=[1,2,3,4,12,34,2,3]
# print(type(l1))
# l1=set(l1)
# print(type(l1))
# l1=list(l1)
# print(l1)