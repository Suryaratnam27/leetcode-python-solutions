n=[5,1,1,1]
k=0
def time(n,k):
    count=0
    while True:
        for i in range(0,len(n)):
            if n[i]!=0:
                n[i]=n[i]-1
                count+=1
            if n[k]==0 and i==k:
                return count
a=time(n,k)
print(a)
