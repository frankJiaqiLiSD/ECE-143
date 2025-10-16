<<<<<<< HEAD
=======
<<<<<<< HEAD
def write_chunks_of_five(words,fname):
    """Write words to a file in chunks of five per line."""
    file = open(fname, 'w')
    for i in range(0, len(words), 5):
        chunk = words[i:i+5]
        single_line = ' '.join(chunk)
        file.write(single_line + '\n')
    file.close()

# def main():
#     in_file = open('word_list.txt', 'r')
#     words = [line.strip() for line in in_file]
#     write_chunks_of_five(words,'chunks_of_five.txt')
#     in_file.close()

# if __name__ == "__main__":
=======
>>>>>>> 6a6b10f (readme added)
def write_chunks_of_five(words,fname):
    """Write words to a file in chunks of five per line."""
    file = open(fname, 'w')
    for i in range(0, len(words), 5):
        chunk = words[i:i+5]
        single_line = ' '.join(chunk)
        file.write(single_line + '\n')
    file.close()

# def main():
#     in_file = open('word_list.txt', 'r')
#     words = [line.strip() for line in in_file]
#     write_chunks_of_five(words,'chunks_of_five.txt')
#     in_file.close()

# if __name__ == "__main__":
<<<<<<< HEAD
=======
>>>>>>> a185041 (Initial Commit)
>>>>>>> 6a6b10f (readme added)
#     main()