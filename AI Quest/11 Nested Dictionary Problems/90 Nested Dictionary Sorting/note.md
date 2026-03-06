# Nested Dictionary Sorting

## Problem
Given a nested dictionary containing product details, sort the products based on their **price in ascending order**.

Example

Input
```
products = {
 "p1":{"name":"Laptop","price":800,"quantity":5},
 "p2":{"name":"Phone","price":500,"quantity":10},
 "p3":{"name":"Tablet","price":300,"quantity":7}
}
```

Output (sorted by price)

```
Tablet → 300
Phone → 500
Laptop → 800
```

---

# Theory

To sort a nested dictionary:

1. Convert dictionary to key-value pairs using `items()`
2. Use `sorted()` with a key function
3. Access inner dictionary value

Example key function:

```
lambda x: x[1]["price"]
```

Where:

```
x[0] → outer key
x[1] → inner dictionary
```

---

# Approach

1. Initialize nested dictionary
2. Use `sorted()` with key function
3. Convert result to dictionary
4. Print sorted dictionary

---

# Python Implementation

```python
products = {
 "p1":{"name":"Laptop","price":800,"quantity":5},
 "p2":{"name":"Phone","price":500,"quantity":10},
 "p3":{"name":"Tablet","price":300,"quantity":7}
}

sorted_products = dict(sorted(products.items(), key=lambda x: x[1]["price"]))

print(sorted_products)
```

---

# Key Idea

Nested dictionary sorting pattern:

```
sorted(dict.items(), key=lambda x: x[1]["field"])
```