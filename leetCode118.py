# 118. Pascal's Triangle
# this question will use two diamension array 
# so classic!! with index operation in array
def generate(self, numRows):
    result = []
    for rowNum in range(numRows):
        # use to init the row   generate rowNum + 1 elements for Nth row
        row = [None for _ in range(rowNum + 1)]
        # the first and the last with index 
        row[0],row[- 1] = 1,1
        for j in range( 1, len(row) - 1):
            row[j] = result[rowNum-1][j-1] + result[rowNum-1][j]
        result.append(row)
    return result

def generate2(self, numRows):
    result = []
    for rowNum in range(numRows):
        row = [0] * (rowNum + 1)
        row[0],row[-1] = 1,1
        for j in range(1,rowNum):
            row[j] = result[row-1][j-1] + result[row-1][j]
        result.append(row)
    return result