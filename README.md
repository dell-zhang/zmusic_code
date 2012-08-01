zmusic_code
================================

Code for the EMI Music Data Science Hackathon

* http://musicdatascience.com/music-data-science-hackathon/
* http://www.kaggle.com/c/MusicHackathon

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

* ./data/*.csv

The data files users.csv and words.csv
have been cleaned and encoded manually
using unix tools (cat, cut, split, grep, sort, wc,...)
and a text editor (search, replace,...).

* ./data/*.txt

The other files users_*.txt and words_*.txt 
show how the text-format categorical attributes are encoded.

--------------------------------
PROGRAMS

* ./users.py

Preprocess the users data

* ./words.py

Preprocess the words data

* ./music.py

Proprocess the music training/test data

* ./model.py n

Run cross-validation experiments on the training data 
using the random forest with n trees

* ./submit.py

Make final predictions on the test data
using the random forest with 60  trees

--------------------------------

PERFORMANCE

RMSE=
* 14.32221 (3-fold cv)
* 13.76513 (public)
* 13.80559 (private)

--------------------------------

Dell Zhang (dell.z@ieee.org)
