def replace(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] != nums[j-1]:
            nums[i] = nums[j]
            i+=1 
    for idx in range(i,len(nums)):
        nums[idx] = ''
    return i 

nums = [0,0,1,1,1,2,2,3,3,4]
n = replace(nums)
print(n)
