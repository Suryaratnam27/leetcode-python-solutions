arr=[17,18,5,4,6,1]
def replace_ele(arr):
    block=[]
    for i in range(0,len(arr)-1):
        l=i+1 
        r=len(arr)-1
        while l < r: 
            if arr[l]>arr[r]:
                r=r-1 
            elif arr[l]<arr[r]:
                l=l+1 
        block.append(arr[l])
    block.append(-1)
    return block 
a=replace_ele(arr)
print(a)               
