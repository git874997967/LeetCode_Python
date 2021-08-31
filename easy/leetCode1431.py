#1431. Kids With the Greatest Number of Candies
def kidsWithCandies( candies, extraCandies):
    maxAmount = max(candies)

    result = []
    for candy in candies:
        if candy + extraCandies >= maxAmount:
            result.append(True)
        else:
            result.append(False)
    return result