

board=[
    [5,-1,-1,1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,2,-1,4,-1,-1],
    [9,-1,-1,-1,-1,-1,-1,-1,8],
    [-1,-1,-1,6,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,9,-1],
    [-1,4,-1,-1,-1,8,-1,-1,-1],
    [-1,2,-1,-1,-1,-1,-1,-1,-1],
    [8,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,7,-1,-1,-1,3,-1],
]

print(board[0:3,0:3])

num_allowed=[1,2,3,4,5,6,7,8,9]
def SudokuSolver(board, num_allowed, pending_value):
    if pending_value>0:
        for i in range(0,9):
            for j in range(0, 9):
                if board[i][j]==-1:
                    for num in num_allowed:
                        can_be_inserted= True
                        for check in range(0,9):
                            if num== board[i][check] or num== board[check][j]:
                                can_be_inserted=False
                                break
                        if can_be_inserted:
                            board[i][j]=num
                            pending_value-=1
                            break
        SudokuSolver(board, num_allowed,pending_value)

#SudokuSolver(board, num_allowed,68)
print (board)

