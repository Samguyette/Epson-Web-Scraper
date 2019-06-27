# File: lists.py
# Name: Samuel Guyette
# Desc:  Helper functions for main

#import scraping tools
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
import string

#import object class
from product_class import Product

#import data lists
from lists import staples_urllist
from lists import newegg_urllist
from lists import bh_urllist
from lists import walmart_urllist
from lists import epson_urllist
from lists import buyvpc_urllist
from lists import dell_urllist
from lists import vistek_urllist
from lists import tastar_urllist
from lists import company_list
from lists import remove_list
from lists import overland_urllist;
from lists import pcnation_urllist


#helper function for build_data_set
def loop_site(urllist, func, product_set):
	for url in urllist:
		func(url, product_set)


#loops urls lists through specific scraper
def build_data_set(product_set):
	#loop raw searches
	loop_site(staples_urllist, pull_staples, product_set)
	loop_site(newegg_urllist, pull_newegg, product_set)
	loop_site(bh_urllist, pull_bh, product_set)
	loop_site(walmart_urllist, pull_walmart, product_set)
	loop_site(epson_urllist, pull_epson, product_set)
	loop_site(buyvpc_urllist, pull_buyvpc, product_set)
	loop_site(dell_urllist, pull_dell, product_set)
	loop_site(vistek_urllist, pull_vistek, product_set)
	loop_site(tastar_urllist, pull_tastar, product_set)
	loop_site(overland_urllist, pull_overland, product_set)
	loop_site(pcnation_urllist, pull_pcnation, product_set)

# *** Website specific scrapers *** #
def pull_pcnation(url, product_set):
	#check if broken
	try:
		#opening connection
		uClient = uReq(url)
		page_html = uClient.read()
		uClient.close()
		#html parsing
		page_soup = soup(page_html,"html.parser")
		#finds all products on current page
		containers = page_soup.findAll("div",{"class":"Allitems"})
		if len(containers) == 0:
			print("PCNation containers produced zero products.")

		for container in containers:
			#try:
			name = container.find("a",{"class":"itemtitle"}).text
			id = container.find("span",{"class":"partNums"}).text
			id = id.split('MFG#  ', 1)[1]
			price = container.find("div",{"class":"Iteminfo"}).text

			price = price.split('Our Price:', 1)[1]
			price = price.split('Y', 1)[0]
			price = price[2:]
			price = butcher(price)

			if "Add" in price:
				price = price.split('A', 1)[0]
			if "Free" in price:
				price = price.split('F', 1)[0]

			add_element("NSP", "PCNation", "", name, id, price, "", product_set)

	except:
		print("www.pcnation.com pipe is now broken.")




def pull_overland(url, product_set):
	#check if broken
	try:
		#opening connection
		uClient = uReq(url)
		page_html = uClient.read()
		uClient.close()
		#html parsing
		page_soup = soup(page_html,"html.parser")
		#finds all products on current page
		containers = page_soup.findAll("div",{"class":"elementor-widget-wrap"})
		namelist = []
		pricelist = []

		for container in containers:
			name = container.find("div",{"class":"elementor-widget-container"}).text
			name = butcher(name)

			if "Printer" not in name:
				name = name + "Printer"

			try:
				price = container.find("figcaption",{"class":"widget-image-caption wp-caption-text"}).text
			except:
				try:
					price = container.find("span",{"style":"text-decoration: line-through"}).text
				except:
					try:
						price = container.find("div",{"class":"elementor-text-editor elementor-clearfix"}).text
					except:
						price = "not"

			for i in company_list:
				if i[0] in name:
					namelist.append(name)


			if "$" in price:
				price = price.split('at', 1)[1]
				price = butcher(price)
				price = price.strip()
				if "Cash" in price:
					first = price.split('$', 2)[1]
					second = price.split('$', 2)[2]
					price = "$" + first + " plus (" + second[:-1] + ")"

				pricelist.append(price)

		for name, price in zip(namelist, pricelist):
			add_element("ISG", "Overland Blueprint", "", name, "", price, "", product_set)

	except:
		print("www.overlandblueprint.com pipe is now broken.")



