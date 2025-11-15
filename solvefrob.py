import numpy as np

def solvefrob(coefs, b):
    """Calculating all sums, check whether rem>=0 and rem%a_n==0"""
    coefs = np.array(coefs, dtype=int)
    n = len(coefs)

    if n == 1:
        a = coefs[0]
        if b % a == 0:
            return [(b // a,)]
        else:
            return []

    a_last = coefs[-1]
    others = coefs[:-1]

    maxs = b // others

    slices = [slice(0, int(m) + 1) for m in maxs]
    grids = np.ogrid[tuple(slices)] 

    shape = np.broadcast(*grids).shape
    s = np.zeros(shape, dtype=int)
    for a_i, g in zip(others, grids):
        s = s + a_i * g

    rem = b - s
    valid = (rem >= 0) & (rem % a_last == 0)

    idxs = np.nonzero(valid)
    if idxs[0].size == 0:
        return []

    x_last = (rem[valid] // a_last).astype(int)

    sols = np.vstack(list(idxs) + [x_last]).T
    return [tuple(int(v) for v in row) for row in sols]
