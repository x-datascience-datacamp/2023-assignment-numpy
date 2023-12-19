"""

Thierry-Séphine GOMA-LEGERNARD
@Sephine-1st GitHub

Assignment - using numpy and making a PR.

The goals of this assignment are:
    * Use numpy in practice with two easy exercises.
    * Use automated tools to validate the code (`pytest` and `flake8`)
    * Submit a Pull-Request on github to practice `git`.

The two functions below are skeleton functions. The docstrings explain what
are the inputs, the outputs and the expected error. Fill the function to
complete the assignment. The code should be able to pass the test that we
wrote. To run the tests, use `pytest test_numpy_question.py` at the root of
the repo. It should say that 2 tests ran with success.

We also ask to respect the pep8 convention: https://pep8.org.
This will be enforced with `flake8`. You can check that there is no flake8
errors by calling `flake8` at the root of the repo.

"""
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
    i = 0
    j = 0

    # We check if input is a numpy array
    if not isinstance(X, np.ndarray):
        raise ValueError("Input must be a numpy array.")

    # We check if the shape is 2D
    if X.ndim != 2:
        raise ValueError("Input array must be 2D.")

    # We find the indices of the maximum element using argmax
    i, j = np.unravel_index(np.argmax(X, axis=None), X.shape)

    return i, j


def wallis_product(n_terms):
    """Implement the Wallis product to compute an approximation of pi.

    See:
    https://en.wikipedia.org/wiki/Wallis_product

    Parameters
    ----------
    n_terms : int
        Number of steps in the Wallis product. Note that `n_terms=0` will
        consider the product to be `1`.(This instruction is not clear!).

    Returns
    -------
    pi : float
        The approximation of order `n_terms` of pi using the Wallis product.
    """
    if n_terms == 0:
        pi_approximation = 2.0
    else:
        # We initialize the Wallis product
        res_wallis_product = 1.0
        # We calculate the Wallis product to estimate pi/2
        for k in range(1, n_terms + 1):
            num_k = (4.0 * (k**2))
            denom_k = num_k - 1
            term_k = num_k / denom_k
            res_wallis_product *= term_k
        # Finally, we get the final approximation of pi
        pi_approximation = 2 * res_wallis_product
    return pi_approximation