def pull_tastar(url, product_set):
	#check if broken
	try:
		#opening connection
		uClient = uReq(url)
		page_html = uClient.read()
		uClient.close()
		#html parsing
		page_soup = soup(page_html,"html.parser")
		#finds all products on current page
		containers_1 = page_soup.findAll("tr",{"class":"productListing-odd"})
		containers_2 = page_soup.findAll("tr",{"class":"productListing-even"})

		full_containers = containers_1 + containers_2

		for container in full_containers:
			data = container.findAll("td",{"class":"productListing-data"})
			name = data[3].text
			name = name[1:]
			name = name[:-1]
			brand = data[1].text
			sku = data[2].text
			sku = sku[1:]
			sku = sku[:-1]
			price = data[5].text
			price = butcher(price)
			price = price.split('Price', 1)[1]
			price = price.split('Please', 1)[0]
			add_element("ISG", "Tartar Supply", brand, name, sku, price, "Free Shipping", product_set)


	except:
		print("www.tastarsupply.com pipe is now broken.")



def pull_vistek(url, product_set):
	#check if broken
	#try:
	#opening connection
	uClient = uReq(url)
	page_html = uClient.read()
	uClient.close()
	#html parsing
	page_soup = soup(page_html,"html.parser")
	#finds all products on current page
	name = page_soup.find("h1",{"class":"title"}).text
	price = page_soup.find("div",{"class":"card-body"}).text
	price = butcher(price)
	price = price.split('Qty', 1)[0]
	price = price.split('Your Price', 1)[1]

	try:
		shipping = page_soup.find("strong",{"class":"text-primary"}).text
	except:
		shipping = ""

	try:
		id = page_soup.find("ul",{"class":"list-unstyled"}).text
		id = id.split('Mfr: ', 1)[1]
		id = butcher(id)
		id = id.split('Free', 1)[0]
		id = id.upper()
	except:
		id = ""

	add_element("E-Commerce", "Vistek", "", name, id, price, shipping, product_set)

	#except:
	#	print("www.vistek.com pipe is now broken.")



def pull_dell(url, product_set):
	#check if broken
	try:
		#opening connection
		uClient = uReq(url)
		page_html = uClient.read()
		uClient.close()
		#html parsing
		page_soup = soup(page_html,"html.parser")
		#finds all products on current page
		name = page_soup.find("h1",{"itemprop":"name"}).text
		price = page_soup.findAll("span",{"class":"pull-right"})
		id = page_soup.find("li",{"class":"text-capitalize text-gray-sepia-light small-font"}).text
		id = ' '.join([w for w in id.split() if len(w)==9])

		add_element("E-Commerce", "Dell", "", name, id, price[1].text, price[0].text, product_set)

	except:
		print("www.dell.com pipe is now broken.")



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
		id = page_soup.find("span",{"id":"mfg_id"}).text

		price = butcher(price)
		price = ''.join([i for i in price if i.isdigit() or "."])
		price = price.split(".", 1)[0]
		price = price.split("$", 1)[1]
		price = "$"+price

		add_element("E-Commerce", "BuyVPC", "", name, id, price, "", product_set)

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
				add_element("E-Commerce", "Epson", "Epson.ca", name, "", "CAD "+price, "", product_set)
			else:
				add_element("E-Commerce", "Epson", "Epson (US)", name, "", price, "", product_set)

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

		add_element("E-Commerce", "Walmart", "", name, "", price, shipping, product_set)

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
		id_containers = page_soup.findAll("span",{"class":"sku"})

		for tcontainer, pcontainer, scontainer, icontainer in zip(text_containers, price_containers, shipping_containers, id_containers):
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
			try:
				id = icontainer.text
			except:
				id = ""

			add_element("E-Commerce", "B&H", company, name, id, price, shipping, product_set)

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


			add_element("E-Commerce", "NewEgg", "", name, "", price, shipping, product_set)

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

			add_element("E-Commerce", "Staples", "", name, "", price, "", product_set) #no shipping data

	except:
		print("www.staples.com pipe is now broken.")




#If correct product, object is created and added to product set
def add_element(channel, store, company, name, id, price, shipping, product_set):
	name = butcher(name)
	price = butcher(price)
	price = price.strip()
	shipping = butcher(shipping)

	if "Hp" in name:
		name = name.replace("Hp", "HP")

	#standardize shipping cost
	if "Free" in shipping:
		shipping = "Free Shipping"
	if "free" in shipping:
		shipping = "Free Shipping"

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
		new_product = Product(channel, store, company, name, id, price, shipping)
		product_set.add(new_product)


#breaks up strings
def butcher(word):
	word = str(word)
	word = word.title()
	word = re.sub(r'\W+ ', '', word)
	word = word.replace('*','')
	word = word.replace(',','')
	word = word.replace(':','')
	word = word.replace('\n', '')
	word = word+" "
	return word
