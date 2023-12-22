import numpy as np


def max_index(X):
    """Return the index of the maximum in a numpy array.

    Parameters
    ----------
    X : ndarray of shape (n_samples, n_features)
        The input array.

    Returns
    -------
    (i, j) : tuple(int)
        The row and columnd index of the maximum.

    Raises
    ------
    ValueError
        If the input is not a numpy array or
        if the shape is not 2D.
    """    
    if not isinstance(X, np.ndarray):
            raise ValueError("L'imput doit être un array numpy")
    
    if X.ndim != 2:
        raise ValueError("L'array doit être en 2D")
    # On trouve l'index du max
    max_index = np.argmax(X)

    # On convertit max_index en 
    max_coords = np.unravel_index(max_index, X.shape)

    return max_coords 


def wallis_product(n_terms):
    """Implement the Wallis product to compute an approximation of pi.

    See:
    https://en.wikipedia.org/wiki/Wallis_product

    Parameters
    ----------
    n_terms : int
        Number of steps in the Wallis product. Note that `n_terms=0` will
        consider the product to be `1`.

    Returns
    -------
    pi : float
        The approximation of order `n_terms` of pi using the Wallis product.
    """
    pi=1    
    #Calcul du produit 
    for i in range(1,n_terms+1):
        
        pi=pi*((2*i/((2*i)-1))) *((2*i/((2*i)+1)))    
    return pi*2