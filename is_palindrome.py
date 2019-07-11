def is_palindrome(s):
    l=[]
    for i in s:
        l.append(i)    
    if(l==l[::-1]):
        print("The given string",s.upper(),"is a Palindrome")
    else:
        print("The given sting is not a Palindrome")
        
