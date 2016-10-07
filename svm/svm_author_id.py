#!/usr/bin/env python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

from sklearn import svm
from collections import Counter

classifier = svm.SVC(kernel='rbf', C=10000)

training_time = time()
classifier.fit(features_train, labels_train)
print "training time:", round(time() - training_time, 3), "s"

predict_time = time()
predictions = classifier.predict(features_test)
print "predict time:", round(time() - predict_time, 3), "s"

print "accuracy:", classifier.score(features_test, labels_test)

print "chris emails:", Counter(predictions)[1]

#########################################################


