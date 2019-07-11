import collections
n=int(input("enter the number of words :"))
d=collections.OrderedDict()
for i in range(n):
    word=input("Word :")
    if word in d:
        d[word]+=1
    else:
        d[word]=1

print("Total words in the dictionary is, ",len(d))
for i,j in d.items():
    print(i," has occured ",j,"times")
            
