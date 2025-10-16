<<<<<<< HEAD
=======
<<<<<<< HEAD
def compute_average_word_length(instring, unique=False):
    """Compute the average word length in a string.

    Words are defined by whitespace splitting (i.e., `str.split()`), so any
    punctuation attached to a token is counted toward its length (e.g., `"hi!"`
    has length 3). If `unique=True`, only distinct word tokens are considered
    (string equality, case-sensitive), achieved by converting the list of words
    to a `set`.

    Args:
        instring (str): The input string to analyze.
        unique (bool, optional): If True, consider each distinct word only once.
            Defaults to False.

    Returns:
        float: The average length of the considered words. Returns `0.0` if the
        string contains no words (e.g., empty or whitespace-only).

    Raises:
        AssertionError: If `instring` is not a `str`.
        AssertionError: If `unique` is not a `bool`.

    Examples:
        >>> compute_average_word_length("a bb ccc")
        2.0
        >>> compute_average_word_length("a a bb", unique=True)
        1.5
        >>> compute_average_word_length("")
        0.0
        >>> compute_average_word_length("Hi, hi", unique=True)  # "Hi," and "hi"
        2.5
    """
    assert isinstance(instring, str), "Input must be a string"
    assert isinstance(unique, bool), "Unique must be a boolean"

    words = instring.split()
    if unique:
        words = set(words)

    total_length = 0
    for word in words:
        total_length += len(word)

    if len(words) == 0:
        return 0.0
    else:
        average_length = total_length / len(words)

    return average_length
=======
>>>>>>> 6a6b10f (readme added)
def compute_average_word_length(instring, unique=False):
    """Compute the average word length in a string.

    Words are defined by whitespace splitting (i.e., `str.split()`), so any
    punctuation attached to a token is counted toward its length (e.g., `"hi!"`
    has length 3). If `unique=True`, only distinct word tokens are considered
    (string equality, case-sensitive), achieved by converting the list of words
    to a `set`.

    Args:
        instring (str): The input string to analyze.
        unique (bool, optional): If True, consider each distinct word only once.
            Defaults to False.

    Returns:
        float: The average length of the considered words. Returns `0.0` if the
        string contains no words (e.g., empty or whitespace-only).

    Raises:
        AssertionError: If `instring` is not a `str`.
        AssertionError: If `unique` is not a `bool`.

    Examples:
        >>> compute_average_word_length("a bb ccc")
        2.0
        >>> compute_average_word_length("a a bb", unique=True)
        1.5
        >>> compute_average_word_length("")
        0.0
        >>> compute_average_word_length("Hi, hi", unique=True)  # "Hi," and "hi"
        2.5
    """
    assert isinstance(instring, str), "Input must be a string"
    assert isinstance(unique, bool), "Unique must be a boolean"

    words = instring.split()
    if unique:
        words = set(words)

    total_length = 0
    for word in words:
        total_length += len(word)

    if len(words) == 0:
        return 0.0
    else:
        average_length = total_length / len(words)

    return average_length
<<<<<<< HEAD
=======
>>>>>>> a185041 (Initial Commit)
>>>>>>> 6a6b10f (readme added)
