# File: lists.py
# Name: Samuel Guyette
# Desc:  Helper functions for main

#import scraping tools
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
import string
import sys

#import object class
from product_class import Product

#import data lists
from lists import *


#function to create loading bar
def progress(count, total, status=''):
	bar_len = 60
	filled_len = int(round(bar_len * count / float(total)))

	percents = round(100.0 * count / float(total), 1)
	bar = '=' * filled_len + '-' * (bar_len - filled_len)

	sys.stdout.write('[%s] %s%s %s\r' % (bar, percents, '%', status))
	sys.stdout.flush()


#helper function for build_data_set
def loop_site(urllist, func, product_set):
	for url in urllist:
		func(url, product_set)


#loops urls lists through specific scraper
def build_data_set(product_set):
	#loop raw searches
	progress(0,21, status='  Intern work beginning...\n')
	loop_site(staples_urllist, pull_staples, product_set)
	progress(1,21, status='  of data gathered...\n')
	loop_site(newegg_urllist, pull_newegg, product_set)
	progress(2,21, status='  of data gathered...\n')
	loop_site(bh_urllist, pull_bh, product_set)
	progress(3,21, status=' of data gathered...\n')
	loop_site(walmart_urllist, pull_walmart, product_set)
	progress(4,21, status=' of data gathered...\n')
	loop_site(epson_urllist, pull_epson, product_set)
	progress(5,21, status=' of data gathered...\n')
	loop_site(buyvpc_urllist, pull_buyvpc, product_set)
	progress(6,21, status=' of data gathered...\n')
	loop_site(dell_urllist, pull_dell, product_set)
	progress(7,21, status=' of data gathered...\n')
	loop_site(vistek_urllist, pull_vistek, product_set)
	progress(8,21, status=' of data gathered...\n')
	loop_site(tastar_urllist, pull_tastar, product_set)
	progress(9,21, status=' of data gathered...\n')
	loop_site(overland_urllist, pull_overland, product_set)
	progress(10,21, status=' of data gathered...\n')
	loop_site(pcnation_urllist, pull_pcnation, product_set)
	progress(11,21, status=' of data gathered...\n')
	loop_site(hp_urllist, pull_hp, product_set)
	progress(12,21, status=' of data gathered...\n')
	loop_site(tiger_urllist, pull_tiger, product_set)
	progress(13,21, status=' of data gathered...\n')
	loop_site(adorama_urllist, pull_adorama, product_set)
	progress(14,21, status=' of data gathered...\n')
	loop_site(govets_urllist, pull_govets, product_set)
	progress(15,21, status=' of data gathered...\n')
	loop_site(plotter_urllist, pull_plotter, product_set)
	progress(16,21, status=' of data gathered...\n')
	loop_site(pcconnection_urllist, pull_pcconnection, product_set)
	progress(17,21, status=' of data gathered...\n')
	loop_site(amazon_urllist, pull_amazon, product_set)
	progress(18,21, status=' of data gathered...\n')
	loop_site(macmall_urllist, pull_macmall, product_set)
	progress(19,21, status=' of data gathered...\n')
	loop_site(shi_urllist, pull_shi, product_set)
	progress(20,21, status=' of data gathered...\n')
	loop_site(grandtoy_urllist, pull_grandtoy, product_set)
	progress(21,21, status='of data gathered...\n')
	loop_site(zones_urllist, pull_zones, product_set)

# *** Website specific scrapers *** #
def pull_zones(url, product_set):
	#check if broken
	try:
		#opening connections
		uClient = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
		page_html = uClient.text
		uClient.close()
		#html parsing
		page_soup = soup(page_html,"html.parser")
		#finds all products on current page
		containers = page_soup.findAll("div",{"class":"product-inner js-product-inner"})
		if len(containers) == 0:
			print("Zones containers produced zero products.")

		for container in containers:
			name_list = container.find_all('a')
			name = name_list[0].text
			name = name.split('- ', 1)[1]
			name = name + " Printer"
			id = container.find("a",{"class":"mfr_text"}).text
			id = butcher(id).upper()
			price = container.find("div",{"class":"product-price product-unit-price"}).text
			price = butcher(price)
			add_element("NSP", "Zones", "", name, id, price, "", product_set)
	except:
		print("www.zones.com pipe is now broken.")




def pull_grandtoy(url, product_set):
	#check if broken
	try:
		#opening connections
		uClient = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
		page_html = uClient.text
		uClient.close()
		#html parsing
		page_soup = soup(page_html,"html.parser")
		#finds all products on current page
		containers = page_soup.findAll("div",{"class":"product-wrapper row--hasPopup"})
		if len(containers) == 0:
			print("Grand&Toy containers produced zero products.")

		for container in containers:
			name = container.find("h3",{"class":"title"}).text
			id = container.find("div",{"class":"sku"}).text
			id = id.replace("SKU", "")
			id = butcher(id).upper()
			price = container.find("p",{"class":"amt"}).text
			price = butcher(price)
			add_element("NSP", "Grand&Toy", "", name, id, price, "", product_set)

	except:
		print("www.grandandtoy.com pipe is now broken.")




