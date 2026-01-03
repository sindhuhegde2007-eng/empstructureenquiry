# Function to calculate salary grade
def get_salary_grade(salary):
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

# Function to display employee details
def display_employee_details(name, emp_id, department, salary):
    grade = get_salary_grade(salary)
    print("\n--- Employee Details ---")
    print("Employee Name :", name)
    print("Employee ID   :", emp_id)
    print("Department    :", department)
    print("Monthly Salary: ₹", salary)
    print("Salary Grade  :", grade)

# Main program
def main():
    name = input("Enter Employee Name: ")
    emp_id = input("Enter Employee ID: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Monthly Salary (₹): "))

    display_employee_details(name, emp_id, department, salary)

# Run the program
main()
