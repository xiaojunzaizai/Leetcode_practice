class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        al = list(set(allowed))     
        count = 0
        for i in words:
            flag = 0
            for j in list(set(i)):
                if j not in al:
                    flag = 1
                    break
            if flag == 0:
                count +=1
        return count