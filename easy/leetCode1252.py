#1252. Cells with Odd Values in a Matrix
def oddCells( m, n, indices):
    rows , cols = [0] * m, [0] * n
    for index in indices:
        rows[index[0]] = rows[index[0]] + 1
        cols[index[1]] = cols[index[1]] + 1
    odd_col,odd_row, even_col,even_row = 0,0,0,0
    for row in rows:
        if row% 2 ==0 :
            even_row += 1
        else:
            odd_row += 1
    for col in cols:
        if col % 2 == 0:
            even_col += 1
        else:
            odd_col += 1
    return (odd_row * even_col) + (odd_col * even_row)
    
         


