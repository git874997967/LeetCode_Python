# 520. Detect Capital
def detectCapitalUse(word):
    return True if word == word.upper() or word == word.lower() or word[1:] == word[1:].lower()