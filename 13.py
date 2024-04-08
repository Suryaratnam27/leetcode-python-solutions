def r_i(nums):
    s={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    block=[]
    for i in range(0,len(nums)-1):
        if s[nums[i]]>=s[nums[i+1]]:
            block.append(s[nums[i]])
        else:
            block.append(-s[nums[i]])
    block.append(s[nums[-1]])
    return sum(block)
a=r_i("MCMXCIV")
print(a)
            


