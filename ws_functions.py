# File: lists.py
# Name: Samuel Guyette
# Desc:  Helper functions for main
# Other files required: lists.py, product_class.py

#import scraping tools
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
import string
import sys

#import object class
from product_class import Product


#checks for arg list
if(len(sys.argv) < 2):
	print("Usage: Specify which list you would like to use on the command line.")
	print("T = T-Series")
	print("PI = Paper and Ink")
	sys.exit()

data_dump = False
if "T" in sys.argv[1]:
	from lists_t_series import *
elif "PI" in sys.argv[1]:
	data_dump = True
	from lists_paper_ink import *
elif "P" in sys.argv[1]:
	from lists_p_series import *
else:
	print("Usage: Specify which list you would like to use on the command line.")
	print("T = T-Series Printers")
	print("P = P-Series Printers")
	print("PI = Paper and Ink")
	sys.exit()

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
	# progress(0,32, status='  Intern work beginning...\n')
	# loop_site(staples_urllist, pull_staples, product_set)
	# progress(1,23, status='  of data gathered...\n')
	# loop_site(newegg_urllist, pull_newegg, product_set)
	# progress(2,32, status='  of data gathered...\n')
	# loop_site(bh_urllist, pull_bh, product_set)
	# progress(3,32, status='  of data gathered...\n')
	# loop_site(walmart_urllist, pull_walmart, product_set)
	# progress(4,32, status=' of data gathered...\n')
	# loop_site(epson_urllist, pull_epson, product_set)
	# progress(5,32, status=' of data gathered...\n')
	# loop_site(buyvpc_urllist, pull_buyvpc, product_set)
	# progress(6,32, status=' of data gathered...\n')
	# loop_site(dell_urllist, pull_dell, product_set)
	# progress(7,32, status=' of data gathered...\n')
	# loop_site(vistek_urllist, pull_vistek, product_set)
	# progress(8,32, status=' of data gathered...\n')
	# loop_site(tastar_urllist, pull_tastar, product_set)
	# progress(9,32, status=' of data gathered...\n')
	# loop_site(overland_urllist, pull_overland, product_set)
	# progress(10,32, status=' of data gathered...\n')
	# loop_site(pcnation_urllist, pull_pcnation, product_set)
	# progress(11,32, status=' of data gathered...\n')
	# loop_site(hp_urllist, pull_hp, product_set)
	# progress(12,32, status=' of data gathered...\n')
	# loop_site(tiger_urllist, pull_tiger, product_set)
	# progress(13,32, status=' of data gathered...\n')
	# loop_site(adorama_urllist, pull_adorama, product_set)
	# progress(14,32, status=' of data gathered...\n')
	# loop_site(govets_urllist, pull_govets, product_set)
	# progress(15,32, status=' of data gathered...\n')
	# loop_site(plotter_urllist, pull_plotter, product_set)
	# progress(16,32, status=' of data gathered...\n')
	# loop_site(pcconnection_urllist, pull_pcconnection, product_set)
	# progress(17,32, status=' of data gathered...\n')
	# loop_site(amazon_urllist, pull_amazon, product_set)
	# progress(18,32, status=' of data gathered...\n')
	# loop_site(macmall_urllist, pull_macmall, product_set)
	# progress(19,32, status=' of data gathered...\n')
	# loop_site(shi_urllist, pull_shi, product_set)
	# progress(20,32, status=' of data gathered...\n')
	loop_site(grandtoy_urllist, pull_grandtoy, product_set)
	# progress(21,32, status=' of data gathered...\n')
	# loop_site(zones_urllist, pull_zones, product_set)
	# progress(22,32, status=' of data gathered...\n')
	# loop_site(cdw_urllist, pull_cdw, product_set)
	# progress(23,32, status=' of data gathered...\n')
	# loop_site(itsupplies_urllist, pull_itsupplies, product_set)
	# progress(24,32, status=' of data gathered...\n')
	# loop_site(imagespectrum_urllist, pull_spectrum, product_set)
	# progress(25,32, status=' of data gathered...\n')
	# loop_site(laube_urllist, pull_laube, product_set)
	# progress(26,32, status=' of data gathered...\n')
	# loop_site(lexjet_urllist, pull_lexjet, product_set)
	# progress(27,32, status=' of data gathered...\n')
	# loop_site(buffalo_urllist, pull_buffalo, product_set)
	# progress(28,32, status=' of data gathered...\n')
	# loop_site(allamerican_urllist, pull_allamerican, product_set)
	# progress(29,32, status=' of data gathered...\n')
	# loop_site(proimagingsupplies_urllist, pull_proimagingsupplies, product_set)
	# progress(30,32, status=' of data gathered...\n')
	# loop_site(shadesofpaper_urllist, pull_shadesofpaper, product_set)
	# progress(31,32, status=' of data gathered...\n')
	# loop_site(spectraflow_urllist, pull_spectraflow, product_set)
	# progress(32,32, status='of data gathered...\n')

	if not data_dump:
		#create uniform skus
		print("Modifying SKU numbers...\n")
		standardize_skus(product_set)


