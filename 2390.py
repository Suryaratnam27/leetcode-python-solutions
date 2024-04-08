s="leet**cod*e"
def remove_stars(s):
    b=[]
    for i in s:
        if i!="*":
            b.append(i)
        else:
            b.pop()
    return "-".join(b)
a=remove_stars(s)
print(a)
