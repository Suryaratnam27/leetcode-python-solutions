def swap(char):
    l=0
    r=len(char)-1
    while l<=r:
        char[l],char[r]=char[r],char[l]
        l+=1
        r-=1
    return char
a=swap(["c","h","i","n","a","r","i"])
print(a)
