p=input("Enter IP Address\n")
ip=p.split(".")
count=0
i=0
err_count=0;
for i in ip:
    n=int(i)
    if(n < 256 and n > -1):
        count+=1;
    else:
        err_count+=1;
        if(i in ip):
            print("\n",i,"is not a Valid Domain!")
        
if(count!=0 and count ==4):
    print("\nValid IP Address\n")
    #print("Domains Okay =")
    #print(count)
    #print("Error count is=")
    #print(err_count)
else:
    print("\nNot a valid IP Adderess\n")
    print("Domains Okay =")
    print(count)
    print("Error domain count is=")
    print(err_count)
        
    
