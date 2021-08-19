# 832. Flipping an Image
def flipAndInvertImage(image):
    for i in range(len(image)):
        image[i] = image[i][::-1]
        image[i] = [0 if x == 1 else 1 for x in image[i]]
    print(image)

flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]])
