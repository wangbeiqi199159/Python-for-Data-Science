# Scrape Data From XML

```
import urllib
import xml.etree.ElementTree as ET
from urllib import request

url = 'http://python-data.dr-chuck.net/comments_301098.xml'

data = urllib.request.urlopen(url).read()
tree = ET.fromstring(data)
results = tree.findall('.//count')

sum = 0

for result in results:
    count = result.text
    count = int(count)
    sum = sum + count

print(sum)
```
