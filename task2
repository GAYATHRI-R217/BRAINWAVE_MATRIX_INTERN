import json
import getpass

class UserVerifier:
    def __init__(self):
        self.registered_users = {"user": "user333"}

    def authenticate(self, username, password):
        if username in self.registered_users and self.registered_users[username] == password:
            print("***Access granted***")
            return True
        else:
            print("Credentials do not match!!!")
            return False

class StockManager:
    def __init__(self):
        self.stock_items = {}

    def add_stock(self):
        item_type = input("\nEnter the stock's type: ")
        item_name = input("\nEnter stock name: ")
        if item_name in self.stock_items:
            print("Item already exists. Use update to modify!!!")
            return
        try:
            quantity = int(input(f"Enter quantity of {item_name}: "))
            price = float(input(f"Enter price per {item_name}: "))
            self.stock_items[item_name] = {"type": item_type, "quantity": quantity, "price": price}
            print(f"***{item_name} added to stock successfully***")
        except ValueError:
            print("Invalid input Quantity should be an integer and price should be a number.")

    def update_stock(self):
        item_name = input("\nEnter stock name to update: ")
        if item_name in self.stock_items:
            try:
                quantity = int(input(f"Enter new quantity for {item_name}: "))
                price = float(input(f"Enter new price for {item_name}: "))
                self.stock_items[item_name]["quantity"] = quantity
                self.stock_items[item_name]["price"] = price
                print(f"***{item_name} updated successfully***")
            except ValueError:
                print("Invalid input Quantity should be an integer and price should be a number!!!")
        else:
            print("Item not found in stock!!!")

    def remove_stock(self):
        item_name = input("\nEnter stock name to remove: ")
        if item_name in self.stock_items:
            del self.stock_items[item_name]
            print(f"***{item_name} removed from stock.***")
        else:
            print("Item not found in stock!!!")

    def view_stock(self):
        print("\nCurrent Stock Levels:")
        item_number = 1
        for item, details in self.stock_items.items():
            print(f"{item_number}. {item} ({details['type']}): {details['quantity']} available at Rs {details['price']} each")
            item_number += 1
        print("\n***stock review completed***")

    def low_stock_warning(self):
        print("\nLow Stock Warnings (Less than 5 items):")
        low_stock_count = sum(1 for item, details in self.stock_items.items() if details["quantity"] < 5)
        if low_stock_count == 0:
            print("No low stock items at this time.")
            return
        for item, details in self.stock_items.items():
            if details["quantity"] < 5:
                print(f"{item}: Only {details['quantity']} left!")

    def sales_report(self):
        print("\nSales Report:")
        total_revenue = 0
        for item, details in self.stock_items.items():
            revenue = details["quantity"] * details["price"]
            total_revenue += revenue
            print(f"{item}: Rs {revenue} total revenue")
        print(f"\nTotal Revenue: Rs {total_revenue}")

    def save_stock(self, filename="stock.json"):
        with open(filename, "w") as f:
            json.dump(self.stock_items, f)
        print("Stock saved to file!")

    def load_stock(self, filename="stock.json"):
        try:
            with open(filename, "r") as f:
                self.stock_items = json.load(f)
            print("Stock loaded from file!")
        except FileNotFoundError:
            print("No previous stock data found. Starting fresh.")

# Main Program
authenticator = UserVerifier()
username = input("Enter your username: ")
password = input("Enter your password: ")

if authenticator.authenticate(username, password):
    stock_manager = StockManager()
    stock_manager.load_stock()

    while True:
        print("\nStock Management System")
        print("1. Add Stock")
        print("2. Update Stock")
        print("3. Remove Stock")
        print("4. View Stock")
        print("5. Low Stock Warnings")
        print("6. Sales Report")
        print("7. Save & Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            stock_manager.add_stock()
        elif choice == "2":
            stock_manager.update_stock()
        elif choice == "3":
            stock_manager.remove_stock()
        elif choice == "4":
            stock_manager.view_stock()
        elif choice == "5":
            stock_manager.low_stock_warning()
        elif choice == "6":
            stock_manager.sales_report()
        elif choice == "7":
            stock_manager.save_stock()
            print("***Exiting... See you later!***")
            break
        else:
            print("Invalid choice Please enter a valid option!!!")
