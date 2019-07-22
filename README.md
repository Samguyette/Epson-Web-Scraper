# Epson-Web-Scraper

Epson-Web-Scraper (main.py) is a Python script that pulls from over 8000 data points, 600 webpages, and 31 different resellers. Data is then
transferred into a pivot type table displaying pricing and shipping of Epson T-Series products, P-Series products, printers and ink and their
respective competitors. Green cells are prices above UP. Red cells are prices bellow lowest sales price permitted.

Excel Comparison Tool similarly is a Python script that takes two command line arguments both being .xlsx files outputted by Epson-Web-Scraper
at different times. The script finds differences in prices between both files. Differences will be highlighted in red showing past and current
price, all else will be grey scaled back.


## Motivation

Epson T-Series product prices change daily across multiple e-commerce channels, this creates a challenge of confirming that hundreds of products
are in compliance with Epson's UP policy. The Epson-Web-Scraper highlights which products and companies are out of compliance in real time.
The pivot like table also provides visibility of mean and median of products across all web sellers, ensuring that pricing goals are met. Data is
also pulled from competitors on the same e-commerce websites revealing if Epson products are being sold at competitive prices in relation to the
current market place.

The Excel Comparison Tool indicates which companies and products have changed prices in a given timeframe. This can display if a back end rebate
or different promotions constructed motivation for price changes. This data can also predict if price matching will ensue across resellers in a
domino like fashion.  


## Installation

Use the package manager to install [beautifulsoup4](https://pypi.org/project/beautifulsoup4/), [lxml](https://pypi.org/project/lxml/),
[numpy](https://pypi.org/project/numpy/), [openpyxl](https://pypi.org/project/openpyxl/), [pandas](https://pypi.org/project/pandas/),
[urllib3](https://pypi.org/project/urllib3/), [requests](https://pypi.org/project/requests/).


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
#### Command Line
```python
python main.py P #Outputs P-Series Data with name timedate-P-Series.xlsx
python main.py S #Outputs S-Series Data with name timedate-S-Series.xlsx
python main.py PI #Outputs printer and ink Data with name timedate-Printer_and_Ink.xlsx
python Excel_Comparison_Tool.py name1.xlsx name2.xlsx #Compares name1 and name2 for differences, outputs name1_vs_name2.xlsx sheet
```
#### User Interface
Created a php user interface that lives on an internal server. This provides easy usability where project managers can download their products
data with a click of a button.
