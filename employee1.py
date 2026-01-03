def calculate_grade(salary):
    if salary >= 80000:
        return "Grade A"
    elif salary >= 60000:
        return "Grade B"
    elif salary >= 40000:
        return "Grade C"
    elif salary >= 25000:
        return "Grade D"
    else:
        return "Grade E"

def display_employee(name, emp_id, department, salary):
    grade = calculate_grade(salary)
    print("Employee Name :", name)
    print("Employee ID   :", emp_id)
    print("Department    :", department)
    print("Monthly Salary: ₹", salary)
    print("Salary Grade  :", grade)

def main():
    # Static values (NO input)
    name = "Sindhu"
    emp_id = "EMP101"
    department = "IT"
    salary = 65000

    display_employee(name, emp_id, department, salary)

main()

