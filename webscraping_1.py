import requests
from bs4 import BeautifulSoup 
url="https://www.bvrit.ac.in/placements/training-and-placement-cell"
r=requests.get(url)
soup=BeautifulSoup(r.content,'html.parser')
parse=soup.prettify()
title=soup.title.prettify()
text=soup.get_text()
print(parse)
print(title)
print(text)
