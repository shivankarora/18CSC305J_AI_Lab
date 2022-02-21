def printSol(board):
for i in range(4):
for j in range(4):
print (board[i][j])
def isSafe(board, row, col):
for i in range(col):
if board[row][i]==1:
return False
for i,j in zip(range(row, -1, -1), range(col, -1, -1)):
if board[i][j]==1:
return False
for i,j in zip(range(row, 4, 1), range(col, -1, -1)):
if board[i][j]==1:
return False
return True
def sol(board, col):
if col>=4:
return True
for i in range(4):
if isSafe(board, i, col):
board[i][col]=1
if sol(board, col+1)==True:
return True
board[i][col]=0
return False
def solNQueens():
board = [[0, 0, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, 0]]
if sol(board, 0)==False:
print("no solution")
return False
printSol(board)
return True
solNQueens()
