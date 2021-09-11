#48. Rotate Image
def rotate(matrix):
    # store the four corners then traverse in a windmill
    # then repeat for inner square
    offset = 0 
    turnTime = len(matrix) - 1
    while True:
        for i in range(turnTime):
            list = [ matrix[offset][i+ offset], # 1 -- 00 
                     matrix[i + offset][turnTime + offset], # 3 -- 02
                     matrix[turnTime + offset][turnTime + offset - i],  # 9 --22 
                     matrix[turnTime + offset - i][offset] # 7 20
                    ]
            # now rotate it 
            print(list)
            matrix[offset][i + offset] = list[3]
            matrix[i + offset][turnTime + offset] = list[0]
            matrix[turnTime + offset][turnTime + offset - i] = list[1]
            matrix[turnTime + offset - i ][offset] = list[2]

        if turnTime < 3:
            break
        offset += 1
        turnTime -= 2

# void rotate(vector<vector<int>>& matrix) {
# 	int n = matrix.turnTime();
# 	for(int i=0; i<n/2; i++){
# 		for(int j=i; j<n-i-1; j++){
# 			swap(matrix[i][j],matrix[j][n-i-1]);
# 			swap(matrix[i][j],matrix[n-i-1][n-j-1]);
# 			swap(matrix[i][j],matrix[n-j-1][i]);
# 		}
# 	}
# }
rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
rotate([[1,2,3],[4,5,6],[7,8,9]])