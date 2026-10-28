class Queue:
    def __init__(self):
        self.customers = []

    def enqueue(self, customer):
        self.customers.append(customer)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("The queue is empty.")
        return self.customers.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("The queue is empty.")
        return self.customers[0]

    def is_empty(self):
        return len(self.customers) == 0

    def display(self):
        if self.is_empty():
            print("The queue is empty.")
        else:
            print("Customers in queue:", " -> ".join(self.customers))


def main():
    customer_queue = Queue()

    while True:
        print("\nCustomer Queue")
        print("1. Add a customer")
        print("2. Serve the next customer")
        print("3. Show the next customer")
        print("4. Show all customers")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            customer = input("Enter the customer name: ").strip()
            if customer:
                customer_queue.enqueue(customer)
                print(f"{customer} has been added to the queue.")
            else:
                print("Customer name cannot be empty.")
        elif choice == "2":
            try:
                customer = customer_queue.dequeue()
                print(f"Now serving: {customer}")
            except IndexError as error:
                print(error)
        elif choice == "3":
            try:
                print(f"Next customer: {customer_queue.peek()}")
            except IndexError as error:
                print(error)
        elif choice == "4":
            customer_queue.display()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
