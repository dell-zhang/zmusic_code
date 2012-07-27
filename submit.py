#! /usr/bin/env python
"""
@author: dell
"""

if __name__ == "__main__":
    import music
    import model
    train_examples = music.load_examples('data/train.pkl')
    model.learn(train_examples)
    test_examples = music.load_examples('data/test.pkl')
    test_ratings = model.predict(test_examples)
    for i in range(len(test_examples)):
        test_examples[i]['rating'] = test_ratings[i]
    music.write_examples('submissions/zmusic_predictions.csv', test_examples)
