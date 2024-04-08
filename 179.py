nums=[3,30,34,5,9]
def largest_num(nums):
    n=len(nums)
    for i in range(n-1):
        for j in range(i+1,n):
            if str(nums[i])+str(nums[j]) > str(nums[j]) + str(nums[i]):
                continue
            else:
                nums[i],nums[j] = nums[j], nums[i]
    print(nums)

largest_num(nums)
