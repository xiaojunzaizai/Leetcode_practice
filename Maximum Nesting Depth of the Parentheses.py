class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        m = 0
        for i in s:
            if i == '(':
                count +=1
            if i == ')':
                count -=1
            if count > m:
                m = count
        return m