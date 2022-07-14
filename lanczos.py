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
    w = np.dot(H, V[:,0]) # new candidate vector
    alpha = np.dot(V[:,0], w) #a0 for tridiagonal matrix
    T[0,0] = alpha
    w = w - alpha*V[:,0] #gram-schmidt 

    """subsequent iterations"""
    for j in range(1,m-1):
        beta = np.sqrt(np.dot(w,w))
        V[:,j] = w / beta
       
        #gram schmidt
        for i in range(j-1):
            V[:,j] = V[:,j] - np.dot(V[:,j].conj(), V[:i])*V[:i]

        #normalize
        V[:,j] = normalize(V[:,j])

        w = np.dot(H, V[:,j])
        alpha = np.dot(V[:,0], w)
        w = w - alpha*V[:,j] - beta*V[:j-1] 

        T[j,j] = alpha
        T[j-1,j] = beta
        T[j,j-1] = beta
        
    return T, V

