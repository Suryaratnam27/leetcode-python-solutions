num=1
def is_square(num):
    for i in range(num+1):
    
        if i*i==num:
            return True
        
    return False
a=is_square(num)
print(a)
