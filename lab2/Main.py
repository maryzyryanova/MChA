import numpy as np

A = np.array([])
b = np.array([[1.2], [2.2], [4.0], [0], [-1.2]])
C = np.array([
    [0.01, 0, -0.02, 0, 0],
    [0.01, 0.01, -0.02, 0, 0],
    [0, 0.01, 0.01, 0, -0.02],
    [0, 0, 0.01, 0.01, 0],
    [0, 0, 0, 0.01, 0.01]
    ])
D = np.array([
    [1.33, 0.21, 0.17, 0.12, -0.13],
    [-0.13, -1.33, 0.11, 0.17, 0.12],
    [0.12, -0.13, -1.33, 0.11, 0.17],
    [0.17, 0.12, -0.13, -1.33, 0.11],
    [0.11, 0.67, 0.12, -0.13, -1.33]
    ])
A = 10*C + D

def prime_criteria(A):
    first_criteria = []
    for i in range(A.shape[0]):
        s = 0
        for j in range(A.shape[1]):
            s += np.abs(A[i][j])
        first_criteria.append(s)
    if max(first_criteria) < 1:
        return True
    second_criteria = 0
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            second_criteria += A[i][j] ** 2 
    if second_criteria < 1:
        return True
    third_criteria = []
    for j in range(A.shape[1]):
        s = 0
        for i in range(A.shape[0]):
            s += np.abs(A[i][j])
        third_criteria.append(s)  
    return max(third_criteria) < 1  

def norm(x):
    return np.sqrt(x.dot(x.T))

def prime_iteration(A, b):
    for i in range(5):
        b[i]/=A[i][i]
        A[i]/=A[i][i]
    B = np.eye(5) - A
    if not prime_criteria(B.copy()):
        print("criteria is not satisfied")
        return None
    x = np.zeros(5)
    e = 1
    interation_count = 0
    while e > 1e-4:
        x_next = B.dot(x.T) + b
        e = norm(x_next - x)
        x = x_next
        interation_count += 1
    return x, interation_count

def zeidel_criteria(A):
    first_criteria = []
    for i in range(A.shape[0]):
        s = 0
        for j in range(A.shape[1]):
            s += np.abs(A[i][j])
        first_criteria.append(s)
    if max(first_criteria) < 1:
        return True
    second_criteria = []
    for j in range(A.shape[1]):
        s = 0
        for i in range(A.shape[0]):
            s += np.abs(A[i][j])
        second_criteria.append(s)
    return max(second_criteria) < 1

def zeidel(A, b):
    for i in range(5):
        b[i]/=A[i][i]
        A[i]/=A[i][i]
    B = np.eye(5) - A
    
    if not zeidel_criteria(B.copy()):
        print("criteria is not satisfied")
        return None
    x = b.copy()
    e = 1
    interation_count = 0
    
    while e > 1e-4:
        x_prev = x.copy()
        for k in range(B.shape[0]):
            s = 0
            for i in range(k):
                s += x[i]*B[k][i]
            for i in range(k+1, B.shape[1]):
                s += x[i]*B[k][i]
            x[k] = s + b[k]
        e = norm(x_prev - x)
        interation_count += 1
    return x, interation_count

x, iters = prime_iteration(A.copy(), b.copy())
print(f"iterations = {iters}")
print(f"X = {x}")

x, iters = zeidel(A.copy(), b.copy())
print(f"iterations = {iters}")
print(f"X = {x}")