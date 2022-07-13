import numpy as np
from numpy import linalg

#lanczos iteration

def iterate(H, x, n: int):
    """
    input:
        H (2D array): Hamiltonian
        x (1D array): initalization vector
        n (int): size of system

    output:
        T (2D array): tridiagonal matrix
        K (2D array): Krylov vector
    """

