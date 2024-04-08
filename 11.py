height=[1,8,6,2,5,4,8,3,7]
def water_tank(height):
    block=[]
    l=0
    r=len(height)-1
    while l<r:
        a=r-l 
        b=min(height[l],height[r])
        area=a*b
        block.append(area)
        if height[l]<height[r]:
            l=l+1 
        else:
            r=r-1
    return max(block)
h=water_tank(height)
print(h)
            