# *** Website specific scrapers *** #
def pull_spectraflow(url, product_set):
	#check if broken
	try:
		page_soup = pull_html(url)
		#finds all products on current page
		name = page_soup.findAll("div",{"class":"itemlist_description"})
		price = page_soup.findAll("div",{"class":"itemlist_price"})

		for name_, price_ in zip(name, price):
			add_element("ProFocus", "US", "Spectraflow", "", name_.text, "", price_.text, "", product_set)
	except:
		print("www.spectraflow.com pipe is now broken.")



def pull_shadesofpaper(url, product_set):
	#check if broken
	try:
		page_soup = pull_html(url)

		name = page_soup.find("h1",{"id":"productName"}).text
		price = page_soup.find("span",{"class":"productBasePrice"}).text

		add_element("ProFocus", "US", "Shades of Paper", "", name, "", price, "", product_set)
	except:
		print("www.shadesofpaper.com pipe is now broken.")



def pull_proimagingsupplies(url, product_set):
	#check if broken
	try:
		page_soup = pull_html(url)
		#finds all products on current page
		containers_1 = page_soup.findAll("td",{"class":"content-odd2"})
		containers_2 = page_soup.findAll("td",{"class":"content-even2"})
		full_containers = containers_1 + containers_2
		if len(full_containers) == 0:
			print("ProImaging Supplies containers produced zero products.")

		for container in full_containers:
			name = container.find("div",{"class":"title"}).text
			try:
				price = container.find("span",{"class":"salePrice myerror"}).text
			except:
				price = "Add To Cart to Show Price"
			add_element("ProFocus", "US", "ProImaging Supplies", "", name, "", price, "", product_set)

	except:
		print("www.proimaginesupplies.com pipe is now broken.")



def pull_allamerican(url, product_set):
	#check if broken
	try:
		page_soup = pull_html(url)

		name = page_soup.find("h1",{"class":"product-title"}).text
		price = page_soup.find("div",{"class":"product--price"}).text
		try:
			price = price.split('$', 2)[2]
		except:
			pass

		add_element("ProFocus", "US", "All American", "", name, "", price, "", product_set)
	except:
		print("www.aaprintsupplyco.us pipe is now broken.")



def pull_buffalo(url, product_set):
	#check if broken
	try:
		page_soup = pull_html(url)

		name = page_soup.find("h1",{"class":"product_title entry-title elementor-heading-title elementor-size-large"}).text
		id = page_soup.find("span",{"class":"sku"}).text
		try:
			price = page_soup.find("p",{"class":"price product-page-price price-on-sale"}).text
			price = price.split('$', 1)[1]
			price = price.split('$', 1)[1]
		except:
			price = page_soup.find("p",{"class":"price product-page-price"}).text

		add_element("ProFocus", "US", "Buffalo", "", name, id, price, "", product_set)
	except:
		print("www.buffalous.us pipe is now broken.")



