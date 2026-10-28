
def calculate_product_total(price, quantity):
    return price * quantity

def print_invoice(customer_name, products, subtotal, tax, total):
    print(f"\nHello, {customer_name}!")
    print("---- Here is your bill ----\n")
    print(f"{'Product':<12}{'Qty':<6}{'Unit Price':<12}{'Total'}")
    print("-" * 40)
    for p in products:
        print(f"{p['name']:<12}{p['quantity']:<6}{p['price']:<12.2f}{p['total']:.2f}")
    print("-" * 40)
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Tax (14%): {tax:.2f}")
    print(f"Total: {total:.2f}\n")

def handle_customer():
    customer_name = input("Enter your name: ")
    num_products = int(input("Enter the number of products: "))

    products = []
    subtotal = 0

    for i in range(num_products):
        print(f"\nProduct {i + 1}")
        name = input("Product name: ")
        quantity = int(input("Quantity: "))
        price = float(input("Unit price: "))
        total = calculate_product_total(price, quantity)
        subtotal += total
        products.append({
            "name": name,
            "price": price,
            "quantity": quantity,
            "total": total
        })

    tax = subtotal * 0.14
    final_total = subtotal + tax

    print_invoice(customer_name, products, subtotal, tax, final_total)

def main():
    while True:
        handle_customer()
        again = input("Do you want to enter details for another customer? (yes/no): ").strip().lower()
        if again == "no":
            print("Goodbye!")
        break
    return main()
main()