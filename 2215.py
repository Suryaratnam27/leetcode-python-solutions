num1=[1,2,3]
num2=[2,4,6]
def find_diff(num1,num2):
    block=[]
    b1=[]
    b2=[]
    for i in num1:
        if i not in num2:
            b1.append(i) 
    for i in num2:
        if i not in num1:
            b2.append(i)
    block.append(b1)
    block.append(b2)

    return block 
a=find_diff(num1,num2)
print(a)
