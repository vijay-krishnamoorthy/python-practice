import os
obj = open("new.txt","r")
text=obj.read()
print(text)
new = open("example_txt.txt","w+")
for i in range(100):
    l=[]
    l.append(i)
test = str(l)
if (new.write(test)):
    print("Write successful")
    print(text)
else:
    print("Unsuccessful!!!")


obj.close()
new.close()
