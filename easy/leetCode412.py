# 412. Fizz Buzz
def fizzBuzz(n):
    result,start =[], 1
    while start <= n:
        if start % 15 == 0:
            result.append('FizzBuzz')
        elif start % 3 == 0:
            result.append('Fizz')
        elif start % 5 == 0:
            result.append('Buzz')
        else:
            result.append(str(start))
        start += 1
    return result 

print(fizzBuzz(15))