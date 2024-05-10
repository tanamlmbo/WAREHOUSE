from tabulate import tabulate # paste "pip install tabulate" on your terminal to install tabulate


class Shoe: #Shoe
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"Code: {self.code}, Product: {self.product}, Quantity: {self.quantity}, Cost: {self.cost:.2f}"


def read_shoes_data(file_name):
    shoes_storage = []
    try:
        with open(file_name, "r") as file:
            next(file)
            for line in file:
                data = line.strip().split(",")
                country, code, product, cost, quantity = data
                shoes_storage.append(Shoe(country, code, product, cost, quantity))
    except FileNotFoundError:
        print(f"File {file_name} not found.")
    return shoes_storage


def capture_shoes():
    country = input("Enter country: ")
    code = input("Enter the code: ")
    product = input("Enter the product: ")
    cost = float(input("Enter the cost: "))
    quantity = int(input("Enter the quantity: "))
    return Shoe(country, code, product, cost, quantity)


def view_all(shoes_storage):
    headers = ["Code", "Product", "Quantity", "Cost"]
    data = [[shoe.code, shoe.product, shoe.quantity, f"R{shoe.cost:.2f}"] for shoe in shoes_storage]
    print(tabulate(data, headers=headers, tablefmt="grid"))


def re_stock(shoes_storage):
    lowest_quantity_shoe = min(shoes_storage, key=lambda shoe: shoe.quantity)
    print(f"Lowest quantity shoe: {lowest_quantity_shoe}")
    add_quantity = int(input("Enter quantity to restock: "))
    lowest_quantity_shoe.quantity += add_quantity
    print(f"Restocked {add_quantity} units for {lowest_quantity_shoe.product}"
          f". New quantity: {lowest_quantity_shoe.quantity}")


def search_shoe(shoes_storage, code):
    for shoe in shoes_storage:
        if shoe.code == code:
            return shoe
    return None


def value_per_item(shoes_storage):
    print("Value per item:")
    for shoe in shoes_storage:
        value = shoe.cost * shoe.quantity
        print(f"Product: {shoe.product}, Value: R{value:.2f}")


def highest_qty(shoes_storage):
    highest_quantity_shoe = max(shoes_storage, key=lambda shoe: shoe.quantity)
    print(f"Product with highest quantity: {highest_quantity_shoe}")


def main():
    shoes_storage = read_shoes_data("inventory.txt")

    while True:
        print("\nMenu:")
        print("1. Capture Shoe")
        print("2. View All Shoes")
        print("3. Re-Stock Shoes")
        print("4. Search Shoe by Code")
        print("5. Calculate Value per Item")
        print("6. Product with Highest Quantity")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            new_shoe = capture_shoes()
            shoes_storage.append(new_shoe)
        elif choice == "2":
            view_all(shoes_storage)
        elif choice == "3":
            re_stock(shoes_storage)
        elif choice == "4":
            code = input("Enter code to search: ")
            shoe = search_shoe(shoes_storage, code)
            if shoe:
                print(shoe)
            else:
                print("Shoe not found.")
        elif choice == "5":
            value_per_item(shoes_storage)
        elif choice == "6":
            highest_qty(shoes_storage)
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()

