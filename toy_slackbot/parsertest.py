from urllib.request import urlopen
from urllib.error import HTTPError
import urllib.parse
import requests
from bs4 import BeautifulSoup
from keyfile import url
from PIL import Image
from io import BytesIO
from datetime import datetime

url = url
find = ""

def get():
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    finds = soup.find_all('img', class_='org_image')
    find = urllib.parse.urljoin(url, finds[1]['src'])
    return find

def day_get():
    find = get()
    
    image = requests.get(find).content # url의 이미지를 바이트 값으로 받아옴
    menu_img = Image.open(BytesIO(image)) # 바이트 값을 변환시켜 실제 이미지를 변수에 넣음
    # crop(left, up, right, down)
    # (992, 1403)

    weekday = datetime.now().weekday() + 1
    interval_y = 210 # 한 칸의 세로 폭 간격
    end_y = 225 + (interval_y * weekday)
    start_y = end_y - interval_y

    today_img = menu_img.crop((80,start_y,550,end_y))

    today_img.save('today_menu.png')
    return today_img
