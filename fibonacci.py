x=0
y=1
s=0
n=int(input("Enter the no of terms:\n"))
print ('Fibonacci series')

for i in range(n):
    print(x)
    s=x+y
    x=y
    y=s
