#-*- coding: utf-8 -*-
#libraries
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from urllib.request import Request, urlopen
from urllib.parse import quote
import os
import binascii
import subprocess

def getpdf():
    req = Request('http://criminalcourt.gov.mv/%de%86%de%af%de%93%de%b0-%de%9d%de%ac%de%91%de%a8%de%87%de%aa%de%8d%de%b0/', headers={'User-Agent': 'Mozilla/5.0'})
    sun = urlopen(req)
    divs = SoupStrainer('div', class_= 'aec aec-events aec-table-layout')
    soup = BeautifulSoup(sun, 'lxml', parse_only=divs)

    latest = soup.find_all('div',class_='row aec-table-layout-row')
    link = latest[0].find('a').get('href')

    #return link
    criminal_dl_data = []
    sub_directory=binascii.b2a_hex(os.urandom(4)).decode('utf-8')
    os.mkdir('/var/www/daisy/ytdl/{0}/'.format(sub_directory))
    
    dl_args=['aria2c', '-q', '--dir', '/var/www/daisy/ytdl/{0}/'.format(sub_directory), link]
    download_processor = subprocess.Popen(dl_args)
    while True:
        poll = download_processor.poll()
        if poll == 0:
            if os.path.exists('/var/www/daisy/ytdl/{0}/'.format(sub_directory)):
                for root, dirs, files in os.walk(os.path.abspath('/var/www/daisy/ytdl/{0}/'.format(sub_directory))):
                    for file in files:
                        total_size = os.path.getsize('/var/www/daisy/ytdl/{0}/{1}'.format(sub_directory,file))
                        file_encoded = quote('{0}'.format(file))
                        media_link = 'https://daisy.eyaadh.net/ytdl/{0}/{1}'.format(sub_directory,file_encoded)
                        file_name = '{0}'.format(file)
                        criminal_dl_data.extend((total_size, media_link, file_name))
                        return criminal_dl_data
            break


pdf = getpdf()
#print(pdf)