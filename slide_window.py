<<<<<<< HEAD
=======
<<<<<<< HEAD
def slide_window(x,width,increment):
    """Getting the number of windows first and 
    then adding the windows to the finallist."""
    window = []
    num_of_windows = (len(x)-width)//increment + 1
    for i in range(num_of_windows):
        window.append(x[i*increment:i*increment+width])
=======
>>>>>>> 6a6b10f (readme added)
def slide_window(x,width,increment):
    """Getting the number of windows first and 
    then adding the windows to the finallist."""
    window = []
    num_of_windows = (len(x)-width)//increment + 1
    for i in range(num_of_windows):
        window.append(x[i*increment:i*increment+width])
<<<<<<< HEAD
=======
>>>>>>> a185041 (Initial Commit)
>>>>>>> 6a6b10f (readme added)
    return window