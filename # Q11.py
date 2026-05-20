# Q11. Attendance System

students = ["Rahul", "Aman"]

def add_student(name):
    students.append(name)

def remove_student(name):
    students.remove(name)

def display_students():
    print(students)

add_student("Kiran")
remove_student("Aman")
display_students()