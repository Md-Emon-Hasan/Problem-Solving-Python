# 90. Nested Dictionary Sorting: Given a nested dictionary containing product details (product name, price, and quantity), write a Python program to sort the products based on their prices in ascending order.

products = {
    "p1": {"name": "Laptop", "price": 800, "quantity": 5},
    "p2": {"name": "Phone", "price": 500, "quantity": 10},
    "p3": {"name": "Tablet", "price": 300, "quantity": 7}
}

sorted_products = dict(sorted(products.items(), key=lambda x: x[1]["price"]))

print("Sorted products:", sorted_products)