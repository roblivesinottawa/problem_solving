def add_prices(basket):
    total = 0
    # this method will access the values of the dictionary items
    for item in basket.values():
        total += item
    return round(total, 2)  # round it to 2 decimal places


# create a groceries list using a dictionary
groceries = {
    "bananas": 2.00,
    "apples": 2.50,
    "oranges": 3.00,
    "bread": 0.99,
    "coffee": 6.99,
    "cheese": 5.99,
}

print(add_prices(groceries))
