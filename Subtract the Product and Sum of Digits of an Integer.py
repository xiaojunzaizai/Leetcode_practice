class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = 0
        p = 1
        while(n !=0):
            s = s+ (n%10)
            p = p* (n%10)
            n = n//10
        return p-s


'''
method 2


def subtractProductAndSum(self, n: int) -> int:
        if n==1:
            return 0
        arr=list(str(n))
        summ=reduce((lambda x, y: int(x) + int(y)), arr)
        prod=reduce((lambda x, y: int(x) * int(y)), arr)
        return prod-summ
'''