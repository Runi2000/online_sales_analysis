# Importovanje klasa
from product import Product
from product_manager import ProductManager
from cart import Cart
import random

manager = ProductManager()
cart = Cart()

# Lista produkata
products = [
    Product("Vešmašina", 539.99, 6),
    Product("Rukavice", 5.60, 110),
    Product("Saksija", 15, 13),
    Product("Čizme", 24.30, 78),
    Product("Kosilica", 850, 3),
    Product("TV", 539.99, 43),
    Product("Slušalice", 5.60, 20),
    Product("Miš", 15, 54),
    Product("Tastatura", 24.30, 50),
    Product("Računar", 850, 10)
    ]

# Dodavanje proizvoda u ProductManager kalsu
for product in  products:
    manager.add_products(product)

# Ispis za proizvode
manager.display_products()

# Ispis ukupne cene proizvoda
total_value = manager.total_value()
print(f"\nUkupna vrednost proizvoda: {total_value}€\n")

# Nasumično biranje proizvoda u korpu
random_products = random.sample(manager.products, 3)
for product in random_products:
    cart.add_to_cart(product)

# Ispis proizvoda u korpi
print("Kupac kupuje sledeće proizvode:\n")
cart.display_cart()

# Ukupna cena proizvoda u korpi
total_cart_value = cart.total_cart_value()
print(f"\nUkupna vrednost proizvoda za platiti: {total_cart_value}€\n")