<<<<<<< HEAD
=======
<<<<<<< HEAD
def write_columns(data,fname):
    """Write three columns to a file: the original data, the square of the data,
    and the result of a specific formula applied to the data."""
    with open(fname, 'w') as f:
        for value in data:
            squared = value ** 2
            formula_result = (value + squared) / 3
=======
>>>>>>> 6a6b10f (readme added)
def write_columns(data,fname):
    """Write three columns to a file: the original data, the square of the data,
    and the result of a specific formula applied to the data."""
    with open(fname, 'w') as f:
        for value in data:
            squared = value ** 2
            formula_result = (value + squared) / 3
<<<<<<< HEAD
=======
>>>>>>> a185041 (Initial Commit)
>>>>>>> 6a6b10f (readme added)
            f.write(f"{value:.2f},{squared:.2f},{formula_result:.2f}\n")