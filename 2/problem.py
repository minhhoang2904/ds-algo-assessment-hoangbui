class Solution:
    def isValidSudoku(self, matrix):
         # Time complexity: O(n)
        # Space complexity: 
        
        # Remove pass and write code here
        for i in range(9):
            row = []
            for j in range(9):
                if matrix[i][j]!= ".":
                    row.append(matrix[i][j])
            if (len(row) != len(set(row))):
                return False
            
        for i in range(9):
            col = []
            for j in range(9):
                if matrix[i][j]!= ".":
                    col.append(matrix[i][j])
            if (len(row) != len(set(row))):
                return False
        
        for box_r in range(0, 9, 3):
            for box_c in range(0, 9, 3):
                block = []
                for i in range(box_r, box_r + 3):
                    for j in range(box_c, box_c + 3):
                        if matrix[i][j] != '.':
                            block.append(matrix[i][j])
                if len(block) != len(set(block)):
                    return False
                
        return True
    

