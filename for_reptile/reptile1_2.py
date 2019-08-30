from bs4 import BeautifulSoup
from lxml import html
import xml
import requests

def main():
    site="http://www.jianshu.com"
    get=requests.get(site)#to access html content
    soup=BeautifulSoup(get.content,"lxml")#To decode by lxml
    #print(get.content.decode())
    






















if __name__=="__main__":
    main()
