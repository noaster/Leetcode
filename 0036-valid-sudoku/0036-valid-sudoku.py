class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowLen = len(board)
        colLen = len(board[0])
        unit = 3
        
        result = True
        for i in range(rowLen):
            colFlags = 0
            rowFlags = 0
            groupFlags = 0
            for j in range(colLen):
                if board[i][j] != '.':
                    position = int(board[i][j])
                    if (colFlags & (1 << position)) != 0:
                        result = False
                        #print(f"{i}, {j}")
                        break
                    colFlags = colFlags | (1 << position)
                    
                
                if board[j][i] != '.':
                    position = int(board[j][i])
                    if (rowFlags & (1 << position)) != 0:
                        result = False
                        #print(f"{j}, {i}")
                        break
                    rowFlags = rowFlags | (1 << position)
                
                index = (i * rowLen) + j
                k = index // unit
                l = (index % unit) + ((k // rowLen) * unit)
                k = k % rowLen
                if board[k][l] != '.':
                    position = int(board[k][l])
                    if (groupFlags & (1 << position)) != 0:
                        result = False
                        #print(f"{k}, {l}")
                        break
                    groupFlags = groupFlags | (1 << position)
                
            if not result:
                break
        
        return result
        