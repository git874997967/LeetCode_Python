#680. Valid Palindrome II almost recurive   need to modify the check condition alittle 
def validPalindrome(s):
    start , end  = 0, len(s) - 1
    while start < end:
        if s[start] < s[end]:
            str1 , str2 = s[start:end], s[start + 1:end + 1]
            return str1 == str1[::-1] or str2 == str2[::-1]
        start += 1
        end -= 1
    return True

print(validPalindrome("aba"))
print(validPalindrome("eccer"))
print(validPalindrome("abcdefg"))
print(validPalindrome("abca"))
#print(validPalindrome("zmvdcyittrhqrrcfaybotuxkfnxewcfqgjeswjgwozzaltqwwdnkrfpqeenxcvbhzsnfengnmyntvvieypwmsawmnhmmzrfkjhlvgrnnegliwthmcbpygcbbfwextwuzybsvudgeuknageekfjmwjogajcmuaznzvupjduqajtiottbikjsjjlyvgtxcjqoteazsoubxyhhzwjiujlqbjyzmsvggnvaqyhwkhpgrhoraatguctklrgbjvyxjmtvjxfjjpcsfndtojzynfqzgufpjktncpvcudgmsekyvcghxmmzqcrvgmxfnfpbdpyxdotthyhtmcbwoxepiklcpidsnehvarbcmtxedzndgkodsgcmfuxtnsywxtjqprhbfpletitctbwwgxwpxttilrhmguojwxdsuhgstugpdxrnldxawgsarixkgoaownlomnekhunuazhqmnrcqhmrseuuxoghkpnyejfyfewgetkhzlmucfoynacgywxhqwmlapzcdtzsczqesbctzpazeqocabpwyshomdkkaltxfuwyslxuzzblccafjikgbayqspyggipxaonjjzzmpniajdowjjhyvdbtinlhigobwhcuvupmufykynzcdlnsktmahgdofxmylkzinigsuzgqeuqspdpemupnoexouusrfqqdmuvmpwpritdncagpzoneaqqfobxnanxwrhfnftyttxsnldybbebqetrncgkgcyajmrmhpyhockgylxtljegumzpttanwttqkbisvyoidlblydigjlwymkwhsrhldxlacvarkravapxivzsbodrgrbpxaqfnqfleeqsojmbutzwupjbmpebinkjkmhtmkysfntgrwlsqdbhnbbvskgbafpimqdizkgomjsicojkgrjcjeekzhrgoszpxiavxkaxfjrrqxxhbjolmmkidvlalnmxfldmizhydcbjpdxusnajrivwheovqxsnpzyinm..."))