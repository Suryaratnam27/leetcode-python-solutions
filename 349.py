def inter(nums1,nums2):
    nums=[]
    nums1=list(set(nums1))
    nums2=list(set(nums2))

    for i in nums1:
        if i in nums2:
            nums.append(i)
    return nums

def inter1(nums1,nums2):
    return list(set(nums1).intersection(set(nums2)))

a=inter1([4,9,5],[9,4,9,8,4])
print(a)
