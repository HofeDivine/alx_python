def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        matrixSquare = []
        for i in row:
          matrixSquare.append(i**2)      
        new_matrix.append(matrixSquare)
               
    return new_matrix