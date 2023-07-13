from requests_html import HTMLSession
from bs4 import BeautifulSoup

s = HTMLSession()
url = 'https://www.tokopedia.com/cockomputer/msi-modern-md272qp-27-wqhd-ips-75hz-with-usb-c'

def getdata(url):
    r = s.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

print(getdata(url))


