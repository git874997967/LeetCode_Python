def compress(chars ):
        i, j = 0, 0
        start = 0
        while i < len(chars) and j < len(chars):
            curr = chars[i]
            while j < len(chars) and chars[j] == curr:
                j += 1

            # chars[j] is a different letter
            counts = j - i
            if counts == 1:
                chars[start] = curr
                start += 1
            else:
                chars[start] = curr
                start += 1
                for digit in str(counts):
                    chars[start] = digit
                    start += 1

            i = j
        print(chars)
        return start

compress(["a","a","b","b","c","c","c"])
compress(["a"])
compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])
compress(["a","a","a","b","b","a","a"])