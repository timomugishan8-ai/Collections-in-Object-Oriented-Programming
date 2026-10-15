###COLLECTIONS IN OOP PRACTICE###

stock= {
    "W001": ("Rolex Submariner", 1500),
    "W002": ("Casio G-Shock", 120),
    "S001": ("Nike Air Max", 90),
    "S002": ("Adidas Yeezy", 200),
    "S003": ("Rolex Submariner", 1500)
}

daily_orders = ["W001", "S001", "W001", "S002", "S001", "S001", "W002"]

#Question 1
name, price = stock["S002"]
print(f"{name} costs ${price}")

#If you tried 'stock["W001"][0] = "Rolex Dayonta", you would get a TypeError because tuples are immutable. 
# You cannot change their elements after they are created.

#Question 2i)
ordered_products = {stock[order_id][0] for order_id in daily_orders}
print("Unique products ordered:", ordered_products)

#Question 2ii)
stock_keys = set(stock.keys())
ordered_keys = set(daily_orders)
not_ordered_keys = stock_keys - ordered_keys
print("Stock codes not ordered:", not_ordered_keys)

ordered_product_names = {stock[order_id][0] for order_id in ordered_keys}
not_ordered_product_names = {
    stock[order_id][0] for order_id in not_ordered_keys
} - ordered_product_names
print("Product names never ordered:", not_ordered_product_names)

#Question 3i)
stock.update({
    "S004": ("Puma RS", 110)
    })

#Question 3ii)
order_count = {}
for product_id in daily_orders:
    order_count[product_id] = order_count.get(product_id, 0) + 1

print("Order count:", order_count)

#Question 3iii)
total_sales = sum(
    count * stock[product_id][1]
    for product_id, count in order_count.items()
)
print(f"Total sales for the day: ${total_sales:,.2f}")

