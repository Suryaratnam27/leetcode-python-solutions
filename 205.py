def bot(s,t):
    s_char={}
    t_char={}
    for i in s:
        s_char[i]=s_char.get(i,0) + 1
    print(s_char)
    for i in t:
        t_char[i]=0
    for i in t:
        t_char[i]+=1
    block1=[]
    block2=[]
    b=list(s_char.values())
    print(b)
    for i in s_char.values():
        block1.append(i)
    for i in t_char.values():
        block2.append(i)
    block1.sort()
    block2.sort()
    if block1==block2:
        return True 
    else:
        return False

s='abb'
t='def'
a=bot(s,t)
print(a)