def pull_lexjet(url, product_set):
	#check if broken
	try:
		page_soup = pull_html(url)
		#finds all products on current page
		containers = page_soup.findAll("div",{"class":"col-xs-12"})
		if len(containers) == 0:
			print("LexJet containers produced zero products.")

		lexjet_list = []
		for container in containers:
			try:
				name = container.find("a",{"class":"product-name"}).text
			except:
				name = ""
			try:
				id = container.find("span",{"itemprop":"sku"}).text
			except:
				id = ""
			try:
				price = container.find("span",{"itemprop":"price"}).text
			except:
				price = ""

			if id not in lexjet_list:
				add_element("ProFocus", "US", "LexJet", "", name, id, price, "", product_set)
				lexjet_list.append(id)
	except:
		print("www.lexjet.com pipe is now broken.")



def pull_laube(url, product_set):
	#check if broken
	try:
		page_soup = pull_html(url)

		name = page_soup.find("h1",{"itemprop":"name"}).text
		id = page_soup.find("dd",{"class":"productView-info-value"}).text
		price = page_soup.find("div",{"class":"price-section price-section--withoutTax"}).text
		price = butcher(price)
		price = price.split('Now', 1)[1]

		add_element("ProFocus", "US", "Laube", "", name, id, price, "", product_set)
	except:
		print("www.imagingspectrum.com pipe is now broken.")



def pull_spectrum(url, product_set):
	#check if broken
	try:
		page_soup = pull_html(url)

		name = page_soup.find("div",{"class":"product-title"}).text
		id = page_soup.find("span",{"class":"property-value"}).text
		price = page_soup.find("span",{"id":"product_price"}).text

		add_element("ProFocus", "US", "Imaging Spectrum", "", name, id, price, "", product_set)
	except:
		print("www.imagingspectrum.com pipe is now broken.")




def pull_itsupplies(url, product_set):
	#check if broken
	try:
		page_soup = pull_html(url)

		name = page_soup.find("h1",{"class":"vp-product-title"}).text
		price = page_soup.find("span",{"itemprop":"price"}).text
		id = page_soup.find("span",{"class":"product_code"}).text

		add_element("ProFocus", "US", "ITSupplies", "", name, id, price, "", product_set)
	except:
		print("www.itsupplies.com pipe is now broken.")



def pull_cdw(url, product_set):
	#check if broken
	try:
		page_soup = pull_html(url)
		#finds all products on current page
		containers = page_soup.findAll("div",{"class":"search-result coupon-check"})
		if len(containers) == 0:
			print("CDW containers produced zero products.")

		for container in containers:
			name = container.find("a",{"class":"search-result-product-url"}).text
			if "SureColor" in name:
				name = name + " Printer"

			id = container.find("span",{"class":"mfg-code"}).text
			id = id.split(': ', 1)[1]
			price = container.find("div",{"class":"price-type-price"}).text

			add_element("NSP", "US", "CDW", "", name, id, price, "", product_set)
	except:
		print("1/11 www.cdw.com links is broken.")



def pull_zones(url, product_set):
	#check if broken
	try:
		page_soup = pull_html(url)
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
			add_element("NSP", "US", "Zones", "", name, id, price, "", product_set)
	except:
		print("www.zones.com pipe is now broken.")



def pull_grandtoy(url, product_set):
	#check if broken
	try:
		page_soup = pull_html(url)
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
			if "/" in price:
				price = price.split('$', 2)[1]
				price = "$"+price


			add_element("NSP", "CA", "Grand&Toy", "", name, id, price, "", product_set)

	except:
		print("1 www.grandandtoy.com link is now broken.")




