n=10
def prime(n):
    num=[1]*n
    num[0]=0

    print(num)
    for i in range(2,n):
        if num[i]==1:
            for j in range(2*i,n,i):
                num[j]=0
    return sum(num)

a=prime(n)
print(a)
