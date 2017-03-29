# Input Data From txt

```
import re

data = open ("data.txt")
lst = list()
for line in data:
    line = line.rstrip()
    nums = re.findall("([0-9]+)+",line)
    if len(nums) == 0: continue
    for num in nums:
        num = int(num)
        lst.append(num)

total = 0
for num in lst:
    total = total + num

print (total)
```
