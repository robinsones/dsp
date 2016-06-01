# Matrix Algebra

import numpy as np
## Define matrices and arrays

A = np.matrix( ((1, 2, 3), (2, 7, 4)))
B = np.matrix( ((1, -1), (0, 1)))
C = np.matrix( ((5, -1), (9, 1), (6, 0) ))
D = np.matrix( ((3, -2, -1), (1, 2, 3)))
u = np.array([[6, 2, -3, 5]]) 
v = np.array([[3, 5, -1, 4]]) 
w = np.array([[1], [8], [0], [5]]) 

#### Matrix Dimensions

# 1.1)
np.shape(A)
# 2x3

#1.2)
np.shape(B)
#2x2

#1.3)
np.shape(C)
# 3x2

# 1.4) 
np.shape(D)
# 2x3

# 1.5)
np.shape(u)
# 1x4

#1.6) 
np.shape(w)
# 4x1


### Vector operations

# 2.1)
u + v
# array([[ 9,  7, -4,  9]])

# 2.2)
u - v
# array([[ 3, -3, -2,  1]])

# 2.3)
6*u
# array([[ 36,  12, -18,  30]])

# 2.4)
np.inner(u, v)
# array([[51]])

# 2.5)
np.linalg.norm(u)
# 8.6023252670426267

### Matrix operations

# 3.1) 
A + C 
# not defined

# 3.2) 
A - np.transpose(C) 

"""
matrix([[-4, -7, -3],
        [ 3,  6,  4]])
"""

# 3.3) 
np.transpose(C) + 3*D
"""
matrix([[14,  3,  3],
        [ 2,  7,  9]])
"""
# 3.4) 
B*A
"""
matrix([[-1, -5, -1],
        [ 2,  7,  4]])
"""

# 3.5) 
B*np.transpose(A)
# not defined

### Optional 

# 3.6) 
B*C
# not defined

# 3.7) 
C*B
""" 
matrix([[ 5, -6],
        [ 9, -8],
        [ 6, -6]])
"""

# 3.8) 
np.linalg.matrix_power(B, 4)
"""
matrix([[ 1, -4],
        [ 0,  1]])
"""
# 3.9) 
A*np.transpose(A)
# matrix([[14, 28],
#        [28, 69]])
# 3.10) 
np.transpose(D)*D
"""
matrix([[10, -4,  0],
        [-4,  8,  8],
        [ 0,  8, 10]])
"""
