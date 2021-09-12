#1961. Check If String Is a Prefix of Array
def isPrefixString(s, words):
     result = ""
     for i in range(words):
         result += words[i]
         if result == s:
             return True
     return False

