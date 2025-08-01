# It will download image in hd

from bs4 import BeautifulSoup as soup
from security import safe_requests

if __name__ == '__main__':
    uname = str(input("Enter the username : "))
    new = safe_requests.get('https://www.instadp.com/fullsize/{}'.format(uname))
    imgsoup = soup(new.content, 'lxml')
    imglink = imgsoup.find('img', {'class': 'picture'})['src']
    imgfind = safe_requests.get(imglink)
    photo = open('photo.png', 'wb')
    photo.write(imgfind.content)
    photo.close()
