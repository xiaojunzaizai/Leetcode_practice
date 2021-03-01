def shuffle(nums, n) :
    l = nums.copy()
    l1 = l[:n]
    l2 =l[n:]
    l3 = [] 
    for i,j in zip (l1,l2):
        l3.append(i)
        l3.append(j)
    return l3

nums = [2,5,1,3,4,7]
n = 3
print(shuffle(nums,n))