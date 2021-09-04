#1720. Decode XORed Array
def decode(encoded, first):
   result = [encoded[0] ^ first]
 
   for i in range(1,len(encoded)):
       result.append(encoded[i]^ result[i-1])
   return[first] + result
print(decode([1,2,3],1))
print(decode([6,2,7,3],4))