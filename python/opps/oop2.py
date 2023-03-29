class Student:
    schoolName="Ria School"
    location="Bangalore"
    name="student name"

stud1=Student()
print(stud1.location)
print(stud1.schoolName)
stud1.name="rohan"
print(stud1.name)
print(stud1)

stud2=Student()
print(stud2.location)
print(stud2.schoolName)
print(stud2.name)
stud2.hobbies=["eating","sleeping"]
stud2.isMale=True
stud2.age=20
stud2.marks={
    "english":85,
    "maths":100
}
stud2.subject={"english","maths"}
stud2.attendance=(1,2,4)

print(Student.location)
print(stud2.__dict__)
print(stud1.__dict__)
print(Student.__dict__)

stud3=Student()
print(stud3.__dict__)