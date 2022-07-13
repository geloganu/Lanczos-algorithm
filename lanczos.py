import numpy as np
from numpy import linalg

#normalization
def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0: 
       return v
    return v / norm


#lanczos iteration
def iterate(H, x, m: int):
    """
    input:
        H (nXn array): Hamiltonian
        x (n 1D array): initalization vector
        m (int): size of system

    output:
        T (2D array): tridiagonal matrix
        K (2D array): Krylov subspace (equal to Q in tutorial)

        where T = K* H K
    """
    n = len(H)

    #ensure n>=m
    if m>n:
        m = n

    T = np.zeros((m,m))
    V = np.zeros((n,m))
    x =  normalize(x) #first krylov vector
    xt = np.transpose(x) #first krylov vector transpose
    V[:,0] = xt #first krylov subspace basis vector

    """first iteration"""
    w = np.dot(H, xt) # new candidate vector
    alpha = np.dot(xt.conj(), w) #a0 for tridiagonal matrix
    T[0,0] = alpha

    """subsequent iterations"""
    for j in range(1,m):
        w = np.dot()



