# Web-scraping

import requests
from bs4 import BeautifulSoup 
url="https://www.bvrit.ac.in/placements/training-and-placement-cell"
r=requests.get(url)
soup=BeautifulSoup(r.content,'html.parser')
parse=soup.prettify()
title=soup.title.prettify()
text=soup.get_text()


The above code implements webscraping using python. Webscraping is used to extract the information from the webpage. We are using beautifulsoup to parse the data which we get by using request library which is used to request the server for the content. Now we have to parse the data so that we get it in nested form which helps us to easily go through the the content and extract the data which we need using html.parser. Here we have extracted the text or the content which is present in the webpage and also we have extraced the title. prettify command is used to give the output in a tag fomat whereas get_text gives the string format as output.
