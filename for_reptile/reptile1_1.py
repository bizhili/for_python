from bs4 import BeautifulSoup
from lxml import html
import xml
import requests

def main():
    site="https://movie.douban.com/chart"
    get=requests.get(site)#to access html content
    soup=BeautifulSoup(get.content,"lxml")#To decode by lxml
    #print(get.content.decode())
    for k in soup.find_all('div',class_='pl2'):
        a=k.find_all('span')
        print(a[0].string)
    






















if __name__=="__main__":
    main()
