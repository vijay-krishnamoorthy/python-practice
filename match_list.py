import re
'''s=" Hi there,how are you?"
#matching a string starting words
print(re.match("how",s))

#searching the string for particular value
print(re.search("how",s))

#finding all occurences of the string given
print(re.findall('o',s))

#splitting the strig with the delimeter specified
print(re.split('',s))

#substituing the struing with the value passed
match=re.sub('o','#',s)
print(match)

#searching the white spaces in the string given
match=re.search('\W',s)
print(match)

#finding the first letter of the string
match=re.search('\S',s)
print(match)

#other than newline,spaces,tabs
print((re.search('\s',s))) 

ip='192.168.111.111'
value = re.search(r'([0-2][0-9][0-9])\.([0-2][0-9][0-9])\.([0-2][0-9][0-9])\.([0-2][0-9][0-9])',ip)
print(value)
print(value.group(0))
print(value.group(1))
print(value.group(2))
print(value.group(3))
print(value.group(4))

ip='192.168.111.111'
value = re.search(r'\d+\.\d+\.\d+\.\d+',ip)
print(value)
ip1='192.168.111.111'
value = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ip1)
print(value)

ipv6='f6e8::80c9::5d7a::b500::2312%24'
value=re.search(r'[a-fA-F0-9]{4}\::[a-fA-F0-9]{4}\:[a-fA-F0-9]{4}\:[a-fA-F0-9]{4}\%[a-fA-F0-9]{2}',ipv6)
print(value)

'''
ph ="local phoen numebr: 044-28412563"
v=re.search(r'[0-9]{1,4}\-[0-9]{8}',ph)
print(v.group(0))

ph='044.21355213'