def pull_shi(url, product_set):
	#check if broken
	try:
		#opening connections
		uClient = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
		page_html = uClient.text
		uClient.close()
		#html parsing
		page_soup = soup(page_html,"html.parser")
		#finds all products on current page
		containers = page_soup.findAll("div",{"class":"row"})
		if len(containers) == 0:
			print("Shi containers produced zero products.")

		for container in containers:
			try:
				name = container.find("h2",{"class":"noMarTop"}).text
				if "SureColor" in name:
					name = name + " Printer"
			except:
				name = ""

			try:
				id = container.find("small",{"class":"srMFR srh_pr.mfrn"}).text
				id = id.split('#: ', 1)[1]
				id = butcher(id)
				id = id.upper()
			except:
				id = " "

			try:
				price = container.find("h3",{"class":"text-warning noMarTop"}).text
				if "Login" in price:
					price = container.find("div",{"class":"srStockMSRP"}).text
			except:
				try:
					price = container.find("div",{"class":"srStockMSRP"}).text
				except:
					price = ""

			if "MSRP" in price:
				price = price.split(': ', 1)[1]

			if "PROGRAF" in name:
				name = name+" Printer"

			if "ml" in name:
				name = name+" Ink"

			if id is not " ":
				add_element("NSP", "shi", "", name, id, price, "", product_set)

	except:
		print("www.shi.com pipe is now broken.")




def pull_macmall(url, product_set):
	#check if broken
	try:
		#opening connections
		uClient = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
		page_html = uClient.text
		uClient.close()
		#html parsing
		page_soup = soup(page_html,"html.parser")
		#finds all products on current page
		containers = page_soup.findAll("div",{"class":"iteminfo"})
		if len(containers) == 0:
			print("MacMall containers produced zero products.")

		for container in containers:
			name = container.find("div",{"class":"rtitle"}).text
			id = container.find("div",{"class":"rpart"}).text
			id = id.split('Mfg Part #: ', 1)[1]
			id = id.split(' |', 1)[0]
			try:
				price = container.find("span",{"class":"tprice prod-price withlprice"}).text
			except:
				try:
					price = container.find("span",{"class":"tprice prod-price"}).text
				except:
					price = container.find("span",{"class":"lprice prod-lprice"}).text

			add_element("NSP", "MacMall", "", name, id, price, "", product_set)

	except:
		print("www.macmall.com pipe is now broken.")




def pull_amazon(url, product_set):
	#check if broken
	try:
		#opening connections
		uClient = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
		page_html = uClient.text
		uClient.close()
		#html parsing
		page_soup = soup(page_html,'lxml')
		try:
			name_list = page_soup.find_all('title')
			name = name_list[0].text
			name = name.split('Amazon.com: ', 1)[1]
			name = name.split(': Gateway', 1)[0]
		except:
			name = ""

		try:
			price_list = page_soup.find_all('table')
			price = price_list[0].text
			price = butcher(price)
			price = price.split('Price', 1)[1]
			price = price.split('Free', 1)[0]
			try:
				price = price.split('#', 1)[0]
			except:
				price = price
			if "Shipping" in price:
				price = price.split('$', 2)[0]

		except:
			price = "Sold out"

		add_element("E-Commerce", "Amazon", "", name, "", price, "", product_set)

	except:
		print("www.amazon.com pipe is now broken.")



def pull_pcconnection(url, product_set):
	#check if broken
	try:
		#opening connections
		uClient = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
		page_html = uClient.text
		uClient.close()
		#html parsing
		page_soup = soup(page_html,"html.parser")
		#finds all products on current page
		containers = page_soup.findAll("tr",{"class":"product-container"})

		if len(containers) == 0:
			print("PC Connection containers produced zero products.")

		for container in containers:
			name = container.find("a",{"class":"product-name"}).text
			id = container.find("ul",{"class":"product-bullets"}).text
			id = butcher(id)
			id = id.split('Part', 1)[1]
			id = id.split('Platform', 1)[0]
			id = id.split('Dpi', 1)[0]
			id = id.split('Max', 1)[0]
			id = id.upper()
			try:
				price = container.find("span",{"class":"priceDisplay"}).text
			except:
				price = ""

			add_element("NSP", "PC Connection", "", name, id, price, "", product_set)

	except:
		print("www.connection.com pipe is now broken.")



def pull_plotter(url, product_set):
	#check if broken
	try:
		#opening connections
		uClient = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
		page_html = uClient.text
		uClient.close()
		#html parsing
		page_soup = soup(page_html,"html.parser")
		#finds all products on current page
		containers = page_soup.findAll({"li":"class"})

		if len(containers) == 0:
			print("Plotter Pro containers produced zero products.")

		for container in containers:
			try:
				name = container.find("h2",{"class":"woocommerce-loop-product__title"}).text
				price = container.find("span",{"class":"price"}).text
				try:
					price = "$"  + price.split('$', 2)[2]
				except:
					price = price
			except:
				name = ""
				price = ""

			if "SureColor" in name and "Epson" not in name:
				name = "Epson "+name

			if "PROGRAF" in name and "Printer" not in name:
				name = name+" Printer"

			add_element("ISG", "Plotter Pro", "", name, "", price, "", product_set)

	except:
		print("www.plotterpro.com pipe is now broken.")



