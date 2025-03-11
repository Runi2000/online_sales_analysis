from product import Product
from product_manager import ProductManager

manager = ProductManager()

products = [
    Product("TV", 539.99, 43),
    Product("Slušalice", 5.60, 20),
    Product("Miš", 15, 54),
    Product("Tastatura", 24.30, 50),
    Product("Računar", 850, 10)
]

for product in  products:
    manager.add_products(product)

manager.display_products()

total_value = manager.total_value()
print(f"Ukupna vrednost proizvoda: {total_value}€\n")