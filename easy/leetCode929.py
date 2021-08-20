#929. Unique Email Addresses
def numUniqueEmails(emails):
    emailMap = {}
    for email in emails:
        nameArr = email.split("@")
        localName = nameArr[0].split("+")
        realLocal = localName[0].replace(".", "")
        realEmail = realLocal +"@" + nameArr[1]
        emailMap[realEmail] = emailMap.get(realEmail, 0) + 1
        print(realEmail)
    return len(emailMap)  

print(numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))

print(numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))
 
print(numUniqueEmails(["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]))