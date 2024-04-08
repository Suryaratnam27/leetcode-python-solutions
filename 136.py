def find_uni(nums):
    s={}
    for i in nums:
        s[i]=0
    print(s)

    for i in nums:
        s[i]+=1
    print(s)
    for i in s:
        if s[i]==1:
            return i 
        


a=find_uni([2,2,1])
print(a)
