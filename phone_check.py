import re
#generalized pattern for below phone numbers
ph='044-25132642'
ph2='044.02131231'
ph3='044*12451236'

value=re.search(r'[0-9]{1,3}\S[0-9]{8}',ph)
print(value)
value=re.search(r'[0-9]{1,3}\S[0-9]{8}',ph2)
print(value)
value=re.search(r'[0-9]{1,3}\S[0-9]{8}',ph3)
print(value)


#get working hours
s='(Monday to Friday, 0930 hrs. - 1730 hrs. IST)'
v=re.search(r'[0-9]+',s)
print(v.group(0))s
print(v.group(1))
