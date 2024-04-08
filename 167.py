nums=[1,2,3,4]
t=6
def two_sum(nums,t):
    l=0
    r=len(nums)-1
    while l<r:
        a=nums[l]+nums[r] 
        if a<t:
            l+=1
        elif a>t:
            r-=1
        else:
            return [l+1,r+1]
    return 0
a=two_sum(nums,t)
print(a)




