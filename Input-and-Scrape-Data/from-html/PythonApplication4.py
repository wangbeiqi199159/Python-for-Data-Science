import urllib
from bs4 import BeautifulSoup
from urllib import request

url = "http://python-data.dr-chuck.net/known_by_Ayla.html"


pos=int(input("Enter position:"))
count=int(input("Enter count:"))

# Retrieve all of the anchor tags
i=0
while(i<count):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,"lxml")
    tags=soup("a")
    print (tags[pos-1].contents[0])
    url=tags[pos-1].get('href', None)
    i=i+1


