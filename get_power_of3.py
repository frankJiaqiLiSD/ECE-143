<<<<<<< HEAD
=======
<<<<<<< HEAD
from itertools import product

def get_power_of3(n): 
    """Finds a representation of n as a sum of powers of 3 with coefficients -1, 0, or 1."""
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if not (1 <= n <= 40):
        raise ValueError("n must be between 1 and 40 (inclusive)")

    weights = [1, 3, 9, 27]
    for pair in product([-1, 0, 1], repeat=4):
        pairs_iter = zip(pair, weights)
        total = 0                        
        for c, w in pairs_iter:
            total += c * w

        if total == n:
            return list(pair)

=======
>>>>>>> 6a6b10f (readme added)
from itertools import product

def get_power_of3(n): 
    """Finds a representation of n as a sum of powers of 3 with coefficients -1, 0, or 1."""
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if not (1 <= n <= 40):
        raise ValueError("n must be between 1 and 40 (inclusive)")

    weights = [1, 3, 9, 27]
    for pair in product([-1, 0, 1], repeat=4):
        pairs_iter = zip(pair, weights)
        total = 0                        
        for c, w in pairs_iter:
            total += c * w

        if total == n:
            return list(pair)

<<<<<<< HEAD
=======
>>>>>>> a185041 (Initial Commit)
>>>>>>> 6a6b10f (readme added)
    return None