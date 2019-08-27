# understanding-basics
Understanding basics of Machine Learning Topics. 

## Eigendecomposition
[for theory](https://machinelearningmastery.com/introduction-to-eigendecomposition-eigenvalues-and-eigenvectors/)

## Reconstructing original matrix 
    # create matrix from eigenvectors
    Q = vectors
    # create inverse of eigenvectors matrix
    R = inv(Q)
    # create diagonal matrix from eigenvalues
    L = diag(values)
    # reconstruct the original matrix
    B = Q.dot(L).dot(R)
