n=int(input("Enter the number for check for pelindrome: "))
s=0
r=0
num=n
while num>0:
    r=num%10
    s=s*10+r
    num=num//10
if s==n:
    print(n,' is Pelindrome')
else:
    print('Not pelindrome')