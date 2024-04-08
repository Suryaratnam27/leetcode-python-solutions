nums=[3,4,5,2]
def hs(nums):
    nums.sort()
    s=(nums[-1]-1)*(nums[-2]-1)
    return s 
a=hs(nums)
print(a)
