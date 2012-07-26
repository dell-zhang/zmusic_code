#! /usr/bin/env python
"""
@author: dell
"""

import csv
import cPickle as pickle
from collections import defaultdict

# global variables
word_dict = defaultdict(dict)

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
    global word_dict
    word_a_dict = {}
    word_a_dict['heard-of']         = defaultdict(list)
    word_a_dict['own-artist-music'] = defaultdict(list)
    word_a_dict['like-artist']      = defaultdict(list)
    word_u_dict = {}
    word_u_dict['heard-of']         = defaultdict(list)
    word_u_dict['own-artist-music'] = defaultdict(list)
    word_u_dict['like-artist']      = defaultdict(list)
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
        if word['heard-of'] >= 0:
            word_a_dict['heard-of'][artist_id].append(word['heard-of'])
            word_u_dict['heard-of'][user_id].append(word['heard-of'])
        if word['own-artist-music'] >= 0:
            word_a_dict['own-artist-music'][artist_id].append(word['own-artist-music'])
            word_u_dict['own-artist-music'][user_id].append(word['own-artist-music'])
        if word['like-artist'] >= 0:
            word_a_dict['like-artist'][artist_id].append(word['like-artist'])
            word_u_dict['like-artist'][user_id].append(word['like-artist'])
    mean = lambda l: float(sum(l))/len(l);
    for artist_id in word_a_dict['heard-of']:
        word_dict[(artist_id, -1)]['heard-of'] = mean(word_a_dict['heard-of'][artist_id])
    for artist_id in word_a_dict['own-artist-music']:
        word_dict[(artist_id, -1)]['own-artist-music'] = mean(word_a_dict['own-artist-music'][artist_id])
    for artist_id in word_a_dict['like-artist']:
        word_dict[(artist_id, -1)]['like-artist'] = mean(word_a_dict['like-artist'][artist_id])
    for user_id in word_u_dict['heard-of']:
        word_dict[(-1, user_id)]['heard-of'] = mean(word_u_dict['heard-of'][user_id])
    for user_id in word_u_dict['own-artist-music']:
        word_dict[(-1, user_id)]['own-artist-music'] = mean(word_u_dict['own-artist-music'][user_id])
    for user_id in word_u_dict['like-artist']:
        word_dict[(-1, user_id)]['like-artist'] = mean(word_u_dict['like-artist'][user_id])
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
