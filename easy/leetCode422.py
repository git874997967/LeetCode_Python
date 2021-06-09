# 422. Valid Word Square
def validWordSquare(words):
          # Iterate each row to check the valid square
            for i ,row in enumerate(words):
                col = ''.join([row[i] for row in words if i < len(row)])

                if len(col) != len(row) or col != row :
                    return False
            return True

