# File: product_class.py
# Name: Samuel Guyette
# Desc: Object class for Epson_WS_V1.py
# Other files required: Epson_WS_V1.py
class Product:
        def __init__(self, website, company, name, price, shipping):
            self.website = website
            self.company = company
            self.name = name
            self.price = price
            self.added = False
            self.shipping = shipping
