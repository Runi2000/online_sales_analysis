from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_products(self, product):
        self.products.append(product)

    def display_products(self):
        for product in self.products:
            product.display_info()

    def total_value(self):
        total_value = sum(product.price * product.quantity for product in self.products)
        return total_value