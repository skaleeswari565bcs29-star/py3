students=[]
n=int(input("enter no of students:"))
for i in range(n):
    s_id=int(input("enter student id:"))
    name=input("enter name:")
    marks=int(input("enter marks:"))
    student=(s_id,name,marks)
    students.append(student)
students=tuple(students)
print("\n student details")
for s in students:
    print("ID:",s[0],"Name",s[1],"Marks",s[2])
k=int(input("\n enter student id:"))
f=0
for s in students:
    if s[0]==k:
        print("student found")
        print("ID:",s[0],"Name:",s[1],"Marks:",s[2])
        f=1
if not f:
    print("student not found")
max=students[0]
for s in students:
    if s[2]>max[2]:
        max=s
print("\n student with highest marks:")
print("ID:",max[0],"Name:",max[1],"Marks:",max[2])
print("\n student with less 40 marks:")
for s in students:
    if s[2]<40:
       print("ID:",s[0],"Name:",s[1],"Marks:",s[2])
t=0
for s in students:
    t=t+s[2]
avg=t/len(students)
print("\n average marks:",avg)
