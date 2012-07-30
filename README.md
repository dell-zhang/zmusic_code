zmusic_code
================================

Code for the EMI Music Data Science Hackathon

http://musicdatascience.com/music-data-science-hackathon/
http://www.kaggle.com/c/MusicHackathon

--------------------------------
REQUIREMENTS

* Python 2.7.3 x64
  http://www.python.org/getit/releases/2.7/
* Numpy-MKL
  http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy
* scikit-learn
  http://www.lfd.uci.edu/~gohlke/pythonlibs/#scikit-learn

--------------------------------
DATA

The data files users.csv and words.csv
have been cleaned and encoded manually
using unix tools (cat, cut, split, grep, sort, wc,...)
and a text editor (search, replace,...).

* ./data/*.csv

The other files users_*.txt and words_*.txt 
show how the text-format categorical attributes are encoded.

* ./data/*.txt

--------------------------------
PROGRAMS

Preprocess the users data
./users.py

Preprocess the words data
./words.py

Proprocess the music training/test data
./music.py

Run cross-validation experiments on the training data 
using the random forest with n trees
./model.py n

Make final predictions on the test data
using the random forest with 60  trees
./submit.py

--------------------------------

PERFORMANCE

RMSE=
* 13.76513 (public)
* 13.80559 (private)

--------------------------------

Dell Zhang (dell.z@ieee.org)
