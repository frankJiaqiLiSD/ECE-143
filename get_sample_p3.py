from get_sample_p1 import *
from get_sample_p2 import *

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

if __name__ == "__main__":
    x=get_sample(nbits=2,prob={'00':1/4,'01':1/4,'10':1/4,'11':1/4},n=20)
    print(x)
    print(gather_values(x))