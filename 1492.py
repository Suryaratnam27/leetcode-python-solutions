n=10
def k_element(n):
    block=[]
    for i in range(1,n+1):
        if n%i==0:
            block.append(i)
    return block
def prime(n):
    c=[]
    for i in range(2,n+1):
        a=k_element(i)
        if len(a)==2:
            c.append(i)
    return c



a=prime(n)
print(a)
