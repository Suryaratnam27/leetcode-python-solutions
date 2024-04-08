n="25"
def letter_com(n):
    s_char={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
    b=[]
    if len(n)==1:
        for i in s_char[n]:
            b.append(i)
    elif len(n)==2:
        c1=s_char[n[0]]
        c2=s_char[n[1]]
        for i in c1:
            for j in c2:
                b.append(i+j)
    return b
a=letter_com(n)
print(a)


