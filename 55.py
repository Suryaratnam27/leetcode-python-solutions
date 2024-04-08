def istam_leni_sum(nums):
    goal=len(nums)-1
    for i in range(len(nums)-2,-1,-1):
        if i+nums[i]>=goal:
            goal=i 

    if goal==0:
        return True
    else:
        return False
a=istam_leni_sum([2,1,0,4,6])
print(a)  


