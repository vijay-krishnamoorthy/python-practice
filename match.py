#get working hours from the string

import datetime
import time
import re

s='(Monday to Friday, 0930 hrs. - 1730 hrs. IST)'
#value=re.search(r'\w+\s\w+\s,\s(\d{4}\shrs\.\s-\s\d{4}\shrs\.)\sIST\)',s)

value=re.search(r'(\d{4}\shrs\.\s-\s\d{4}\shrs\.)',s)
print(value.group(0))

found=[]
phone=['044-13253112','100.22121132','704*12457845']
for i in phone:
    value=re.match(r'\d{3}[*|.|-]\d{8}',i)
    found.append(value.group(0))
print(found)

pattern=re.compile(r'o')
pattern_object=pattern.finditer(pattern,s)
for i in pattern_object:
    print(i)
