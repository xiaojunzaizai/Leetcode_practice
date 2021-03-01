def numJewelsInStones( jewels: str, stones: str):
    sum = 0
    s = list(set(jewels))
    for i in s:
        sum = sum + stones.count(i)
    return sum

jewels = "aA"
stones = "aAAbbbb"

print(numJewelsInStones(jewels,stones))
