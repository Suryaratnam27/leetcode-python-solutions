def restore_string(S,I):
    result=[]
    for c in range(len(S)):
        result.append(0)
    print(result)
    for idx,char in zip(I,S):
        result[idx]=char
    print(result)
restore_string("codeleet",[4,5,6,7,0,2,1,3])

