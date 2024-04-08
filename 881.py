nums=[0,1,1,1,2,2,3] 
t=3
def num_boats(nums,t):
    nums.sort()
    l=0
    r=len(nums)-1
    boats=0
    while l<=r:
        if nums[l]+nums[r]>t:
            r-=1
        else:
            l+=1
            r-=1
        boats+=1
    return boats
mummy=num_boats(nums,t)
print(mummy)


