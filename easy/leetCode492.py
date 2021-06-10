# 492. Construct the Rectangle
def constructRectangle(area):
      root = int(area ** 0.5)
      if root * root == area:
          return [root,root]
      else:
          for i in range(root,0,-1):
              if area % i == 0:
                  return [int (area / i), i]
      return [area,1]



print(constructRectangle(18))

print(constructRectangle(4))

print(constructRectangle(122122))