def pull_govets(url, product_set):
	#check if broken
	try:
		#opening connections
		uClient = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
		page_html = uClient.text
		uClient.close()
		#html parsing
		page_soup = soup(page_html,"html.parser")
		#finds all products on current page
		containers = page_soup.findAll("div",{"class":"ty-column3"})

		if len(containers) == 0:
			print("GoVets containers produced zero products.")

		for container in containers:
			name = container.find("a",{"class":"product-title"}).text
			try:
				price = container.find("input",{"type":"hidden"})
				price = butcher(price.text)
				price = price.split('$', 2)[2]
				price = "$"+price.split('Q', 1)[0]
			except:
				price = container.find("span",{"class":"ty-price"}).text

			if "SureColor" in name:
				id = name.split('Color ', 1)[1]
				id = id.split('Ink', 1)[0]
			else:
				id = ""

			if "Series" in id:
				id = name.split('Series ', 1)[1]
			if "Ink" in id:
				id = id.split('Ink', 1)[0]

			add_element("E-Commerce", "GoVets", "", name, id, price, "", product_set)

	except:
		print("www.govets.com pipe is now broken.")



def pull_adorama(url, product_set):
	#check if broken
	try:
		#opening connections
		uClient = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
		page_html = uClient.text
		uClient.close()
		#html parsing
		page_soup = soup(page_html,"html.parser")
		#finds all products on current page
		containers = page_soup.find_all("div",{"class"})
		prices = page_soup.findAll("strong",{"class":"your-price"})

		if len(containers) == 0:
			print("Adorama containers produced zero products.")

		for container, pri in zip(containers, prices):
			try:
				name = container.find("div",{"class":"item-details"}).h2.a.text
				id_list = container.findAll("i",{"class":"product-sku"})
				id = id_list[1].text.split('MFR: ', 1)[1]
				price = pri.text
				id = butcher(id)
				id = id.upper()
				try:
					shipping = container.find("strong",{"class":"free-shipping"}).text
				except:
					shipping = ""
			except:
				name = ""
				id = ""
				price = ""

			add_element("E-Commerce", "Adorama", "", name, id, price, "", product_set)

	except:
		print("www.adorama.com pipe is now broken.")


def pull_tiger(url, product_set):
	#check if broken
	try:
		#opening connections
		uClient = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
		page_html = uClient.text
		uClient.close()
		#html parsing
		page_soup = soup(page_html,"html.parser")
		#finds all products on current page
		containers = page_soup.findAll("div",{"class":"product"})
		if len(containers) == 0:
			print("Tiger Direct containers produced zero products.")

		for container in containers:
			name = container.find("h3",{"class":"itemName"}).text
			id = container.find("p",{"class":"itemModel"}).text
			id = butcher(id)
			id = id.split('Model', 1)[1]
			if "#" in id:
				id = id[2:]

			id = id.upper()

			price = container.find("div",{"class":"salePrice"}).text
			try:
				price = price.split('$', 2)[2]
			except:
				price = price
			if "Details" in price:
				price = ""

			add_element("NSP", "Tiger Direct", "", name, id, price, "", product_set)

	except:
		print("www.tigerdirect.com pipe is now broken.")



def pull_hp(url, product_set):
	#check if broken
	try:
		#opening connection
		uClient = uReq(url)
		page_html = uClient.read()
		uClient.close()
		#html parsing
		page_soup = soup(page_html,"html.parser")
		#finds all products on current page
		name_list = page_soup.findAll("h3",{"class":"font-lh3"})
		name = name_list[1].text
		name = name.split('Printer', 1)[0] + "Printer"


		id = name_list[1].text.split('Printer', 1)[1]
		id = id.replace('(','')
		id = id.replace(')','')
		id = butcher(id).upper()
		price = page_soup.find("span",{"itemprop":"price"}).text

		add_element("E-Commerce", "HP", "", name, "CQ891C", price, "", product_set)


	except:
		print("www.hp.com pipe is now broken.")

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
	try:
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

	except:
		print("www.vistek.com pipe is now broken.")



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
		price_list = page_soup.findAll("span",{"class":"pull-right"})
		id = page_soup.find("li",{"class":"text-capitalize text-gray-sepia-light small-font"}).text
		id = ' '.join([w for w in id.split() if len(w)==9])
		if "Free" in price_list[1].text:
			shipping = price_list[1].text
			price = price_list[0].text
		else:
			shipping = price_list[0].text
			price = price_list[1].text

		add_element("E-Commerce", "Dell", "", name, id, price, shipping, product_set)

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

	if "Ipf670" in name:
		name = name.replace("Ipf670", "IPF670")

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
