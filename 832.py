def image(nums):
    for i in range(len(nums)):
        nums[i].reverse() 
        for j in range(len(nums[i])):
            if nums[i][j]==0:
                nums[i][j]=1
            else:
                nums[i][j]=0
    return nums
a=image([[1,1,0],[1,0,1],[0,0,0]])
print(a)
