import numpy as np
from scipy import sparse
vector_row=np.array([3,2,1])
print(vector_row)


matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
matrix1=np.array([[1,2,3],[4,5,6],[7,8,9]])
add=matrix+matrix1
sub=matrix1-matrix
mul=matrix1*matrix
print(matrix)
print(add)
print(sub)
mul=np.dot(matrix,matrix1)
print(mul)

matrix3= np.array([[0,0,1],[1,0,0],[1,0,0]])
matrix_sparse=sparse.csr_matrix(matrix3)
print (matrix_sparse)

print(matrix3[2:3])
print(matrix3.shape)

mult=lambda arr1: arr1*5
print(mult(matrix1))
print(np.max(matrix1))
print(np.min(matrix1))
print(np.average(matrix1))
print(np.var(matrix1))
print(np.std(matrix1))
print(np.reshape(matrix1,(3,3)))
print(np.transpose(matrix1))
print(matrix1.flatten())
print(matrix1.diagonal())
print(np.linalg.eig(matrix1))
print(np.random.seed([5,2,4]))
print(np.random.normal())
print(np.random.uniform(size=2))
print(np.random.randint(low=50,high=1000,size=10))
print(matrix1.ndim)