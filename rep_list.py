def del_rep():
    n=int(input("Enter the no of elements"))
    print("Enter the list elements")
    l=[]
    for i in range(n):
        l.append(input())
    print(l)
    for i in l:
        c=int(l.count(i))
        for j in l:
            if(i==j) and c >1:
                l.remove(j)
                c-=1
        
    print(l)
