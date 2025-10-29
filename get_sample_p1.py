import random

def get_sample(nbits=3,prob=None,n=1):
    """Generate samples of bitstrings of length `nbits`."""
    assert isinstance(nbits,int)
    assert isinstance(prob,dict)
    assert isinstance(n,int)
    assert nbits>0
    assert n>0
    assert len(prob) > 0
    assert len(prob)<=2**nbits

    for k,v in prob.items():
        assert isinstance(k,str)
        assert len(k)==nbits

    vals = []
    for k in prob:
        if len(prob) == 1:
            assert isinstance(prob[k],int) or isinstance(prob[k],float)
        else:
            assert isinstance(prob[k],float)
        vals.append(prob[k])

    total = sum(vals)
    assert total == 1.0
    
    bitstrings = list(prob.keys())
    probabilities = [prob[k] for k in bitstrings]
    samples = random.choices(bitstrings, weights=probabilities, k=n)
    
    return samples