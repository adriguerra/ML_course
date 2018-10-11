# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np


def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree."""
    poly = np.ones((len(x), 1))
    for deg in range(1, degree+1):
        poly = np.c_[poly, np.power(x, deg)]

#     N = x.shape[0]
#     print('N: '+ str(N))
#     print('x:' + str(x))
#     print('degree:' + str(degree))
    
#     result = np.zeros((N, degree+1))
#     for i in range(N):
#         for j in range(degree+1):
#             print('x_i:' + str(x[i]))
#             print('j:' + str(j))
#             result[i][j] = x[i]**j
#             print('curr:' + str(result[i][j]))
    return poly
