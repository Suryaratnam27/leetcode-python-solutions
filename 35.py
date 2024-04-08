nums=[1,3,6,7]
T=5
def search(nums,T):
    for i in range(0,len(nums)):
        if nums[i]==T:

            return i
        elif nums[i]>T:
            return i
a=search(nums,T)
print(a)
