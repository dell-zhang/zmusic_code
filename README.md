zmusic_code
================================

Code for the EMI Music Data Science Hackathon

--------------------------------
Requirements
* Python 2.7.3 x64
  http://www.python.org/getit/releases/2.7/
* Numpy-MKL
  http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy
* scikit-learn
  http://www.lfd.uci.edu/~gohlke/pythonlibs/#scikit-learn

--------------------------------
Data
./data/*.csv

# The data files users.csv and words.csv
# have been cleaned and encoded manually
# using unix tools (cat, cut, split, grep, sort, wc,...)
# and a text editor (search, replace,...).

# The other files users_*.txt and words_*.txt 
# show how the text-format categorical attributes are encoded.

--------------------------------
Programs

# preprocess the users data
./users.py

# preprocess the words data
./words.py

# proprocess the music training/test data
./music.py

# conduct cross-validation experiments on the training data 
# using the random forest with <n> trees
./model.py <n>

# make final predictions on the test data
# using the random forest with 60  trees
./submit.py

--------------------------------

Performance

RMSE=
13.76513 (public), 
13.80559 (private). 

--------------------------------

Dell Zhang (dell.z@ieee.org)
