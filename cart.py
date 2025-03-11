from product import Product

class Cart:
    def __init__(self):
        self.cart_items = []
    def add_to_cart(self, product):
        self.cart_items.append(product)

# Funkcija za ukupnu vrednost proizvoda u korpi
    def total_cart_value(self):
        total_value = sum(product.price * product.quantity for product in self.cart_items)
        return total_value
    
# Funkcija za ispis proizvoda u korpi
    def display_cart(self):
            for product in self.cart_items:
                print(product.name)