class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l = []
        for i in nums:
            count = 0
            for j in nums:
                if i>j:
                    count +=1
            l.append(count)
        return l

        # medthod 2
        #n2 = sorted(nums)
        
        #out = [n2.index(n) for n in nums]
        
        #return out