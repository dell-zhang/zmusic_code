#! /usr/bin/env python
"""
@author: dell
"""

import model

def sp_vector(v):
    return ' '.join(["%d:%.2f" % (j, v[j]) for j in range(len(v)) if v[j] != 0])

def to_libfm(examples, libfm_filename):
    libfm_file = open(libfm_filename, 'w')
    for example in examples:
        x_i = model.represent(example)[:-1]
        y_i = model.label(example)
        user_id = example['user']
        user_id_feature = "%d:1" % (len(x_i)+user_id)
        libfm_file.write("%d %s %s\n" % (y_i, sp_vector(x_i), user_id_feature))
    libfm_file.close()
    
if __name__ == "__main__":
    import music
    train_examples = music.load_examples('data/train.pkl')
    to_libfm(train_examples, 'libfm/train.libfm')
    test_examples = music.load_examples('data/test.pkl')
    to_libfm(test_examples, 'libfm/test.libfm')
