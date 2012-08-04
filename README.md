zmusic_code
================================

Code for the EMI Music Data Science Hackathon 

http://www.kaggle.com/c/MusicHackathon

--------------------------------
DOCUMENTS

* How I Did It

  http://www.dcs.bbk.ac.uk/~dell/publications/musichackthon/zmusic_doc.pdf

* Interview

  http://www.dcs.bbk.ac.uk/~dell/publications/musichackthon/zmusic_int.txt

--------------------------------
REQUIREMENTS

* Python 2.7.3 x64

  http://www.python.org/getit/releases/2.7/

* Numpy-MKL

  http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy

* scikit-learn

  http://www.lfd.uci.edu/~gohlke/pythonlibs/#scikit-learn

* libFM

  http://www.libfm.org/

--------------------------------
DATA

* EMI One Million Interview Dataset

  http://musicdatascience.com/emi-million-interview-dataset/  

* ./data/*.csv

  The data files users.csv and words.csv
  have been cleaned and encoded manually
  using Unix tools (cat, cut, split, grep, sort, wc, etc.)
  and a text editor (search, replace, etc.).

* ./data/*.txt

  The other files users_*.txt and words_*.txt 
  show how the text-format categorical attributes are encoded.

--------------------------------
PROGRAMS

* ./users.py

  Pre-process the users data

* ./words.py

  Pre-process the words data

* ./music.py

  Pre-process the music training/test data

* ./model.py [n]

  Run cross-validation experiments on the training data 
  using the random forest with n trees (n=60 by default)

* ./submit.py

  Make final predictions on the test data
  using the random forest with 60 trees

* ./prepare_libfm.py

  Convert the data into libFM format: train.libfm and test.libfm

--------------------------------

PERFORMANCE

Random Forest
(n_estimators=60, max_features='sqrt')

* RMSE = 14.59553 (2-fold cross-validation)
* RMSE = 13.76513 (public)
* RMSE = 13.80559 (private)

Factorization Machine
(-method mcmc -dim '1,1,100' -init_stdev 0.25 -iter 1000)

* RMSE = 14.19240 (2-fold cross-validation)

--------------------------------

AUTHOR

Dell Zhang (dell.z@ieee.org)
