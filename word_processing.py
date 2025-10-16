<<<<<<< HEAD
=======
<<<<<<< HEAD
def get_average_word_length(words):
    """Calculate the average length of words in a list."""
    total_length = 0
    for word in words:
        total_length += len(word)
    average_length = total_length / len(words) if words else 0
    return average_length

def get_longest_word(words):
    """Find the longest word in a list of words."""
    longest_word = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

def get_longest_words_startswith(words,start):
    """Find the longest word in a list that starts with a specific letter."""
    longest_word = ""
    for word in words:
        if(word[0]==start and len(word)>len(longest_word)):
            longest_word=word
    return longest_word

def get_most_common_start(words):
    """Find the most common starting letter among a list of words."""
    start_letters = {}
    most_start = ""
    for word in words:
        start_letter = word[0]
        if start_letter in start_letters:
            start_letters[start_letter] += 1
        else:
            start_letters[start_letter] = 1
    for letter in start_letters:
        if start_letters[letter]>start_letters.get(most_start,0):
            most_start=letter
    return most_start

def get_most_common_end(words):
    """Find the most common ending letter among a list of words."""
    end_letters = {}
    most_end = ""
    for word in words:
        end_letter = word[-1]
        if end_letter in end_letters:
            end_letters[end_letter] += 1
        else:
            end_letters[end_letter] = 1
    for letter in end_letters:
        if end_letters[letter]>end_letters.get(most_end,0):
            most_end=letter
    return most_end

# def main():
#     file = open('word_list.txt', 'r')
#     words = [line.strip() for line in file]
#     print("Average word length:", get_average_word_length(words))
#     print("Longest word:", get_longest_word(words))
#     print("Longest word starting with 'a':", get_longest_words_startswith(words,'a'))
#     print("Most common starting letter:", get_most_common_start(words))
#     print("Most common ending letter:", get_most_common_end(words))
#     file.close()

# if __name__ == "__main__":
=======
>>>>>>> 6a6b10f (readme added)
def get_average_word_length(words):
    """Calculate the average length of words in a list."""
    total_length = 0
    for word in words:
        total_length += len(word)
    average_length = total_length / len(words) if words else 0
    return average_length

def get_longest_word(words):
    """Find the longest word in a list of words."""
    longest_word = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

def get_longest_words_startswith(words,start):
    """Find the longest word in a list that starts with a specific letter."""
    longest_word = ""
    for word in words:
        if(word[0]==start and len(word)>len(longest_word)):
            longest_word=word
    return longest_word

def get_most_common_start(words):
    """Find the most common starting letter among a list of words."""
    start_letters = {}
    most_start = ""
    for word in words:
        start_letter = word[0]
        if start_letter in start_letters:
            start_letters[start_letter] += 1
        else:
            start_letters[start_letter] = 1
    for letter in start_letters:
        if start_letters[letter]>start_letters.get(most_start,0):
            most_start=letter
    return most_start

def get_most_common_end(words):
    """Find the most common ending letter among a list of words."""
    end_letters = {}
    most_end = ""
    for word in words:
        end_letter = word[-1]
        if end_letter in end_letters:
            end_letters[end_letter] += 1
        else:
            end_letters[end_letter] = 1
    for letter in end_letters:
        if end_letters[letter]>end_letters.get(most_end,0):
            most_end=letter
    return most_end

# def main():
#     file = open('word_list.txt', 'r')
#     words = [line.strip() for line in file]
#     print("Average word length:", get_average_word_length(words))
#     print("Longest word:", get_longest_word(words))
#     print("Longest word starting with 'a':", get_longest_words_startswith(words,'a'))
#     print("Most common starting letter:", get_most_common_start(words))
#     print("Most common ending letter:", get_most_common_end(words))
#     file.close()

# if __name__ == "__main__":
<<<<<<< HEAD
=======
>>>>>>> a185041 (Initial Commit)
>>>>>>> 6a6b10f (readme added)
#     main()