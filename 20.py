def is_valid(chars):
    stack=[]
    dictn={'(':')','[':']','{':'}'}
    for i in chars:
        if i in dictn:
            stack.append(i)
        else:
            if i== dictn[stack[-1]]:
                stack.pop()
            else:
                return False
    if len(stack)==0:
        return True
a=is_valid("(]")
print(a)





