def is_perfect(n):
    """ First find all proper divisors of the number, then sum up to see if it equals to n."""
    assert isinstance(n, int)
    assert n > 0
    divisors = []
    for i in range(1, n):
        if n%i == 0:
            divisors.append(i)
    return sum(divisors) == n