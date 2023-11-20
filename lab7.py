# class Book:
#     def __init__(self, book_title, book_author, book_isbn):
#         self.title = book_title
#         self.author = book_author
#         self.isbn = book_isbn

# book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
# book2 = Book("To Kill a Mockingbird", "Harper Lee", "0061120081")
# book3 = Book("1984", "George Orwell", "0451524934")

# print("Информация о книге 1:")
# print(f"Название: {book1.title}")
# print(f"Автор: {book1.author}")
# print(f"ISBN: {book1.isbn}")
# print()

# print("Информация о книге 2:")
# print(f"Название: {book2.title}")
# print(f"Автор: {book2.author}")
# print(f"ISBN: {book2.isbn}")
# print()

# print("Информация о книге 3:")
# print(f"Название: {book3.title}")
# print(f"Автор: {book3.author}")
# print(f"ISBN: {book3.isbn}")

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def display_car(self):
#         return f"Car: {self.year} {self.make} {self.model}"

# my_car = Car("Toyota", "Corolla", 2022)
# print(my_car.display_car())

# class Car:
#     def __init__(self, make, model, year, color, mileage):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.color = color
#         self.mileage = mileage

#     def display_car(self):
#         return f"Car: {self.year} {self.make} {self.model}, Color: {self.color}, Mileage: {self.mileage} miles"
# car1 = Car("Toyota", "Corolla", 2022, "Red", 15000)
# car2 = Car("Honda", "Civic", 2020, "Blue", 20000)
# car3 = Car("Ford", "Mustang", 2023, "Black", 5000)
# print(car1.display_car())
# print(car2.display_car())
# print(car3.display_car())

# class Car:
#     def __init__(self, make, model, year, color, mileage):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.color = color
#         self.mileage = mileage
#     def display_car(self):
#         return f"Car: {self.year} {self.make} {self.model}, Color: {self.color}, Mileage: {self.mileage} miles"
#     def drive(self, distance):
#         self.mileage += distance
#         print(f"New mileage after driving: {self.mileage} miles")
# car1 = Car("Toyota", "Corolla", 2022, "Red", 15000)
# print("Before driving:")
# print(car1.display_car())
# car1.drive(1000)
# print("\nAfter driving:")
# print(car1.display_car())

# class Car:
#     def __init__(self, make, model, year, color, mileage):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.color = color
#         self.mileage = mileage
#     def display_car(self):
#         return f"Car: {self.year} {self.make} {self.model}, Color: {self.color}, Mileage: {self.mileage} miles"

# class ElectricCar(Car):
#     def __init__(self, make, model, year, color, mileage, battery_size):
#         super().__init__(make, model, year, color, mileage)
#         self.battery_size = battery_size
#     def describe_battery(self):
#         print(f"Battery size: {self.battery_size} kWh")
# my_electric_car = ElectricCar("Tesla", "Model S", 2023, "Black", 10000, 75)
# print(my_electric_car.display_car())
# my_electric_car.describe_battery()

# class InventorySystem:
#     def __init__(self):
#         self.inventory = []
#     def add_item(self, name, quantity, description):
#         item = {"name": name, "quantity": quantity, "description": description}
#         self.inventory.append(item)
#     def display_inventory(self):
#         print("Inventory:")
#         for item in self.inventory:
#             print(f"Name: {item['name']}, Quantity: {item['quantity']}, Description: {item['description']}")
#         print("\n")
#     def change_quantity(self, name, new_quantity):
#         for item in self.inventory:
#             if item['name'] == name:
#                 item['quantity'] = new_quantity
#                 print(f"Quantity of {name} changed to {new_quantity}")
#                 return
#         print(f"{name} not found in inventory")
# inventory_system = InventorySystem()
# inventory_system.add_item("Laptop", 10, "Brand new laptops")
# inventory_system.add_item("Monitor", 20, "High-resolution monitors")
# inventory_system.add_item("Keyboard", 30, "Mechanical keyboards")
# inventory_system.display_inventory()
# inventory_system.change_quantity("Laptop", 15)
# inventory_system.display_inventory()
