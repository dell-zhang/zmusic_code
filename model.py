#! /usr/bin/env python
"""
@author: dell
"""

import users
users.load_users('data/users.pkl')

import words
words.load_words('data/words.pkl')

#import means
#means.load_means('data/means.pkl')

from collections import defaultdict

def indicator(cat_id, dim):
    v = [0] * dim
    if cat_id >= 0:
        v[cat_id] = 1
    return v

def binary(w):
    if w == -1:
        return 0
    if w == 0:
        return -1
    if w == 1:
        return 1
    return 1/0  # error

def represent(example):
    vector = []
    artist_id = example['artist']
    track_id  = example['track']
    user_id   = example['user']
    time_id   = example['time']
    vector.extend(indicator(artist_id, 50))
    vector.extend(indicator(time_id, 24))
    user = users.user_dict.get(user_id, defaultdict(lambda: -1))
    vector.append(binary(user['gender']))
    vector.append(user['age'])
    vector.extend(indicator(user['working'], 13))
    vector.extend(indicator(user['region'], 4))
    vector.extend(indicator(user['music'], 5))
    vector.extend([user['list_own'], user['list_back']])
    vector.extend([user['q%d' % (j+1)] for j in range(19)])
#    if (artist_id, user_id) in words.word_dict:
#        word = words.word_dict[(artist_id, user_id)]
#    elif (artist_id, -1) in words.word_dict:
#        word = words.word_dict[(artist_id, -1)]
#    elif (-1, user_id) in words.word_dict:
#        word = words.word_dict[(-1, user_id)]
#    else:
#        word = defaultdict(lambda: -1)
    word = words.word_dict.get((artist_id, user_id), defaultdict(lambda: -1))
    vector.extend(indicator(word['heard-of'], 4))
    vector.extend(indicator(word['own-artist-music'], 5))
    vector.append(word['like-artist'])
    vector.extend([binary(word['w%d' % (j+1)]) for j in range(81)])
#    for j in range(81):
#        vector.extend(indicator(word['w%d' % (j+1)], 2))
#    artist_word = words.word_dict.get((artist_id, -1), defaultdict(lambda: -1))
#    vector.append(artist_word.get('heard-of', -1))
#    vector.append(artist_word.get('own-artist-music', -1))
#    vector.append(artist_word.get('like-artist', -1))
#    user_word = words.word_dict.get((-1, user_id), defaultdict(lambda: -1))
#    vector.append(user_word.get('heard-of', -1))
#    vector.append(user_word.get('own-artist-music', -1))
#    vector.append(user_word.get('like-artist', -1))
    vector.extend(indicator(track_id, 184))
    vector.append(user_id)
#    vector.append(means.user_mean[user_id,track_id])
#    vector.append(means.track_mean[user_id,track_id])
    return vector

def label(example):
    return example['rating']

from sklearn.ensemble import RandomForestRegressor
clf = RandomForestRegressor(n_estimators=60, max_features='sqrt')
#from sklearn.ensemble import ExtraTreesRegressor
#clf = ExtraTreesRegressor(n_estimators=40, max_features='sqrt')
#from sklearn.ensemble import GradientBoostingRegressor
#clf = GradientBoostingRegressor(n_estimators = 200)

def learn(examples):
    global clf
    X = [represent(example) for example in examples]
    y = [label(example) for example in examples]
    clf.fit(X, y)

#def normalize_ratings(ratings):
#    return ratings
#    #return [(2*int(rating/20)+1)*10 for rating in ratings]

def predict(examples):
    global clf
    X = [represent(example) for example in examples]
    y = clf.predict(X)
    return y

import math
from sklearn.metrics import mean_squared_error

def rmse(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    return math.sqrt(mse)

from sklearn.cross_validation import cross_val_score

def validate(examples):
    global clf
    X = [represent(example) for example in examples]
    y = [label(example) for example in examples]
    scores = cross_val_score(clf, X, y, cv=3, score_func=rmse)
    return scores

if __name__ == "__main__":
    import music
    train_examples = music.load_examples('data/train.pkl')
    scores = validate(train_examples)
    print "RMSE: %0.6f (+/- %0.6f)" % (scores.mean(), scores.std()/2)
