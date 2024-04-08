def shuffle(nums,n):
    a=nums[0:n]
    b=nums[n:]
    c=[]
    for i in range(n):
        c.append(a[i])
        c.append(b[i])
    return c 
g=shuffle([2,3,5,4,1,7],3)
print(g)
    
