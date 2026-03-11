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
