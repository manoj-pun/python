# Implement MATRIX TRANSPOSE: outer = for loop, inner = while loop.
# matrix = [[1,2,3],[4,5,6],[7,8,9]] => result = [[1,4,7],[2,5,8],[3,6,9]]

matrix = [[1,2,3],[4,5,6],[7,8,9]]

result = []

cols = len(matrix[0])
rows = len(matrix)

for i in range(cols):  
    new_row = []
    
    j = 0
    while j < rows:     
        new_row.append(matrix[j][i])
        j += 1
    
    result.append(new_row)

print(result)