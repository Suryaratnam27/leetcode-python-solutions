a="qwertyuiop"
b="asdfghjkl"
c="zxcvbnm"
def search(nums,a,b,c):
    count=0
    count1=0
    count2=0
    for i in nums:
        if i in a:
            count+=1
        elif i in b:
            count1+=1
        elif i in c:
            count2+=1
    if len(nums)==count or len(nums)==count1 or len(nums)==count2:
        return True
    else:
        return False
d=search("qwyur",a,b,c)
print(d) 



    
