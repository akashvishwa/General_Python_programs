n=int(input("Enter the number for sum:"))
s=0
r=0
num=n
while num>0:
    r=num%10
    s=s+r
    num=num//10
print('Sum of digit is: ',s)