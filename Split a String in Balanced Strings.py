class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l = list(s)
        l2 = list(set(l))
        l1 = []
        count = 0
        while (l):
            a = l.pop()
            b = l.pop()
            if a == b:
                l1.append(a)
                l1.append(b)
                while(l1):
                    c = l.pop()
                    d = l.pop()
                    if c ==d:
                        l1.append(c)
                        l1.append(d)
                    else:
                        l1.append(c)
                        l1.append(d)
                    if l1.count(l2[0]) == l1.count(l2[1]):
                            count +=1
                            l1 = []
            else:
                count +=1
        return count
        '''
        # method 2
        count = 0
        ans = 0
        l = list(set(s))
        for i in s:
            if i ==l[0]:
                count +=1
            else:
                count -=1
            if count == 0:
                ans +=1
        return ans
                    







        '''            