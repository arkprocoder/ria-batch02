'''
2)Take a inputs and Evaluate the expressions
a)Take the Students name
b)Take the student english marks
maths,science,social,kannada,hindi
c)add the total marks 
d)print average
e)add languages marks (english,kannada,hindi)and print average
f)add the core subjects (maths,science and social)and print average
'''
sName=str(input("enter student name \n"))
english=int(input("enter english marks \n"))
maths=int(input("enter maths marks \n"))
science=int(input("enter science marks \n"))
social=int(input("enter social marks \n"))
kannada=int(input("enter kannada marks \n"))
hindi=int(input("enter hindi marks \n"))
total=english+kannada+maths+science+social+hindi
avg=total/6
langTotal=english+kannada+hindi
AvgLan=langTotal/3
coreSubTotal=maths+science+social
avgcore=coreSubTotal/3
avgcore=coreSubTotal/3
print(f'average of all sub is {avg}\nLangauges total marks is {langTotal}\nAverage of languages marks {AvgLan}\n Core languaes total marks {coreSubTotal}\tAverage of core subject {avgcore}')
