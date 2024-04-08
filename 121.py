nums=[7,1,5,3,4]
def max_profit(nums):
    profit=[]
    l=0
    r=1
    for r in range(1,len(nums)):
        a=(nums[r]-nums[l])
        if a<0:
            l=r 
        else:
            profit.append(a)
    
    return max(profit)
d=max_profit(nums)
print(d)


        
