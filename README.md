# Epson-Web-Scraper

Epson-Web-Scraper (main.py) is a Python script that pulls from over 1600 data points, 210 webpages, and 31 different resellers. Data is then
transferred into a pivot type table displaying pricing of Epson T-Series printers and their competitors compared to all web resellers.
Green cells are prices above UP. Red cells are prices bellow lowest sales price permitted.

Excel Comparison Tool is a Python script that takes two command line arguments of two .xlsx files outputted by Epson-Web-Scraper. The
script finds differences in prices between both files. Differences will be highlighted in red showing past and current price, all else
will be grey scaled back.

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
[MIT](https://choosealicense.com/licenses/mit/)
