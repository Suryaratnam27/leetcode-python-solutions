

def vowels(char):
    char=list(char)
    a=[]
    v=["a","e","i","o","u"]
    for i in range(0,len(char)):
        if char[i] in v:
            a.append(i)
    print(a)
    l=0
    r=len(a)-1
    while l<r:
        i = a[l]
        j = a[r]
        char[i],char[j]=char[j],char[i]
        l+=1
        r-=1
    return char


def swap_vowels(char):
    char = list(char)
    l = 0
    r = len(char) - 1
    vowels = ['a','e','i','o','u']
    while l<r:
        if char[l] not in vowels:
            l+=1
        elif char[r] not in vowels:
            r -=1
        else:
            char[l], char[r] = char[r],char[l]
            l+=1
            r-=1
    return "".join(char)



a=swap_vowels("hellomai")
print(a)

