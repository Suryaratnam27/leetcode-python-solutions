def run_sum(nums):
    count=0
    a=[]
    for i in nums:
        count+=i 
        a.append(count)
    return a 
b=run_sum([1,2,3,4])
print(b)

