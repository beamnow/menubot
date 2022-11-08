from urllib.request import urlopen
from urllib.error import HTTPError
import urllib.parse
import requests
from bs4 import BeautifulSoup
import pprint


# import ssl
# context = ssl._create_unverified_context()
url = url
find = ""

req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')

finds = soup.find_all('img', class_='org_image')
# for find in finds:
#     find = urllib.parse.urljoin(url, find['src'])

find = urllib.parse.urljoin(url, finds[1]['src'])
print(find)
