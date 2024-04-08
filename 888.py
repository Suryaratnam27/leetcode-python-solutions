def fair_candy(a,b):
    e=(sum(b)-sum(a))//2
    for i in a:
        if i+e in b:
            return [i,i+e] 
z=fair_candy([1,1],[2,2])
print(z)

