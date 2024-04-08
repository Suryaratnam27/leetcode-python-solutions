s="1011"
def binary(s):
    for i in range(0,len(s)-1):
        if s[i]=="1" and s[i+1]=="1":
            return True 
    return False 
a=binary(s)
print(a)
