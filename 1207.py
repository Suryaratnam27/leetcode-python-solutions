def unique(arr):
    nums={}
    for i in arr:
        nums[i]=0
    for i in arr:
        nums[i]+=1
    print(nums)
    print(len(nums.values()))
    if len(nums.values())==len(set(nums.values())):
        return True
    else:
        return False
d=unique([1,2,2,1,3])
print(d)
    
