n=[1,2,2,3]
def sum_unique(n):
    p={}
    for i in n:
        p[i]=0
    for i in n:
        p[i]+=1
    sume=0
    for k,v in p.items():
        if v==1:
            sume=sume+k
    return sume 
a=sum_unique(n)
print(a)



