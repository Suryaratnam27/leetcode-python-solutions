def binary(nums,target):
    l=0
    r=len(nums)-1
    while l<=r:
        m=(l+r)//2
        if nums[m]==target:
            return m 
        elif nums[m]<target:
            l=m+1
        else:
            r=m-1
    return -1
a=binary([0,1,2,3,4,5,6,7,18],18)
print(a)

