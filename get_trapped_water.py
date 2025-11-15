def get_trapped_water(seq):
    """Get the current height and sum up its differences between the previous height. """
    if not seq:
        return 0

    n = len(seq)

    left_max = [0] * n
    current_max = 0
    for i, h in enumerate(seq):
        if h > current_max:
            current_max = h
        left_max[i] = current_max

    right_max = [0] * n
    current_max = 0
    for i in range(n - 1, -1, -1):
        h = seq[i]
        if h > current_max:
            current_max = h
        right_max[i] = current_max

    water_block = 0
    for i, h in enumerate(seq):
        water_level = min(left_max[i], right_max[i])
        water_block += water_level - h

    return water_block
