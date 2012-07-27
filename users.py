#! /usr/bin/env python
"""
@author: dell
"""

import csv
import cPickle as pickle

# global variables
user_dict = {}

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

def read_users(csv_filename):
    csv_file = open(csv_filename, 'rb')
    reader = csv.reader(csv_file)
    reader.next()  # ignore header
    for row in reader:
        respid      = int(row[0])
        user = {}
        user['gender']  = get_int_attr(row[1])
        user['age']     = get_int_attr(row[2])
        user['working'] = get_int_attr(row[3])
        user['region']  = get_int_attr(row[4])
        user['music']   = get_int_attr(row[5])
        user['list_own']    = get_flt_attr(row[6])
        user['list_back']   = get_flt_attr(row[7])
        for j in range(19):
            user['q%d' % (j+1)] = get_flt_attr(row[8+j])
        user_dict[respid] = user
    csv_file.close()

def load_users(pkl_filename):
    global user_dict
    pkl_file = open(pkl_filename, 'rb')
    user_dict = pickle.load(pkl_file)
    pkl_file.close()

def save_users(pkl_filename):
    pkl_file = open(pkl_filename, 'wb')
    pickle.dump(user_dict, pkl_file, -1)
    pkl_file.close()

if __name__ == "__main__":
    read_users('data/users.csv')
    save_users('data/users.pkl')
