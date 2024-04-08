def square(nums):
    n=[]
    for i in nums:
        i=i*i 
        n.append(i)
    n.sort()
    return n
a=square([-4,-1,0,3,10])
print(a)
