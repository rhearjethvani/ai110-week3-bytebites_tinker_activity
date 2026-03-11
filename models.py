"""
ByteBites Backend Models

Four classes:
- Customer: Tracks name and purchase history for user verification
- FoodItem: Individual item (name, price, category, popularity rating)
- Menu: Collection of food items with category filtering
- Order: Transaction holding selected items and total cost
"""


class Customer:
    """Tracks customer name and past purchase history for verification."""

    def __init__(self, name, purchase_history=None):
        self.name = name
        self.purchase_history = purchase_history if purchase_history is not None else []


class FoodItem:
    """A single food item (e.g., Spicy Burger, Large Soda)."""

    def __init__(self, name, price, category, popularity_rating):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Menu:
    """Digital list of all food items with category filtering."""

    def __init__(self, items=None):
        self.items = items if items is not None else []

    def filter_by_category(self, category):
        """Return items matching the given category (e.g., Drinks, Desserts)."""
        return [item for item in self.items if item.category == category]


class Order:
    """Single transaction grouping selected items; computes total cost."""

    def __init__(self, selected_items=None):
        self.selected_items = selected_items if selected_items is not None else []

    def get_total_cost(self):
        """Compute total cost of selected items."""
        return sum(item.price for item in self.selected_items)


if __name__ == "__main__":
    # Manual test: exercises filtering, total calculation, and full workflow

    # Add items to menu
    burger = FoodItem("Spicy Burger", 9.99, "Entrees", 4.5)
    soda = FoodItem("Large Soda", 2.49, "Drinks", 4.0)
    fries = FoodItem("Fries", 3.49, "Sides", 3.8)
    dessert = FoodItem("Chocolate Cake", 5.99, "Desserts", 4.2)

    menu = Menu([burger, soda, fries, dessert])

    # Filter by category
    drinks = menu.filter_by_category("Drinks")
    desserts = menu.filter_by_category("Desserts")
    assert len(drinks) == 1 and drinks[0].name == "Large Soda"
    assert len(desserts) == 1 and desserts[0].name == "Chocolate Cake"

    # Compute order total
    order = Order([burger, soda, fries])
    total = order.get_total_cost()
    expected = 9.99 + 2.49 + 3.49
    assert abs(total - expected) < 0.01, f"Expected {expected}, got {total}"

    # Customer with purchase history
    customer = Customer("Jordan", purchase_history=[order])
    assert customer.name == "Jordan"
    assert len(customer.purchase_history) == 1
    assert customer.purchase_history[0].get_total_cost() == total

    print("All manual tests passed.")
