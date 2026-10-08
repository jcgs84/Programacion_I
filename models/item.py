class Item:
    def __init__(self, name, description, price):
        
        self.set_name(name)
        self.description = description
        self.set_price(price)

    def get_name(self):
        return self._name

    def set_name(self, name):
        if (name != ""):
            self._name = name
        else:
            raise ValueError("El nombre no puede estar vacío")

    def get_price(self):
        return self._price

    def set_price(self, price):
        if (price > 0):
            self._price = price
        else:
            raise ValueError("El precio debe ser mayor a cero")   
    def show_info(self):
        return f"{self.get_name()} - Descripción: {self.description} - Precio: self.get_price():.2f}"