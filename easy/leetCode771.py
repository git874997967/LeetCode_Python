#771. Jewels and Stones
def numJewelsInStones(jewels, stones):
    result = 0
    stoneMap = {}
    for stone in stones:
        stoneMap[stone] = stoneMap.get(stone,0) + 1

    for jewel in jewels:
        result += stoneMap.get(jewel,0)
    print(result)
    return result

numJewelsInStones("aA","aAAbbbb")


numJewelsInStones("z","ZZ")

