# File: lists.py
# Name: Samuel Guyette
# Desc:  Helper functions for main

#import scraping tools
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re

#import object class
from product_class import Product

#import data lists
from lists import staples_urllist
from lists import newegg_urllist
from lists import bh_urllist
from lists import walmart_urllist
from lists import epson_urllist
from lists import buyvpc_urllist
from lists import company_list
from lists import remove_list


#loops urls lists through specific scraper
def build_data_set(product_set):
	#loop raw searches
	for url in staples_urllist:
		pull_staples(url, product_set)

	for url in newegg_urllist:
		pull_newegg(url, product_set)

	#for url in bh_urllist:
	#	pull_bh(url, product_set)

	for url in walmart_urllist:
		pull_walmart(url, product_set)

	#for url in epson_urllist:
	#	pull_epson(url, product_set)

	#for url in buyvpc_urllist:
	#	pull_buyvpc(url, product_set)


# *** Website specific scrapers *** #
def pull_buyvpc(url, product_set):
	#check if broken
	try:
	    #opening connection
		uClient = uReq(url)
		page_html = uClient.read()
		uClient.close()
		#html parsing
		page_soup = soup(page_html,"html.parser")
		#finds data on page
		name = page_soup.find("h2",{"itemprop":"name"}).text
		price = page_soup.find("div",{"class":"price"}).text
		price = butcher(price)
		price = ''.join([i for i in price if i.isdigit() or "."])
		price = price.split(".", 1)[0]
		price = price.split("$", 1)[1]
		price = "$"+price

		add_element("BuyVPC", "", name, price, "No_Data", product_set)

	except:
		print("www.newegg.com pipe is now broken.")



def pull_epson(url, product_set):
	#check if broken
	try:
		#opening connection
		uClient = uReq(url)
		page_html = uClient.read()
		uClient.close()
		#html parsing
		page_soup = soup(page_html,"html.parser")
		#finds all products on current page
		containers = page_soup.findAll("div",{"class":"product-info"})

		if len(containers) == 0:
			print("Epson containers produced zero products.")

		for container in containers:
			name = (container.find("a",{"class":"name"}).text) + " Printer"
			price = container.find("div",{"class":"amount"}).text

			if "epson.ca" in url:
				add_element("Epson", "Epson.ca", name, "CAD "+price, "No_Data", product_set)
			else:
				add_element("Epson", "Epson (US)", name, price, "No_Data", product_set)

	except:
		print("www.epson.com pipe is now broken.")



def pull_walmart(url, product_set):
	#check if broken
	try:
		#opening connection
		uClient = uReq(url)
		page_html = uClient.read()
		uClient.close()
		#html parsing
		page_soup = soup(page_html,"html.parser")
		#finds all products on current page
		container = page_soup.find("div",{"class":"hf-Bot hf-PositionedRelative"})

		if len(container) == 0:
			print("Walmart containers produced zero products.")

		try:
			name = container.find("div",{"class":"ProductTitle"}).text
			try:
				shipping = container.find("div",{"class":"font-semibold free-shipping-msg"}).text
			except:
				shipping = "No_Data"

			#trys different html specs for pricing
			try:
				price_list = container.findAll("span",{"itemprop":"price"})
				price = "Price range: $"+price_list[0].text+" - to"+price_list[1].text
			except:
				price = container.find("span", {"class":"price display-inline-block arrange-fit price price--stylized"}).text

		except:
			name = ""
			price = ""

		add_element("Walmart", "", name, price, shipping, product_set)

	except:
		print("www.walmart.com pipe is now broken.")



def pull_bh(url, product_set):
	#check if broken
	try:
		#opening connection
		uClient = uReq(url)
		page_html = uClient.read()
		uClient.close()
		#html parsing
		page_soup = soup(page_html,"html.parser")
		#finds all products on current page
		text_containers = page_soup.findAll("div",{"data-selenium":"itemDetail"})
		price_containers = page_soup.findAll("div",{"class":"price-zone"})
		shipping_containers = page_soup.findAll("div",{"class":"salesComments scShipNote sect clearfix c2 bold"})

		for tcontainer, pcontainer, scontainer in zip(text_containers, price_containers, shipping_containers):
			name = tcontainer.find("span",{"itemprop":"name"}).text
			company = tcontainer.find("span",{"itemprop":"brand"}).text
			try:
				price = pcontainer.find("span",{"class":"itc-you-pay-price bold"}).text
			except:
				price = "Missing price"
			try:
				shipping = scontainer.text
				shipping = ' '.join([w for w in shipping.split() if len(w)<9])
			except:
				shipping = "Missing shipping"

			add_element("B&H", company, name, price, shipping, product_set)

	except:
		print("www.bhphotovideo.com pipe is now broken.")



def pull_newegg(url, product_set):
	#check if broken
	try:
		#opening connection
		uClient = uReq(url)
		page_html = uClient.read()
		uClient.close()
		#html parsing
		page_soup = soup(page_html,"html.parser")
		#finds all products on current page
		containers = page_soup.findAll("div",{"class":"item-container"})

		if len(containers) == 0:
			print("NewEgg containers produced zero products.")

		for container in containers:
			try:
				name = container.find("a",{"class":"item-title"}).text
				price = "$"+container.find("li",{"class":"price-current"}).strong.text
				shipping = container.find("li",{"class":"price-ship"}).text
			except:
				name = ""
				price = ""
				shipping = ""


			add_element("NewEgg", "", name, price, shipping, product_set)

	except:
		print("www.newegg.com pipe is now broken.")



def pull_staples(url, product_set):
	#check if broken
	try:
		#opening connection
		uClient = uReq(url)
		page_html = uClient.read()
		uClient.close()
		#html parsing
		page_soup = soup(page_html,"html.parser")
		#finds all products on current page
		containers = page_soup.findAll("div",{"class":"standard-type__large_product_tile"})

		if len(containers) == 0:
			print("Staples containers produced zero products.")

		for container in containers:
			name = container.div.div.a["title"]
			price = container.find("span",{"class":"standard-type__price"}).text

			add_element("Staples", "", name, price, "No_Data", product_set) #no shipping data

	except:
		print("www.staples.com pipe is now broken.")




#If correct product, object is created and added to product set
def add_element(store, company, name, price, shipping, product_set):
	name = butcher(name)
	price = butcher(price)
	shipping = butcher(shipping)

	#find which comapny the product belongs to
	for i in company_list:
		if i[0] in name:
			company = i[1]

	#check if name contains banned word list
	banned = False
	for checker in remove_list:
		if checker in name:
			banned = True

	#create product object
	if not banned:
		new_product = Product(store, company, name, price, shipping)
		product_set.add(new_product)


#breaks up strings
def butcher(str):
	str = re.sub(r'\W+ ', '', str)
	str = str.replace(',','')
	str = str.replace('\n', '')
	str = str+" "
	return str
