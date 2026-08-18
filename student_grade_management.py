"""
    Student Grade Management System
    1. Add Student
    2. Update Student
    3. Delete Student
    4. View Student
    5. Exit

"""
student_grade={ }
def add(name,grade) :
    student_grade[name]=grade
    print(f"Added {name} with a{grade}")
    
def update(name,grade):
    if name in student_grade:
        student_grade[name]=grade

        print(f"{name} with marks are updated {grade}")

    else:
        print(f"{name} is not found!")

def delete(name):
    if name in student_grade:
        del student_grade[name]
        print(f"{name} has been successfully deleted")

    else:
        print(f"{name} is not found!")

def view():
    if student_grade:
        for name,grade in student_grade.items():
            print(f"{name} : {grade}")

    else :
        print("No students found/added") 



def main():
    while True:
        print("\nStudent Grade Management System")   
        print("1. Add Student") 
        print("2. Update Student") 
        print("3. Delete Student") 
        print("4. View Student") 
        print("5. Exit") 

        choice=int(input("Enter your choice = "))

        if choice==1:
            name = input("Enter Your Name = ")
            grade = input("Enter Your Grade = ")
            add(name,grade)

        elif choice==2:
            name = input("Enter Your Name = ")
            grade = input("Enter Your Grade = ")
            update(name,grade)

        elif choice==3:
            name = input("Enter Your Name = ")
            delete(name)

        elif choice==4:
            view()

        elif choice==5:
            print("Closing the program....")
            break
        
main()