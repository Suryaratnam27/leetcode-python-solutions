num=[3,0,1]
def miss_num(num):
    num.sort()
    p=0
    for i in num:
        if i==p:
            p+=1
        else:
            return p 
a=miss_num(num)
print(a)










