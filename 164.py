n=[3,6,9,1]
def max_gap(n):
    n.sort()
    b=[]

    for i in range(0,len(n)-1):
        a=n[i+1]-n[i]
        b.append(a)
    return max(b)
s=max_gap(n)
print(s)
    
