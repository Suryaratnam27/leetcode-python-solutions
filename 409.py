s="abccccdddfff"
def long_pal(s):
    s_char={}
    for i in s:
        s_char[i]=0
    for i in s:
        s_char[i]+=1
    count=0
    is_odd=False
    for i in s_char.values():
        if i%2==0:
            count+=i 
        else:
            is_odd=True
            count=count+(i-1)

    if is_odd:
        return count+1 
    return count 
a=long_pal(s)
print(a)



