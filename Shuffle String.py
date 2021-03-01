class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        l = list(s)
        for j,i in zip(s,indices):
            l[i] = j
        return ''.join(l)