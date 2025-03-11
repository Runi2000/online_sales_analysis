from product import Product

class Cart:
    def __init__(self, cart_items):
        self.cart_items = []

    def add_to_cart(self, product):
        self.cart_items.append(product)

    def total_cart_value(self):
        total_value = sum(product.price * product.quantity for product in self.cart_items)
        return total_value
    
    def display_cart(self):
        for product in self.cart_items:
            product.display_info()