def maximumWealth(accounts):
    # m = 0
    # for i in accounts:
    #     if sum(i)>m:
    #         m = sum(i)
    # return m
    return max([sum(i) for i in accounts])

accounts = [[1,2,3],[3,2,1]]

print(maximumWealth(accounts))


