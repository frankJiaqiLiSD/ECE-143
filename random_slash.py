import numpy as np

def gen_rand_slash(m=6, n=6, direction='back'):
    """
    Generate an m x n array with a random contiguous slash (\ or /)
    of length at least 2.
    """
    x = np.zeros((m, n), dtype=int)
    assert direction in ["back","forward"]

    if direction == 'back':
        dr, dc = 1, 1   # \
    elif direction == 'forward':
        dr, dc = 1, -1  # /

    # Collect all possible slashes as (start_row, start_col, length)
    options = []
    assert direction in ["back","forward"]
    for i in range(m):
        for j in range(n):
            # Find maximum possible length starting at (i, j)
            r, c = i, j
            max_len = 0
            while 0 <= r < m and 0 <= c < n:
                max_len += 1
                r += dr
                c += dc

            # Add all segments with length >= 2
            for L in range(2, max_len + 1):
                options.append((i, j, L))
    assert len(options)>=0

    # Pick one slash uniformly at random
    i0, j0, L = options[np.random.randint(len(options))]

    # Draw it
    r, c = i0, j0
    for _ in range(L):
        x[r, c] = 1
        r += dr
        c += dc

    return x
