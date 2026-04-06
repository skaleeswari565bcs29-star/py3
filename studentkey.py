d={}
n=int(input("enter no of students"))
for i in range(n):
    name=input("enter name:")
    marks=int(input("enter mark:"))
    d[name]=marks
print(d)
key=input("enter name of student:")
if key in d:
    print("the mark of",key,"is",d[key])
else:
    print("student not found")
