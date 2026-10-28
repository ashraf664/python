product_names = []
product_prices = []

for i in range(5):
    name = input(f"Enter product #{i+1} name: ")
    price = float(input(f"Enter price of {name}: "))
    product_names.append(name)
    product_prices.append(price)

expensive_products = []
for i in range(5):
    if product_prices[i] > 50:
        expensive_products.append((product_names[i], product_prices[i]))

print("Products with price > 50:")
for name, price in expensive_products:
    print(name, "->", price)

max_price = product_prices[0]
max_index = 0
for i in range(1, 5):
    if product_prices[i] > max_price:
        max_price = product_prices[i]
        max_index = i

print("Most expensive product:")
print(product_names[max_index], "->", max_price)

for i in range(5):
    if product_prices[i] < 10:
        product_prices[i] = 10.0

print("Updated products and prices:")
for i in range(5):
   print(product_names[i], "->", product_prices[i])
