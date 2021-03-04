# 58. Length of Last Word
def lengthOflastWord(s):
    if s.isspace() or s is None:
        return 0
    return len(s.split()[-1])