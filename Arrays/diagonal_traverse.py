class Solution(object):
    def findDiagonalOrder(self, mat):

        # Get number of rows in the matrix
        rows = len(mat)

        # Get number of columns in the matrix
        cols = len(mat[0])

        # This will store the final diagonal traversal result
        result = []

        # Total diagonals in a matrix = rows + cols - 1
        for d in range(rows + cols - 1):

            # Temporary list to store elements of the current diagonal
            temp = []

            # Determine the starting position of the diagonal

            # If diagonal index is within the number of columns
            # start from top row
            row = 0 if d < cols else d - cols + 1

            # If diagonal index is within columns use d
            # otherwise start from the last column
            col = d if d < cols else cols - 1

            # Traverse along the diagonal
            # Move down-left direction (row+1, col-1)
            while row < rows and col >= 0:
                temp.append(mat[row][col])  # add element to temp list
                row += 1                    # move downward
                col -= 1                    # move left

            # For even-numbered diagonals we reverse the order
            # because traversal direction alternates
            if d % 2 == 0:
                temp.reverse()

            # Add the processed diagonal elements to the final result
            result.extend(temp)

        # Return the final diagonal traversal
        return result

num = [[1,2,3],[4,5,6],[7,8,9]]
sol = Solution()
print("Diagonal traverse is:", sol.findDiagonalOrder(num))