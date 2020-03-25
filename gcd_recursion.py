def gcd(x,y):
    if(x==0):
        return(y)
    if(y==0):
        return(x)
    if(x==y):
        return(x)
    if(x>y):
        return(gcd(x%y,y))
    else:
        return(gcd(x,y%x))
n=int(input("Enter First Number: "))
n2=int(input("Enter Second Number: "))
print('Gcd is: ',gcd(n,n2))