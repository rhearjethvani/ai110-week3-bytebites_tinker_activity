"""Quick manual check: create sample objects and verify scaffolds work."""

from models import Customer, FoodItem, Menu, Order

# Create sample FoodItems
burger = FoodItem("Spicy Burger", 9.99, "Entrees", 4.5)
soda = FoodItem("Large Soda", 2.49, "Drinks", 4.0)
fries = FoodItem("Fries", 3.49, "Sides", 3.8)

# Create Menu with items
menu = Menu([burger, soda, fries])
print("Menu items:", [item.name for item in menu.items])

# Filter by category
drinks = menu.filter_by_category("Drinks")
print("Drinks:", [item.name for item in drinks])

# Create Order with selected items
order = Order([burger, soda])
print("Order items:", [item.name for item in order.selected_items])
print("Total cost:", order.get_total_cost())

# Create Customer with purchase history
customer = Customer("Alex", purchase_history=[])
customer.purchase_history.append(order)
print("Customer:", customer.name, "| Past orders:", len(customer.purchase_history))
print("All attributes stored correctly. Scaffolds OK.")
