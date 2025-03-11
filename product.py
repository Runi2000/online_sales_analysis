class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"\nProizvod: {self.name}\n"
                   f"Cena: {self.price}€\n"
                   f"Količina: {self.quantity}\n")
        
    def update_quantity(self, quantity):
        self.quantity = quantity