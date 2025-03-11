class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

# Funkcija za ispis proizvoda
    def display_info(self):
        print(f"\nProizvod: {self.name}\n"
                   f"Cena: {self.price}€\n"
                   f"Količina: {self.quantity}")

# Funkcija za ažuriranje količine proizvoda        
    def update_quantity(self, quantity):
        self.quantity = quantity