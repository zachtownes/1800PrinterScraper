import json
import requests
from bs4 import BeautifulSoup

url = "http://ctacinv/api/PrinterLevels?GetShortPrinters=true"
page = requests.get(url, verify=False)
print(page.content)
Printers = json.loads(page.content)
for printer in Printers: 
    print(printer['Id'])
    print(printer['PrinterName'])
    print(printer['PrinterIp'])