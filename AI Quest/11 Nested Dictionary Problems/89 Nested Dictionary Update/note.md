# Nested Dictionary Update

## Problem
Given a nested dictionary containing employee details, update an employee’s salary using their employee ID.

Example

Input
```
employees = {
 "E101":{"name":"Alice","salary":50000},
 "E102":{"name":"Bob","salary":60000}
}

Employee ID = E101
New Salary = 70000
```

Output
```
Salary updated successfully
```

Updated dictionary:

```
{
 "E101":{"name":"Alice","salary":70000},
 "E102":{"name":"Bob","salary":60000}
}
```

---

# Theory

A nested dictionary stores dictionaries inside another dictionary.

Access pattern:

```
dictionary[outer_key][inner_key]
```

To update a value:

```
dictionary[key1][key2] = new_value
```

---

# Approach

1. Initialize nested dictionary
2. Take employee ID as input
3. Take new salary as input
4. Check if employee exists
5. Update salary
6. Print updated dictionary

---

# Python Implementation

```python
employees = {
 "E101":{"name":"Alice","salary":50000},
 "E102":{"name":"Bob","salary":60000}
}

emp_id = "E101"
new_salary = 70000

employees[emp_id]["salary"] = new_salary

print(employees)
```

---

# Key Idea

Nested dictionary update pattern:

```
dict[key1][key2] = value
```