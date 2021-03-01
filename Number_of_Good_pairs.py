def numIdenticalPairs( nums):
        l = []
        l1 = list(set(nums))
        for i in l1:
            l.append(nums.count(i))
        sum = 0
        for j in l:
            for k in range(j):
                sum = sum +k
        return sum

nums = [1,2,3,1,1,3]
print(numIdenticalPairs(nums))