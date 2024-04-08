def third_max(nums):
    if len(nums)<3:
        return max(nums)    
    nums=list(set(nums))
    nums.sort()
    print(nums)
    return nums[-3]


a=third_max([56,3,3,3,2])
print(a)
