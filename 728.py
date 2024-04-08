l=1
r=22
def self_div(l,r):
    b=[]
    for i in range(l,r):
        d=i%10
        if d==0:
            continue
        while True:
            if d%i==0:
                i=i//10
            b.append(i) 

    return b 
a=self_div(l,r)
print(a)
