n=[1,2]
def nm(n):
    a=max(n)
    b=min(n)
    for i in n:
        if i==a or i==b:
            continue
        else:
            return i 
    return -1
a=nm(n)
print(a)
