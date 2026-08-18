"""
    Student Grade Management System
    1. Add Student
    2. Update Student
    3. Delete Student
    4. View Student
    5. Exit

"""
def management() : 
    student=[]
    operation=int(input("Student Grade Management System\n 1. Add Student\n 2. Update Student\n 3. Delete Student\n 4. View Student\n 5. Exit\n Enter your choice :  "))
    
    if operation == 1:
        name=input("Enter student name = ")
        grade=int(input("Enter student grade = "))
        student.append(f"{name} : {grade}")
        print(f"Added {name} with a {grade}")

    elif operation==2:
        update=input("Enter  what you want to update : ")
        if update in student:
            up=input("Enter new task : ")
            ind=student.index(update)
            student[ind]=up
            print(f"Updated task {up}")
    


management()