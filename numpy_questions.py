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
        The row and column index of the maximum.

    Raises
    ------
    ValueError
        If the input is not a numpy array or
        if the shape is not 2D.
    """
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        raise ValueError("Input must be a 2D numpy array.")

    i, j = np.unravel_index(np.argmax(X), X.shape)
    return i, j

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
    if not isinstance(n_terms, int) or n_terms < 0:
        raise ValueError("Number of terms must be a non-negative integer.")

    if n_terms == 0:
        return 2.0

    terms = np.arange(1, n_terms + 1).astype(np.float64)
    print(terms)
    wallis_array = (4.0 * terms ** 2) / ((4.0 * terms ** 2) - 1)
    pi_approximation = 2.0 * np.prod(wallis_array)
    print(n_terms)
    print(pi_approximation)
    return pi_approximation
