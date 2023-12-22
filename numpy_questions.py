"""Assignment - using numpy and making a PR.

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
    # check if X a numpy array
    if not isinstance(X, np.ndarray):
        raise ValueError("input is not a numpy array")
    # check if array of 2 D
    if X.ndim != 2:
        raise ValueError("input is not 2D")
    # retourne coordonnées max
    return np.unravel_index(np.argmax(X), X.shape)


def wallis_product(n_terms):
    """
    Return the index of the maximum in a numpy array.
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
    # pi/2 formula from wallis
    range = np.arange(1, n_terms + 1, dtype=np.float64)
    n = 4 * np.power(range, 2)
    d = 4 * np.power(range, 2) - 1
    # Retourne pi.
    return 2 * np.prod(n / d)


# Test max_index
X = np.array([[0, 4], [2, 0], [4, 1], [1, 6]])

print(max_index(X))
print(X)

# Test wallis_product
print(wallis_product(100000))
