nums=234
def sp(nums):
    boom=[]
    while nums>0:
        d=nums%10
        boom.append(d)
        nums=nums//10
    a=sum(boom)
    b=1
    for i in boom:
        b=b*i 
    c=b-a
    return c 
w=sp(nums)
print(w)
            
        
