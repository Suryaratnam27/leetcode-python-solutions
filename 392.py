s="abc"
t="ahbgdc"
def is_sub(s,t):
    s_char={}
    t_char={}
    for i in s:
        s_char[i]=0
    for i in s:
        s_char[i]+=1
    for i in t:
        t_char[i]=0
    for i in t:
        t_char[i]+=1
    for k,v in s_char.items():
        if k not in t_char:
            return -1
        elif t_char[k] < v:
            return -1
    return True
a=is_sub("abc","ahgdc")
print(a)
        


