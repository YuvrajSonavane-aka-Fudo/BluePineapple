import numpy as np
'''
Generate two matrices A (3 ,4) and B(4,2).
Compute A @ B.
Verify properties: (A.T).T equals A; create identity matrix I and show A 
@ I (shape permitting).
'''

A = np.random.randint(0,10 , size = (3,4))
B = np.random.randint(0,10, size = (4,2))

print(f"Matrix A is => {A}\n")
print(f"Matrix B is => {B}\n")

#*A.B
C = A @ B
print(f"A @ B is => {C}\n")

#*Checking if Transpose of transpose of A is equal to A
A_T_T = A.T.T
print(f"(A.T).T == A ? : {np.array_equal(A,A_T_T)}")

identity_matrix = np.eye(4 , dtype = int)
I = A @ identity_matrix
print(f"A @ I == A ? : {np.array_equal(A , I)}")





