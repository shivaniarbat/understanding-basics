import numpy as np
from numpy import dot

# define an array
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(A)

# calculate eigendecomposition
values,vectors = np.linalg.eig(A)

# A.v = λ.v
# A is square matrix 
# v is of size of A
# λ (eigen values) is usually a list 
# so for the given example the 
#           first eigenvector is vectors[:, 0] and eigenvalues is values[0]
#           second eigenvector is vectors[:, 1] and eigenvalues is values[2]
#           third eigenvector is vectors[:, 2] and eigenvalues is values[2]

# verify eigendecomposition 
# first 
print(A.dot(vectors[:,0]))
print(vectors[:,0] * values[0])

# second 
print(A.dot(vectors[:,1]))
print(vectors[:,1] * values[1])

# third 
print(A.dot(vectors[:,2]))
print(vectors[:,2] * values[2])

# reconstruct the original matrix 
Q = vectors
R = np.linalg.inv(Q)
L = np.diag(values)

A_old = Q.dot(L).dot(R)
print(A_old)
