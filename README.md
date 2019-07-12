# Epson-Web-Scraper

Epson-Web-Scraper (main.py) is a Python script that pulls from over 1600 data points, 210 webpages, and 31 different resellers. Data is then
transferred into a pivot type table displaying pricing of Epson T-Series printers and their competitors compared to all web resellers.
Green cells are prices above UP. Red cells are prices bellow lowest sales price permitted.

Excel Comparison Tool is a Python script that takes two command line arguments both being .xlsx files outputted by Epson-Web-Scraper. The
script finds differences in prices between both files. Differences will be highlighted in red showing past and current price, all else
will be grey scaled back.


# Motivation

Epson T-Series product prices change daily across multiple e-commerce channels, this creates a challenge of confirming that hundreds of products
are in compliance with Epson's UP policy. The Epson-Web-Scraper highlights which products and companies are out of compliance in real time.
The pivot like table also provides visibility of mean and median across all web sellers, ensuring that pricing goals are met. Data is also pulled
from T-Series competitors on the same e-commerce websites revealing if Epson T-Series products are being sold at competitive prices for the
current market place.

The Excel Comparison Tool indicates which companies and products have changed prices in a given timeframe. This can display if a back end rebate
or different promotions constructed motivation for price changes. This data can also predict if price matching will ensue across resellers in a
domino like fashion.  



## Installation

Use the package manager [pip](https://pypi.org/project/beautifulsoup4/) to install beautifulsoup4.
Use the package manager [pip](https://pypi.org/project/lxml/) to install lxml.
Use the package manager [pip](https://pypi.org/project/numpy/) to install numpy.
Use the package manager [pip](https://pypi.org/project/openpyxl/) to install openpyxl.
Use the package manager [pip](https://pypi.org/project/pandas/) to install pandas.
Use the package manager [pip](https://pypi.org/project/urllib3/) to install urllib3.
Use the package manager [pip](https://pypi.org/project/requests/) to install requests.

```bash
pip install beautifulsoup4
pip install lxml
pip install numpy
pip install openpyxl
pip install pandas
pip install urllib3
pip install requests
```

## Usage

```python
python main.py #Main webscraper to excel script, outputs .xlsx sheet named "final_output"
python Excel_Comparison_Tool.py name1.xlsx name2.xlsx #Compares name1 and name2 for differences, outputs name1_vs_name2.xlsx sheet
```


## License
[Epson End User Software License Agreement](https://epson.com/SoftwareLicenseAgreement)
