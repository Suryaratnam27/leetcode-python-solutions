nums=[1,1,0,1]
def max_con(nums):
    sumi=0
    block=[]
    for i in range(0,len(nums)):
        if nums[i]==1:
            sumi+=nums[i]
        else:
            block.append(sumi)
            sumi=0
    block.append(sumi)

    return max(block) 
a=max_con(nums)
print(a)

