n=[1,7,3,6,5,6]
def pivot(n):
    for i in range(1,len(n)+1):
        if sum(n[0:i])==sum(n[i+1:len(n)]):
            return n[i]
    return -1
a=pivot(n)
print(a)

