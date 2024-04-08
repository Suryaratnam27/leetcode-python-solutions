nums=[0,1,0,1,3,12]
def move_zero(nums):
    a=[]
    for i in nums:
        if i==0:
            a.append(i)
            nums.remove(0)
    return (nums+a)
d=move_zero(nums)
print(d)

