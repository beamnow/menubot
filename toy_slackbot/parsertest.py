from urllib.request import urlopen
from urllib.error import HTTPError
import urllib.parse
import requests
from bs4 import BeautifulSoup
from keyfile import url

url = url
find = ""

def get():
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    finds = soup.find_all('img', class_='org_image')
    find = urllib.parse.urljoin(url, finds[1]['src'])
    return find
