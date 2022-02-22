#Gauss Method for solving SLAE
 
def gaussMethod(matrixA, b):
    for i in range(1, matrixA.shape[0]):
        for j in range(i, matrixA.shape[0]):
            if (matrixA[i-1][i-1] != 0):
                q = matrixA[j][i-1] / matrixA[i-1][i-1]
                b[j] -= round(q * b[i-1], 4)
                for k in range(matrixA.shape[0]):
                    matrixA[j][k] = round((matrixA[j][k] - q * matrixA[i-1][k]), 4)

    print(f"\nMatrix A after the straight stroke: \n{matrixA}")
    print(f"\nMatrix b after the straight stroke: \n{b}\n")

    x = [0 for i in range(matrixA.shape[0])] #the list of the koeffs
    for i in range(matrixA.shape[0] - 1, -1, -1):
        if(matrixA[i][i] != 0):
            x[i] = int(((b[i] - sum([matrixA[i][j] * x[j] for j in range(i+1, matrixA.shape[0])]))/matrixA[i][i]) * 10000) / 10000
    print("The result:")
    for i in range(matrixA.shape[0]):
        print(f"x[{i+1}] = {x[i]}")

    return x