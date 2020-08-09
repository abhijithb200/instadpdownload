import requests
from bs4 import BeautifulSoup as bs


username = input("enter the username:")

URL= f"https://www.instadp.com/fullsize/{username}"
r = requests.get(URL).content
soup = bs(r,'html.parser')
picclass=soup.find('div',class_='instadp')
pic = picclass.find('img',class_="picture")
pic = pic['src']
p = requests.get(pic).content

filename=username+'.png'


with open(filename,'wb') as f:
    f.write(p)
