# What is Laplacian Matrix 


## Laplacian Matrix
    The Laplacian matrix, sometimes also called the admittance matrix (Cvetković et al. 1998, Babić et al. 2002) or Kirchhoff matrix, of a graph G, where G=(V,E) is an undirected, unweighted graph without graph loops (i,i) or multiple edges from one node to another, V is the vertex set, n=|V|, and E is the edge set, is an n×n symmetric matrix with one row and column for each node defined by

`L=D-A,`	                                    (1)
```
where D=diag(d_1,...,d_n) is the degree matrix, which is the diagonal matrix formed from the vertex degrees and A is the adjacency matrix. The diagonal elements l_(ij) of L are therefore equal the degree of vertex v_i and off-diagonal elements l_(ij) are -1 if vertex v_i is adjacent to v_j and 0 otherwise.

```

##### The Laplacian matrix of a graph is implemented in the Wolfram Language as KirchhoffMatrix[g].

### A normalized version of the Laplacian matrix, denoted L, is similarly defined by

http://mathworld.wolfram.com/images/equations/LaplacianMatrix/NumberedEquation2.gif
(Chung 1997, p. 2).

The Laplacian matrix is a discrete analog of the Laplacian operator in multivariable calculus and serves a similar purpose by measuring to what extent a graph differs at one vertex from its values at nearby vertices. The Laplacian matrix arises in the analysis of random walks and electrical networks on graphs (Doyle and Snell 1984), and in particular in the computation of resistance distances. The Laplacian also appears in the matrix tree theorem.
