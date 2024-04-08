n=[1,1,1,2,2,2,2,3,4]
def top_k(n,k):
    n_char={}
    for i in n:
        n_char[i]=0
    for i in n:
        n_char[i]+=1
    arr=[]
    for i in range(len(n)):
        arr.append([])
    print(arr)
    for key,v in n_char.items():
        arr[v].append(key)
    print(arr)

    res=[]
    for i in range(len(arr)-1,0,-1):
        for num in arr[i]:
            res.append(num)
            print(f"res:{res}")
            if len(res)==k:
                return res

    print(res)
        
a=top_k(n,2)
print(a)
