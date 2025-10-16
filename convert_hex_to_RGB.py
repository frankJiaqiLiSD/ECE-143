<<<<<<< HEAD
=======
<<<<<<< HEAD
def convert_hex_to_RGB(code_list):
    rgb = []
    """
    Converts a list of hexadecimal color codes to a list of RGB tuples.
    Each hexadecimal code must be a string starting with '#' followed by 
    six hexadecimal characters (e.g., '#RRGGBB').
    Args:
        code_list (list): A list of strings, where each string is a hex color code.
    Returns:
        list: A list of tuples, where each tuple contains three integers 
              representing the (Red, Green, Blue) values (0-255).
    """
    for hex_code in code_list:
        hex_code = hex_code[1:]
        r = int(hex_code[0:2], 16)
        g = int(hex_code[2:4], 16)
        b = int(hex_code[4:6], 16)
        rgb.append((r, g, b))
=======
>>>>>>> 6a6b10f (readme added)
def convert_hex_to_RGB(code_list):
    rgb = []
    """
    Converts a list of hexadecimal color codes to a list of RGB tuples.
    Each hexadecimal code must be a string starting with '#' followed by 
    six hexadecimal characters (e.g., '#RRGGBB').
    Args:
        code_list (list): A list of strings, where each string is a hex color code.
    Returns:
        list: A list of tuples, where each tuple contains three integers 
              representing the (Red, Green, Blue) values (0-255).
    """
    for hex_code in code_list:
        hex_code = hex_code[1:]
        r = int(hex_code[0:2], 16)
        g = int(hex_code[2:4], 16)
        b = int(hex_code[4:6], 16)
        rgb.append((r, g, b))
<<<<<<< HEAD
=======
>>>>>>> a185041 (Initial Commit)
>>>>>>> 6a6b10f (readme added)
    return rgb