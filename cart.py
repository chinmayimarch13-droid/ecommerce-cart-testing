class Cart:

    def __init__(self):
        self.items = []

    def add_item(self, price):
        if price <= 0:
            return "Invalid price"
        self.items.append(price)
        return "Item added"

    def remove_item(self, price):
        if price in self.items:
            self.items.remove(price)
            return "Item removed"
        return "Item not found"

    def calculate_total(self):
        return sum(self.items)

    def apply_discount(self, percent):
        if percent < 0 or percent > 100:
            return "Invalid discount"
        total = self.calculate_total()
        discount_amount = total * (percent / 100)
        return total - discount_amount
