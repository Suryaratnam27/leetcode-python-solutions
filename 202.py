nums=1024
def nive_podu(nums):
    p=0
    while nums>0:
        d=nums%10 
        p=p+(d*d)
        nums=nums//10
    return p

def is_happy(n):
    is_seen = set()
    while n>1:
        n = nive_podu(n)
        if n in is_seen: 
            return False
        else:
            is_seen.add(n)
    if n==1:
        return True

a = is_happy(19)
print(a)

