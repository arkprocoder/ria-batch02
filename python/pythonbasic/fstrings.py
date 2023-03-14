a=10
b=20
c=40
d=a+b+c

print("the sum of ",a,"+",b,"+",c,"=",d)
print(f"the sum of {a} + {b} + {c} = {d}")
print(f'the sum of {a} + {b} + {c} = {d}\nthis is easy')

print(a,b)
a,b,c=b,a,a+b
print(a,b,c)