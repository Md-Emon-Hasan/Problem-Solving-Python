# 89. Nested Dictionary Update: Given a nested dictionary of employee details, write a Python program to update an employee’s salary based on their employee ID.

employees = {
    "E101": {"name": "Alice", "salary": 50000},
    "E102": {"name": "Bob", "salary": 60000}
}

emp_id = input("Enter Employee ID: ")
new_salary = int(input("Enter new salary: "))

if emp_id in employees:
    employees[emp_id]["salary"] = new_salary
    print("Salary updated successfully")
else:
    print("Employee ID not found")

print("Updated employee data:", employees)