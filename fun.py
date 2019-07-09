def hi():
    name = input("Tell me your name\n");
    print(name + ", Did you called me?");
    response=input("let me know \n");
    if(response == "no" or response == "No"):
        print("You didn't called me!!, I thought i heard someone calling me!.\n Thar's okay I must b talking to myself");
    else:
        reply = input("Why did you called me?");
        print("you called me just for, "+reply);
    print("Ok, bye. I'm leaving");
    
