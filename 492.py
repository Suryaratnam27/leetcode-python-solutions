area=6
def rect(area):
    c=[]
    
    for b in range(1,area+1):
        for l in range(b+1,area+1):
            d=l*b
            if d==area:
                c.append([l,b])
    min_idx=0
    s= c[0][0]-c[0][1]
    for i in range(len(c)):
        lst=c[i]
        if s>(lst[0]-lst[1]):
            min_idx = i 
            s = lst[0] -lst[1]
    return c[min_idx]
        

        



a=rect(area)
print(a)
