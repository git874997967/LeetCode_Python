#443. String Compression
def compress(chars):
    start, end = 0 , 0 
    length = 0 
    while start < len(chars) and end < len(chars):
        curr = chars[start]
        while end < len(chars) and chars[end] == chars[start]:
            end += 1
        counts = end - start 
        chars[length] = curr 
        length += 1
        if counts > 1:
            for digit in str(counts):
                chars[length] = digit
                length += 1
        start = end 
    print(chars)
    return length

compress(["a","a","b","b","c","c","c"])
compress(["a"])
compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])
compress(["a","a","a","b","b","a","a"])