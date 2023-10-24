# https://github.com/spro/char-rnn.pytorch

import unidecode
import string
import random
import time
import math
import torch
import itertools

# Reading and un-unicode-encoding data

#在这里设置我自己认为的可能的字符串
characters = 'ABCDEFGHIJKL'
permutations_2 = list(itertools.permutations(characters, 2))
all_characters = ['AA','BB','CC','DD','EE','FF','GG','HH','II','JJ','KK','LL']
for p in permutations_2:
    all_characters.append(''.join(p))
#all_characters = string.printable
#all_characters = "ABCDEFGHIJKL"
n_characters = len(all_characters)

def read_file(filename):
    file = unidecode.unidecode(open(filename).read())
    return file, len(file)

# Turning a string into a tensor

def char_tensor(string):
    tensor = torch.zeros(len(string)).long()
    for c in range(len(string)):
        try:
            tensor[c] = all_characters.index(string[c])
        except:
            continue
    return tensor

# Readable time elapsed

def time_since(since):
    s = time.time() - since
    m = math.floor(s / 60)
    s -= m * 60
    return '%dm %ds' % (m, s)

