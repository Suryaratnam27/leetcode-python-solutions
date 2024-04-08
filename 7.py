n=124
def reverse(n):

    p=0
    while n>0:
        d=n%10
        p=p*10+d 
        n=n//10
    return p 
a=reverse(n)
print(a)