def pull_shi(url, product_set):
	#check if broken
	try:
		page_soup = pull_html(url)
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
				add_element("NSP", "US", "shi", "", name, id, price, "", product_set)

	except:
		print("www.shi.com pipe is now broken.")




def pull_macmall(url, product_set):
	#check if broken
	try:
		page_soup = pull_html(url)
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

			add_element("NSP", "US", "MacMall", "", name, id, price, "", product_set)

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
			try:
				name = name.split('Amazon.com: ', 1)[1]
				name = name.split(': Gateway', 1)[0]
			except:
				pass
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

		add_element("E-Commerce", "US", "Amazon", "", name, "", price, "", product_set)

	except:
		print("www.amazon.com pipe is now broken.")



def pull_pcconnection(url, product_set):
	#check if broken
	try:
		page_soup = pull_html(url)
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
				price = "call for price"

			add_element("NSP", "US", "PC Connection", "", name, id, price, "", product_set)

	except:
		print("www.connection.com pipe is now broken.")



def pull_plotter(url, product_set):
	#check if broken
	try:
		page_soup = pull_html(url)
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

			add_element("ISG", "US", "Plotter Pro", "", name, "", price, "", product_set)

	except:
		print("www.plotterpro.com pipe is now broken.")



def pull_govets(url, product_set):
	#check if broken
	#try:
	page_soup = pull_html(url)
	#finds all products on current page
	containers = page_soup.findAll("div",{"class":"ty-column3"})

	if len(containers) == 0:
		print("GoVets containers produced zero products.")

	for container in containers:
		try:
			name = container.find("a",{"class":"product-title"}).text
		except:
			name = ""
		try:
			price = container.find("input",{"type":"hidden"})
			price = butcher(price.text)
			price = price.split('$', 2)[2]
			price = "$"+price.split('Q', 1)[0]
		except:
			try:
				price = container.find("span",{"class":"ty-price"}).text
			except:
				price = ""
		if "SureColor" in name:
			id = name.split('Color ', 1)[1]
			id = id.split('Ink', 1)[0]
		else:
			id = ""

		if "Series" in id:
			id = name.split('Series ', 1)[1]
		if "Ink" in id:
			id = id.split('Ink', 1)[0]

		add_element("E-Commerce", "US", "GoVets", "", name, id, price, "", product_set)

	#except:
	#	print("www.govets.com pipe is now broken.")



def pull_adorama(url, product_set):
	#check if broken
	try:
		page_soup = pull_html(url)
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

			add_element("E-Commerce", "US", "Adorama", "", name, id, price, "", product_set)

	except:
		print("www.adorama.com pipe is now broken.")


def pull_tiger(url, product_set):
	#check if broken
	try:
		page_soup = pull_html(url)
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
				price = "Add to Cart"

			add_element("NSP", "US", "Tiger Direct", "", name, id, price, "", product_set)

	except:
		print("one www.tigerdirect.com link is now broken.")



def pull_hp(url, product_set):
	#check if broken
	try:
		page_soup = pull_html(url)

		name_list = page_soup.findAll("h3",{"class":"font-lh3"})
		name = name_list[1].text
		name = name.split('Printer', 1)[0] + "Printer"

		id = name_list[1].text.split('Printer', 1)[1]
		id = id.replace('(','')
		id = id.replace(')','')
		id = butcher(id).upper()
		price = page_soup.find("span",{"itemprop":"price"}).text

		add_element("E-Commerce", "US", "HP", "", name, "", price, "", product_set)

	except:
		try:
			page_soup = pull_html(url)

			name = page_soup.find("h1",{"class":"hp-main-heading-lowercase prodName"}).text
			price = page_soup.find("span",{"class":"hp-large-price-label"}).text
			price = price.replace('*', '')
			add_element("E-Commerce", "US", "HP", "", name, "", price, "", product_set)
		except:
			try:
				page_soup = pull_html(url)
				name = page_soup.find("span",{"itemprop":"name"}).text
				price = page_soup.find("span",{"id":"price_value"}).text
				price = price.replace('*', '')
				add_element("E-Commerce", "US", "HP", "", name, "", price, "", product_set)
			except:
				print("www.hp.com pipe is now broken.")



