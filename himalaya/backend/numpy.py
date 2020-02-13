import numpy as np


def apply_argmax(array, argmax, axis):
    """Apply precomputed argmax indices in multi dimension arrays

    array[np.argmax(array)] works fine in dimension 1, but not in higher ones.
    This function extends it to higher dimensions.

    Example
    -------
    >>> import numpy as np
    >>> array = np.random.randn(10, 4, 8)
    >>> argmax = np.argmax(array, axis=1)
    >>> max_ = apply_argmax(array, argmax, axis=1)
    >>> assert np.all(max_ == np.max(array, axis=1))
    """
    argmax = np.expand_dims(argmax, axis=axis)
    max_ = np.take_along_axis(array, argmax, axis=axis)
    return np.take(max_, 0, axis=axis)


###############################################################################

argmax = np.argmax
assert_array_equal = np.testing.assert_array_equal
max = np.max
randn = np.random.randn
matmul = np.matmul
norm = np.linalg.norm
transpose = np.transpose
