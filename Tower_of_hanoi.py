def TOH(n,start,end,aux):
    if(n>=1):
        TOH(n-1,start,aux,end)
        print(n,'moves from',start,'to',end)
        TOH(n-1,aux,end,start)

n=int(input("The no of disk: "))
TOH(n,'A','C','B')