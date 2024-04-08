def tot(num1,num2,num3):
    num1=set(num1)
    num2=set(num2)
    num3=set(num3)
    #initialise
    s_char={}
    a=[]
    for i in num1:
        s_char[i]=0
    for i in num2:
        s_char[i]=0
    for i in num3:
        s_char[i]=0
    for i in num1:
        s_char[i]+=1
    for i in num2:
        s_char[i]+=1
    for i in num3:
        s_char[i]+=1
    for k,v in s_char.items():
        if v>1:
            a.append(k)
    return a 
z=tot([1,1,2,3],[2,3,3,5,6],[4,3,6])
print(z)


