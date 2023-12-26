#Sudoku
def is_valid(board, row, col, num):
    if num in board[row] or num in [board[i][col]for i in range(9)]:
        return False
    start_row, start_col = 3*(row//3),3*(col//3)
    for i in range(start_row, start_row+3):
        for j in range(start_col,start_col+3):
            if board[i][j]==num:
                return False
            
        return True
    
def solve_sudoku(board):
    empty_cell = find_empty_cell(board)

    if not empty_cell:
        return True       #Puzzle solved
    row,col = empty_cell

    for num in map(str,range(1,10)):
        if is_valid(board,row,col,num):
            board[row][col]=num
            if solve_sudoku(board):
                return True
            board[row][col] = '!'
            return False
    
def  find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == '!':
                return i,j
    return None