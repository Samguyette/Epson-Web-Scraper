# File: Epson_WS_V1.py
# Name: Samuel Guyette
# Desc: Pulls data from numerous websites to compare pricing of T-series competitors.
#		Will output a .csv file to location of program.
# Other files required: product_class.py

import string
import datetime

#import object class
from product_class import Product

#import helper function
from helper_functions import build_data_set



def append_category(category, substrings, red_words):
	#picks correct category
	for product in product_set:
		write = True

		if product.added:
			write = False

		for word in red_words:
			if word in product.name:
				write = False;

		if write:
			for substring in substrings:
				if substring in product.name and not product.added:
					f.write(product.website + "," + product.company + "," + category + "," + product.name + "," + product.id + ", " + product.price + "," + product.shipping + "\n")
					product.added = True;


# ****MAIN**** #
if __name__ == '__main__':
    #opens connection
    filename = "Comparison_T-Series.csv"
    f = open(filename, "w")

    #hash set for all product objects
    product_set = set()
    build_data_set(product_set);

    #Writes name
    f.write("Created by Sam Guyette\n")

    #Writes date and time of when ran
    now = datetime.datetime.now()
    f.write("Date and time of script execution: "+now.strftime("%Y-%m-%d %H:%M:%S")+"\n\n")

    #write header
    headers = "Website, Company, Category, Name, SKU, Price, Shipping\n"
    f.write(headers)

    #creates sub categories
    append_category("Printer", ["Printer", "printer"], ["Spindle","Cyan", "Magenta", "Tank", "Kit", "Pad", "Plan", "Service"]);
    append_category("Ink", ["Ink"], ["Bottles","Tank"]);
    append_category("Accessory", ["Spindle","Tank", "Bottles", "Maintenance", "Kit", "Pad", "Plan", "Service"], [])

    f.close()


















#
