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

def map_bitstring(bitstring_lst):
    """Map each bitstring to 0 or 1 based on the count of '0's and '1's."""
    # Making sure everything is valid
    assert isinstance(bitstring_lst,list)
    for bitstring in bitstring_lst:
        assert isinstance(bitstring,str)
        assert len(bitstring_lst)>0
        assert len(bitstring)==len(bitstring_lst[0])
        for i in bitstring:
            assert i in ['0','1']
    
    output_map = {}
    for bitstring in bitstring_lst:
        if bitstring.count('0') > bitstring.count('1'):
            output_map[bitstring] = 0
        else:
            output_map[bitstring] = 1
    return output_map


def gather_values(x):
    """Given a list of bitstrings `x`, gather the values into a dictionary"""

    assert isinstance(x,list)
    assert len(x)>0
    for s in x:
        assert isinstance(s,str)
        assert len(s)==len(x[0])
        for i in s:
            assert i in ['0','1']

    map = map_bitstring(x)
    out_dict = {}
    for k in map:
        k_lst = []
        for s in x:
            if k == s:
                k_lst.append(map[s])
        out_dict[k] = k_lst
    return out_dict


def threshold_values(seq, threshold=1):
    """Given a list of bitstrings `seq`, return a dictionary with the highest number of 1s per bitstring key."""

    assert isinstance(seq, list)
    assert len(seq) > 0
    assert isinstance(threshold, int) and threshold > 0
    assert len(seq[0]) > 0
    for s in seq:
        assert isinstance(s, str)
        assert len(s) == len(seq[0])
        for ch in s:
            assert ch in ('0', '1')

    sorted_seq = sorted(seq)
    value_gathered_dict = gather_values(sorted_seq)
    ranking_dict = {}
    for key in value_gathered_dict:
        ranking_dict[key] = sum(value_gathered_dict[key])
    sorted_val=sorted(ranking_dict,key=lambda x:ranking_dict[x],reverse=True)
    output_dict = {}
    for i in range(threshold):
        output_dict[sorted_val[i]] = 1
    for j in range(threshold, len(sorted_val)):
        output_dict[sorted_val[j]] = 0
    return output_dict
