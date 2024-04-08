n=15 
def fizbuz(n):
    b=[]
    for i in range(1,n+1):
        if i%3!=0 and i%5!=0:
            b.append(str(i))
        elif i%3==0 and i%5==0:
            b.append("fizzbuzz")
        elif i%3==0:
            b.append("fizz")
        elif i%5==0:
            b.append("buzz")
        
        
    return b 
a=fizbuz(n)
print(a)
