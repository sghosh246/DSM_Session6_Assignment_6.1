# -*- coding: utf-8 -*-
"""
Created on Wed May 1 11:10:24 2018
@author: sourav ghosh
"""
"""
Write a function so that the columns of the output matrix are powers of the input
vector.
The order of the powers is determined by the increasing boolean argument. Specifically,
when increasing is False, the i-th output column is the input vector raised element-wise
to the power of N - i - 1.
HINT: Such a matrix with a geometric progression in each row is named for Alexandre-Theophile Vandermonde.
"""
import numpy as np
def out_matrix(in_vector):
    x = np.array(in_vector)
    N=len(x)
    '''
    Iterating through each element of the vector and applying exponential operation on each of the element with operand starting from 0 to n-1th element
    and populating the result in a 2D array. Finally applied Transpose function on the resultant 2D array to obtain the desired output with increasing geometric progression as per Vandermonde Matrix Theory
    '''
    #y = np.array([x**(N-i-1) for i in range(N)]) # Implementing Decreasing boolean argument
    y = np.array([x**i for i in range(N)])
    return(y.T)
in_vector = [1,4,5,7]
print(out_matrix(in_vector)) 