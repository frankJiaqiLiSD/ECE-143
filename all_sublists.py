def all_sublists(lst):
    """Generate all non-empty sublists (subsets) of a list using recursion."""
    assert isinstance(lst, list)
    assert len(lst) > 0
    assert len(lst) == len(set(lst))
    
    if len(lst) == 1:
        return [lst[:]] 

    first = lst[0]
    rest_sublists = all_sublists(lst[1:])

    combined = [[first]] + rest_sublists + [[first] + sub for sub in rest_sublists]
    return combined