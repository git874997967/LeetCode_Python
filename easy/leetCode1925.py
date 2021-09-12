#1925. Count Square Sum Triples
def countTriples(n):
    result = 0 

    for a  in range(1,n +1):
        for c in range(1,a):
            b  = a * a - c * c
            bsqrt = int(b ** 0.5)
            if bsqrt ** 2 == b:
                result += 1

    return result