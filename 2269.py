n=430043
k=2
def kb(n,k):
    num=n
    block=[]
    while n>0:
        d=n%10**k
        block.append(d)
        n=n//10
    
    #print(block)
    #print(num)
    block2=[]
    for i in block:
        if i!=0 and num%i==0:
            block2.append(i)
    return len(block2)
a=kb(n,k)
print(a)



kb(n,k)

        
