"""Assignment - using numpy and making a PR.#

The goals of this assignment are:
    * Use numpy in practice with two easy exercises.
    * Use automated tools to validate the code (`pytest` and `flake8`)
    * Submit a Pull-Request on github to practice `git`.

#The two functions below are skeleton functions. The docstrings explain what
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
    # Check if the input is a numpy array
    if not isinstance(X, np.ndarray):
        raise ValueError("The input must be a numpy array")

    # Check if the shape is 2D
    if len(X.shape) != 2:
        raise ValueError("The shape must be 2D")

    # Find the index of the maximum value using np.argmax
    # np.argmax returns the index of the maximum value along an axis
    # By default, the index is into the flattened array
    # To get the row and column index, we can use np.unravel_index
    # np.unravel_index converts a flat index into an index tuple
    # It takes the shape of the array as an argument
    i, j = np.unravel_index(np.argmax(X), X.shape)

    return i, j



def wallis_product(n_terms: int) -> float:
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
    pi = 2.0
    for i in range(1, n_terms + 1):
        pi *= (4 * i ** 2) / (4 * i ** 2 - 1)
    return pi


