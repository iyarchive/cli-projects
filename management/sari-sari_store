import json
from pathlib import Path

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def to_dict(self):
        return {
            "price": self.price,
            "stock": self.stock,
        }

    def restock(self, amount):
        if amount < 0:
            raise ValueError("Restock amount must not be negative.")
        self.stock += amount

    def deduct_stock(self, amount):
        if amount < 0:
            raise ValueError("Deduction amount must not be negative.")
        if amount > self.stock:
            raise ValueError("Not enough stock available.")
        self.stock -= amount


base_dir = Path(__file__).resolve().parent
data_dir = base_dir / "data"
inventory_file = data_dir / "inventory.json"
customers_file = data_dir / "customers.json"

data_dir.mkdir(exist_ok=True)


def load_data(file_path):
    if file_path.exists() and file_path.stat().st_size > 0:
        with file_path.open("r", encoding="utf-8") as file:
            return json.load(file)
    return {}


def save_data(file_path, data):
    with file_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def add_product(inventory):
    while True: 
        name = input("Enter product name: ").strip().lower()

        if not name:
            print("Product name cannot be empty.")
            continue

        if name in inventory:
            print("Product already exists.")
            continue
        
        break

    while True:
        try:
            price = float(input("Enter product price: ").strip())
            stock = int(input("Enter starting stock: ").strip())
        except ValueError:
            print("Invalid price or stock.")
            continue

        if price < 0 or stock < 0:
            print("Price and stock must not be negative.")
            continue

        break

    inventory[name] = {
        "price": price,
        "stock": stock,
    }

    save_data(inventory_file, inventory)
    print(f"{name} added successfully.")


def view_products(inventory):
    if not inventory:
        print("Inventory is empty.")
        return

    print("\nCurrent inventory:")
    for name, details in inventory.items():
        print(f"- {name}: ₱{details['price']:.2f}, stock = {details['stock']}")


def main():
    inventory = load_data(inventory_file)
    customers = load_data(customers_file)
    
    print("Inventory:", inventory)
    print("Customers:", customers)

    while True:
        add_product(inventory)

        while True:
            try:
                new_product = int(input("Would you like to add another product?\n"
                                        "Press 1 for yes, 2 for no: "))
            except ValueError:
                print("Enter only 1 or 2.")
                continue

            if new_product == 1:
                break
            elif new_product == 2:
                view_products(inventory)
                return
            else:
                print("Enter only 1 or 2.")

if __name__ == "__main__":
    main()
