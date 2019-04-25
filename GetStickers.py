import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import unquote

src="http://sg.salieri.me/assets/stickers/"


def downloadSticker(url,dir,file):
    if not os.path.exists('src/'+unquote(dir)):
        os.mkdir('src/'+unquote(dir))
    if not os.path.exists('src/'+unquote(dir)+unquote(file)):
        myfile = requests.get(url+dir+file, allow_redirects=True)
        print('src/'+unquote(dir)+unquote(file))
        open('src/'+unquote(dir)+unquote(file), 'wb').write(myfile.content)

def getStickers(dir="./"):
    r =requests.get(src+dir)
    soup = BeautifulSoup(r.text).body.table
    for i in soup.find_all('tr'):
        try:
            if i.td.img['alt']=='[IMG]':
                downloadSticker(src,dir,i.find('a')['href'])
            if i.td.img['alt']=='[DIR]':
                getStickers(dir=i.find('a')['href'])
        except:
            pass

getStickers()

