# Q17. Student Result Analyzer

marks = [45, 78, 90, 35, 60]

def average(marks):
    return sum(marks) / len(marks)

def passed_students(marks):
    count = 0
    for m in marks:
        if m > 40:
            count += 1
    return count

print("Average:", average(marks))
print("Highest:", max(marks))
print("Lowest:", min(marks))
print("Passed Students:", passed_students(marks))