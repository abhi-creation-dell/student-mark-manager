# project 2: student marks manager

students = {"Aman": [85, 90, 78], "Riya": [92, 88, 95], "Zoya": [70, 65, 80]}
highest=0
topper=""

for name,marks in students.items():
    total=0
    count=0
    for mark in marks:
        total+=mark
        count+=1
    average=round(total/count,2)

    if average>=85:
        grade="A"
    elif average>=70:
        grade="B"
    elif average>=50:
        grade="C"
    else:
        grade="F"
    print(f"{name} {average} {grade}")

    if average>highest:
        highest=average
        topper=name
print("Topper:",topper)

while True:
    print("\n====MENU====")
    print("1.Add student")
    print("2.View all")
    print("3.Show topper")
    print("4.Exit")
    choice=float(input("enter your choice:"))
    if choice==1.:
        name=str(input("enter new student name:")).strip()
        if name in students:
            print("student already exits")
            continue
        marks=[]
        while len(marks)<3:
            mark=int(input("enter mark:"))
            if 0<=mark<=100:
                marks.append(mark)
            else:
                print("invalid marks,try again")
        students[name]=marks
        print("student add successfully")


    elif choice==2.:
        for name,marks in students.items():
            total=0
            count=0
            for mark in marks:
                total+=mark
                count+=1
            average=round(total/count,2)
            if average>=85:
                grade="A"
            elif average>=70:
                grade="B"
            elif average>=50:
                grade="C"
            else:
                grade="F"
        
            print(f"{name} {average} {grade}")
            
    elif choice==3.:
        for name,marks in students.items():
            total=0
            count=0
            for mark in marks:
                total+=mark
                count+=1
            average=round(total/count,2)
        if average>highest:
            highest=average
            topper=name
        print("Topper:",topper)

    elif choice==4.:
        print("Goodbye!")
        break