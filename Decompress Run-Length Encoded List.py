class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        l1 = []
        l2 = []
        l3 = []
        for i in range(len(nums)):
            if i%2 == 0:
                l1.append(nums[i])
            else:
                l2.append(nums[i])
        for i in range(len(l1)):
            for j in range(l1[i]):
                l3.append(l2[i])
        return l3
        # method 2
        # return [v for i in range(0, len(nums), 2) for v in [nums[i+1]]*nums[i]]