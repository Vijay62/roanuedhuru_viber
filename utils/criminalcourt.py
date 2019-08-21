#-*- coding: utf-8 -*-
#libraries
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from urllib.request import Request, urlopen
from urllib.parse import unquote
from functools import reduce
import os

def getpdf():
    req = Request('http://criminalcourt.gov.mv/%de%86%de%af%de%93%de%b0-%de%9d%de%ac%de%91%de%a8%de%87%de%aa%de%8d%de%b0/', headers={'User-Agent': 'Mozilla/5.0'})
    sun = urlopen(req)
    divs = SoupStrainer('div', class_= 'aec aec-events aec-table-layout')
    soup = BeautifulSoup(sun, 'lxml', parse_only=divs)

    latest_schedule = soup.find('p', class_='aec-margin-top')
    
    criminalcourt = [] 
    title = soup.find('h3',class_='aec-no-margin').text
    pdf_url = reduce(lambda a, b: a.replace(*b),
                    [('[pdfjs-viewer url="',''), ('" viewer_width=100% viewer_height=1360px fullscreen=true download=true print=true]','')],
                    latest_schedule.text
                )
    pdf_url = unquote(pdf_url)
    pdf = urlopen(pdf_url)
    meta = pdf.info()
    size = meta.get('Content-Length')
    file_name = os.path.basename(pdf_url)
    
    criminalcourt.extend((title, pdf_url, size, file_name))
    return criminalcourt

pdf = getpdf()
#print(pdf)
