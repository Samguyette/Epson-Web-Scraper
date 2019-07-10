#!/usr/bin/python
# File: Epson_WS_V1.py
# Name: Samuel Guyette
# Desc: Pulls data from numerous websites to compare pricing of T-series competitors.
#		Will output a .csv file to location of program.
# Other files required: helper_functions.py, product_class.py, lists.py

import string
import datetime

#xlsx
import os
import glob
import csv
import openpyxl
import pandas as pd

#import object class
from product_class import Product

#import helper function
from helper_functions import build_data_set

#import lists
from lists import *


def append_category(f, product_set, category, green_words, red_words):
	#picks correct category
	for product in product_set:
		write = True

		if product.added:
			write = False

		for word in red_words:
			if word in product.name:
				write = False

		if write:
			for substring in green_words:
				if substring in product.name and not product.added:
					f.write(product.channel + "," + product.country + "," + product.website + "," + product.company + "," + category + ",")
					f.write(product.name + "," + product.id + ", " + product.price + "," + product.shipping + "\n")
					product.added = True


def build_condensed_table(f, product_set):
	header = ",Website,"
	for i in sku_targets:
		header = header + i + ","
	f.write(header+"\n")

	for website in website_targets:
		#write country
		line = ""
		if "(CA)" in website:
			line += "CA,"
			website = website.replace(' (CA)','')
		else:
			line += "US,"
		line += website+","
		for sku in sku_targets:
			product_found = False
			for product in product_set:
				if product.id == sku and product.website == website and not product_found:
					line += product.price
					#check if lowest sales price is correct
					try:
						lsp = price_target_hash[sku]
						price = product.price
						try:
							price = price.split('.', 1)[0]
						except:
							pass
						price = price.replace('$','')
						price = int(price)
						if price < lsp:
							line = line+" L "
						if price > lsp:
							line = line+" H "
					except:
						pass

					if "Free" in product.shipping:
						line += "*,"
					else:
						line += ","

					product_found = True

			if not product_found:
				line += ","

		f.write(line+"\n")



# ****MAIN**** #
def main():
	#opens connection
	filename = "Comparison_T-Series_ouput.csv"
	f = open(filename, "w")

	#hash set for all product objects
	product_set = set()
	build_data_set(product_set)
	print(str(len(product_set))+" potential products gathered.\n")
	#Writes name
	f.write("Created by Sam Guyette\n")

	#Writes date and time of when ran
	now = datetime.datetime.now()
	f.write("Date and time of script execution: "+now.strftime("%Y-%m-%d %H:%M:%S")+"\n\n")

	#builds condensed table
	print("Building condensed table...\n")
	title = "Condensed Table\n*Free Shipping\n"
	f.write(title)
	build_condensed_table(f, product_set)
	space = "\n\n\n\n\n"
	f.write(space)
	print("Finished building and writing condensed table.\n")

	#write headers for super table
	title = "Super Table\n"
	f.write(title)
	headers = "Channel, Country, Website, Company, Category, Name, SKU, Price, Shipping\n"
	f.write(headers)

	#creates sub categories
	print("Writing all data to super table...\n")
	#builds super table
	append_category(f, product_set, "Printer", printer_include_list, printer_exclude_list)
	append_category(f, product_set, "Ink", ink_include_list, ink_exclude_list)
	append_category(f, product_set, "Accessory", accessories_include_list, accessories_exlude_list)

	#convert .csv file to .xlsv
	wb = openpyxl.Workbook()
	ws = wb.active
	with open(filename, 'rt') as f:
		reader = csv.reader(f)
		for r, row in enumerate(reader, start=1):
			for c, val in enumerate(row, start=1):
				ws.cell(row=r, column=c).value = val
	wb.save("Comparison_T-Series_ouput.xlsx")

	#Change letters to highlights

	# new = pd.read_excel(filename + '.xlsx')
	#
	# writer = pd.ExcelWriter(new, engine='xlsxwriter')
	#
	# new.conditional_format('A1:ZZ1000', {'type': 'text',
	# 										'criteria': 'containing',
	# 										'value':' H ',
	# 										'format': highlight_fmt})

	print("Intern work is now complete.\n")

	f.close()


if __name__ == '__main__':
	main()













#