def pull_pcnation(url, product_set):
	#check if broken
	try:
		page_soup = pull_html(url)
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

			add_element("NSP", "US", "PCNation", "", name, id, price, "", product_set)

	except:
		print("www.pcnation.com pipe is now broken.")



def pull_overland(url, product_set):
	#check if broken
	try:
		page_soup = pull_html(url)
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
			add_element("ISG", "US", "Overland Blueprint", "", name, "", price, "", product_set)

	except:
		print("www.overlandblueprint.com pipe is now broken.")



def pull_tastar(url, product_set):
	#check if broken
	try:
		page_soup = pull_html(url)
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
			add_element("ISG", "US", "Tartar Supply", brand, name, sku, price, "Free Shipping", product_set)


	except:
		print("www.tastarsupply.com pipe is now broken.")



def pull_vistek(url, product_set):
	#check if broken
	#try:
	page_soup = pull_html(url)

	name = page_soup.find("h1",{"class":"title"}).text
	try:
		price = page_soup.find("div",{"class":"card-body"}).text
		price = butcher(price)
		price = price.split('Qty', 1)[0]
		price = price.split('Your Price', 1)[1]
	except:
		price = "No_Data"

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

	add_element("E-Commerce", "CA", "Vistek", "", name, id, price, shipping, product_set)

	#except:
	#	print("1/20 www.vistek.com links is now broken.")



def pull_dell(url, product_set):
	#check if broken
	try:
		page_soup = pull_html(url)

		name = page_soup.find("h1",{"itemprop":"name"}).text
		if "Epson" in name:
			name = name + " Surecolor"
		price_list = page_soup.findAll("span",{"class":"pull-right"})
		id = page_soup.find("li",{"class":"text-capitalize text-gray-sepia-light small-font"}).text
		id = ' '.join([w for w in id.split() if len(w)==9])
		if "Free" in price_list[1].text:
			shipping = price_list[1].text
			price = price_list[2].text
		else:
			shipping = price_list[2].text
			price = price_list[1].text

		add_element("E-Commerce", "US", "Dell", "", name, id, price, shipping, product_set)

	except:
		print("www.dell.com pipe is now broken.")



def pull_buyvpc(url, product_set):
	#check if broken
	try:
		page_soup = pull_html(url)
		#finds data on page
		name = page_soup.find("h2",{"itemprop":"name"}).text
		price = page_soup.find("div",{"class":"price"}).text
		id = page_soup.find("span",{"id":"mfg_id"}).text

		if "SC" in name:
			name = name.replace('SC', '')

		price = butcher(price)
		price = ''.join([i for i in price if i.isdigit() or "."])
		price = price.split(".", 1)[0]
		price = price.split("$", 1)[1]
		price = "$"+price

		add_element("E-Commerce", "US", "BuyVPC", "", name, id, price, "", product_set)

	except:
		print("www.newegg.com pipe is now broken.")



def pull_epson(url, product_set):
	#check if broken
	try:
		page_soup = pull_html(url)
		#finds all products on current page
		containers = page_soup.findAll("div",{"class":"product-info"})

		if len(containers) == 0:
			print("Epson containers produced zero products.")

		for container in containers:
			name = (container.find("a",{"class":"name"}).text)
			if "Ink" not in name and "Paper" not in name:
				name = name + " Printer"

			price = container.findAll("div",{"class":"amount"})
			if len(price) > 0:
				try:
					price = price[1].text
				except:
					price = price[0].text
			else:
				price = ""

			if "epson.ca" in url:
				add_element("E-Commerce", "CA", "Epson.ca", "Epson", name, "", price, "", product_set)
			else:
				add_element("E-Commerce", "US", "Epson", "Epson", name, "", price, "", product_set)

	except:
		print("www.epson.com pipe is now broken.")



