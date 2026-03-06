# 80. Dictionary Value Search: Given a dictionary of items and their prices, write a Python program to search for an item based on its price and print the item’s name.

items = {
    "apple": 100,
    "banana": 60,
    "orange": 80
}

search_price = int(input("Enter price to search: "))

for item, price in items.items():
    if price == search_price:
        print("Item with this price:", item)