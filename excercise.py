l=[10,['user1','user2'],10.25,('test1','test2'),True,None]
list1=[]
print("Default list is ",l,"\n")
for i in l:
    if (type(i)==list):
        for j in i:
            list1.append(j)
    elif (type(i)==tuple):
        for j in i:
            list1.append(j)
    else :
        list1.append(i)
print("list after flaterning")
print(list1)
