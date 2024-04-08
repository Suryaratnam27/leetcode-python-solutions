def is_pal(num):
    r=0
    num1=num
    while num>0:
        d=num%10
        r=r*10+d 
        num=num//10
    if r==num1:
        return True
    else:
        return False 
a=is_pal(121)
print(a)  

