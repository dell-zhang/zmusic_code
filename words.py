#! /usr/bin/env python
"""
@author: dell
"""

import csv
import cPickle as pickle

# global variables
word_dict = {}

def get_int_attr(attr):
    if attr:
        return int(attr)
    else:
        return -1

def get_flt_attr(attr):
    if attr:
        return float(attr)
    else:
        return -1.0

def read_words(csv_filename):
    csv_file = open(csv_filename, 'rb')
    reader = csv.reader(csv_file)
    reader.next()  # ignore header
    for row in reader:
        artist_id   = int(row[0])
        user_id     = int(row[1])  
        word = {}
        word['heard-of']            = get_int_attr(row[2])
        word['own-artist-music']    = get_int_attr(row[3])
        word['like-artist']         = get_flt_attr(row[4])
        for j in range(81):
            word['w%d' % (j+1)] = get_int_attr(row[5+j])
        word_dict[(artist_id,user_id)] = word
    csv_file.close()

def load_words(pkl_filename):
    global word_dict
    pkl_file = open(pkl_filename, 'rb')
    word_dict = pickle.load(pkl_file)
    pkl_file.close()

def save_words(pkl_filename):
    pkl_file = open(pkl_filename, 'wb')
    pickle.dump(word_dict, pkl_file, -1)
    pkl_file.close()

if __name__ == "__main__":
    read_words('data/words.csv')
    save_words('data/words.pkl')
