s="loveleetcode"
c="e"
def short_char(s,c):
    e=[]
    for i in range(0,len(s)):
        if s[i]=="e":
            e.append(i)
    print(e)
    d=[]
    sumi=len(s)
    for i in range(0,len(s)):
        for j in range(0,len(e)):
            p=abs(i-e[j])
            if p<sumi:
                sumi=p
        d.append(sumi)
        sumi=len(s)
    return d
a=short_char(s,c)
print(a)
