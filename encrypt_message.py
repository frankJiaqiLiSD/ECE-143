import random

def open_file(fname):
  """read file and return a list of lines"""
  file = open(fname, 'r')
  lines = file.readlines()
  file.close()
  return lines

def encrypt_message(message,fname):
    '''
        Given `message`, which is a lowercase string without any punctuation, and `fname` which is the
        name of a text file source for the codebook, generate a sequence of 2-tuples that
        represents the `(line number, word number)` of each word in the message. The output is a list
        of 2-tuples for the entire message. Repeated words in the message should not have the same 2-tuple.      
        :param message: message to encrypt
        :type message: str
        :param fname: filename for source text
        :type fname: str
        :returns: list of 2-tuples
    '''
    input_lst = open_file(fname)
    word_dict = {}
    for i in range(len(input_lst)):
        word_lst = input_lst[i].strip().split()
        for j in range(len(word_lst)): 
            word_lower = word_lst[j].lower()
            if word_lower not in word_dict:
                word_dict[word_lower] = [(i+1,j+1)]
            else:
                word_dict[word_lower].append((i+1,j+1))
    message_lst = message.strip().split()
    output_lst = []
    for word in message_lst:
        word_lower = word.lower()
        position = word_dict[word_lower]
        if len(position) == 1:
            output_lst.append(position[0])
        else:
            output_lst.append(random.choice(position))
    return output_lst

def decrypt_message(inlist,fname):
    '''
      Given `inlist`, which is a list of 2-tuples`fname` which is the
      name of a text file source for the codebook, return the encrypted message.      
      :param message: inlist to decrypt
      :type message: list
      :param fname: filename for source text
      :type fname: str
      :returns: string decrypted message
 '''
    input_lst = open_file(fname)
    output_lst = []
    for position in inlist:
        line_num = position[0]-1
        word_num = position[1]-1
        word_lst = input_lst[line_num].strip().split()
        output_lst.append(word_lst[word_num])
    return ' '.join(output_lst)