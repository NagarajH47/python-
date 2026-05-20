# Q12. Employee Salary Dictionary

employees = {}

def add_employee(name, salary):
    employees[name] = salary

def update_salary(name, salary):
    employees[name] = salary

def search_employee(name):
    if name in employees:
        print(name, employees[name])
    else:
        print("Employee not found")

add_employee("Ravi", 30000)
update_salary("Ravi", 35000)
search_employee("Ravi")