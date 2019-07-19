#!/usr/bin/env python
# File: product_class.py
# Name: Samuel Guyette
# Desc: Object class for Epson_WS_V1.py
# Other files required: Epson_WS_V1.py
class Product:
        def __init__(self, channel, country, website, company, name, id, price, shipping):
            self.channel = channel
            self.country = country
            self.website = website
            self.company = company
            self.name = name
            self.id = id
            self.price = price
            self.added = False
            self.sku_change = False
            self.shipping = shipping
