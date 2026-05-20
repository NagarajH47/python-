# Q14. Voting Eligibility Checker

ages = (12, 18, 25, 16, 40)

def check_voting(age):
    if age >= 18:
        return "Eligible"
    else:
        return "Not Eligible"

for age in ages:
    print(age, "-", check_voting(age))