def pull_walmart(url, product_set):
	#check if broken
	try:
		page_soup = pull_html(url)
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

		add_element("E-Commerce", "US", "Walmart", "", name, "", price, shipping, product_set)

	except:
		print("www.walmart.com pipe is now broken.")



def pull_bh(url, product_set):
	#check if broken
	try:
		page_soup = pull_html(url)
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

			add_element("E-Commerce", "US", "B&H", company, name, id, price, shipping, product_set)

	except:
		print("www.bhphotovideo.com pipe is now broken.")



def pull_newegg(url, product_set):
	#check if broken
	try:
		page_soup = pull_html(url)
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


			add_element("E-Commerce", "US", "NewEgg", "", name, "", price, shipping, product_set)

	except:
		print("www.newegg.com pipe is now broken.")



def pull_staples(url, product_set):
	#check if broken
	try:
		page_soup = pull_html(url)
		#finds all products on current page
		containers = page_soup.findAll("div",{"class":"standard-type__large_product_tile"})

		if len(containers) == 0:
			print("Staples containers produced zero products.")

		for container in containers:
			name = container.div.div.a["title"]
			price = container.find("span",{"class":"standard-type__price"}).text

			add_element("E-Commerce", "US", "Staples", "", name, "", price, "", product_set) #no shipping data

	except:
		print("www.staples.com pipe is now broken.")



#creates same sku number for same products
def standardize_skus(product_list):
	matching_sku = ""
	#loops all products
	for product in product_list:
		continue_loop = True
		#stops loop if product is accessory
		for word in accessories_include_list:
			if word in product.name:
				continue_loop = False
		if continue_loop:
			#loops all sku keys for each product
			for key in sku_key:
				match = True
				#loops all words in sku key to try and find a match
				for word in key[0]:
					if word not in product.name:
						match = False
				#loops all words that can't be in the name
				for word in key[1]:
					if word in product.name:
						match = False
				#if true change sku
				if match is True:
					sku_change = True
					product.id = key[2]

#opens connection via beautiful soup and urllib
def pull_html(url):
	#opening connections
	uClient = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
	page_html = uClient.text
	uClient.close()
	#html parsing
	page_soup = soup(page_html,"html.parser")
	return page_soup


#If correct product, object is created and added to product set
def add_element(channel, country, store, company, name, id, price, shipping, product_set):
	name = butcher(name)
	price = butcher(price)
	price = price.strip()
	shipping = butcher(shipping)
	#add space between all upper and lower case
	name = re.sub(r"(\w)([A-Z])", r"\1 \2", name)

	if "Hp" in name:
		name = name.replace("Hp", "HP")

	if "Ipf670" in name:
		name = name.replace("Ipf670", "IPF670")

	if "(" in name:
		try:
			tempName = name
			tempName = name.split("(", 1)[1]
			first = tempName[0]
			if not first.isdigit():
				name = name.split("(", 1)[0]
		except:
			name = name.replace("(","")

	if "$" not in price:
		price = "$"+price

	#standardize shipping cost
	if "Free" in shipping:
		shipping = "Free Shipping"
	if "free" in shipping:
		shipping = "Free Shipping"

	#if no digits in price remove $
	if not any(char.isdigit() for char in price):
		price = price.replace('$','')

	#find which comapny the product belongs to
	if company is "" or " ":
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
		new_product = Product(channel, country, store, company, name, id, price, shipping)
		product_set.add(new_product)


#breaks up strings
def butcher(word):
	word = str(word)
	word = word.title()
	word = re.sub(r'\W+ ', '', word)
	word = word.replace('*','')
	word = word.replace('Hewlett Packard', 'HP')
	word = word.replace('P-600','P600')
	word = word.replace(',','')
	word = word.replace(':','')
	word = word.replace('\n', '')
	word = word+" "
	return word
