x=0
y=1
z=1
s=0
n=int(input("Enter the no of terms:\n"))
print ('Tribonacci series')

for i in range(n):
    print(x)
    s=x+y+z
    x=y
    y=z
    z=s
