#! /usr/bin/env python
"""
@author: dell
"""

import csv
import cPickle as pickle

def read_examples(csv_filename):
    csv_file = open(csv_filename, 'rb')
    reader = csv.reader(csv_file)
    reader.next()  # ignore header
    examples = []
    for row in reader:
        example = {}
        example['artist']   = int(row[0])
        example['track']    = int(row[1])
        example['user']     = int(row[2])
        if len(row) == 5:  # train
            example['rating'] = int(row[3])
        else:  # test
            example['rating'] = -1
        example['time']     = int(row[-1])
        examples.append(example)
    csv_file.close()
    return examples

def write_examples(csv_filename, examples):
    csv_file = open(csv_filename, 'wb')
    writer = csv.writer(csv_file)
    writer.writerow(['Artist','Track','User','Rating','Time'])  # header
    for example in examples:
        row = [str(example['artist']),
               str(example['track']),
               str(example['user']),
               str(example['rating']),
               str(example['time'])]
        writer.writerow(row)
    csv_file.close()

def load_examples(pkl_filename):
    pkl_file = open(pkl_filename, 'rb')
    examples = pickle.load(pkl_file)
    pkl_file.close()
    return examples

def save_examples(pkl_filename, examples):
    pkl_file = open(pkl_filename, 'wb')
    pickle.dump(examples, pkl_file, -1)
    pkl_file.close()

if __name__ == "__main__":
    train_examples = read_examples('data/train.csv')
    save_examples('data/train.pkl', train_examples)
    test_examples = read_examples('data/test.csv')
    save_examples('data/test.pkl', test_examples)
