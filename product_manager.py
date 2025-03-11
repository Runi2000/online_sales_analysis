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
    
    def remove_product(self, name):
        product_to_remove = None
        for product in self.products:
            if product.name == name:
                break
        if product_to_remove:
            self.products.remove(product_to_remove)
            print(f"Proizvod {name} je uklonjen.\n")
        else:
            print(f"Proizvod {name} nije pronađen.\n")