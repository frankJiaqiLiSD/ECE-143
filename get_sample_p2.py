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
