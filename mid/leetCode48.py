#48. Rotate Image
def rotate(matrix):
    # store the four corners then traverse in a windmill
    # then repeat for inner square
    offset = 0 
    size = len(matrix) - 1
    while True:
        for i in range(size):
            list = [ matrix[offset][i+ offset], # 1 -- 00 
                     matrix[i + offset][size + offset], # 3 -- 02
                     matrix[size + offset][size + offset - i],  # 9 --22 
                     matrix[size + offset - i][offset] # 7 20

                    ]
            # now rotate it 
            print(list)
            matrix[offset][i + offset] = list[3]
            matrix[i + offset][size + offset] = list[0]
            matrix[size + offset][size + offset - i] = list[1]
            matrix[size + offset - i ][offset] = list[2]

        if size < 3:
            break
        offset += 1
        size -= 2


rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
rotate([[1,2,3],[4,5,6],[7,8,9]])