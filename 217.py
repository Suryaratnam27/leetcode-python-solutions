
def dup(nums):
    s_char={}
    for i in nums:
        s_char[i]=0
    for i in nums:
        s_char[i]+=1
    for i in s_char.values():
        if i>1:
            return True

    return False
a=dup([1,2,3,1])
print(a)

l=[1,2,3,4,1]
a = not(len(l)==len(set(l)))
print(a)
