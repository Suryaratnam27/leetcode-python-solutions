def max_arr(nums):
    s = 0
    maxi=float('-inf')
    block = []
    for i in nums:
     s += i 
     if s<0:
         s=0
     if s>maxi:
         maxi=s
    return maxi 
nums=[-2,1,-3,4,-1,2,1,-5,4]
a=max_arr(nums)
print(a)

