#!/usr/bin/env python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
import numpy

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here


from sklearn.cross_validation import train_test_split
import sklearn.metrics
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)

from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)
print clf.score(features_test, labels_test)

pred = clf.predict(features_test)
poi_predicted = numpy.count_nonzero(pred)
people_in_test_set = len(labels_test)
non_pop_predicted = people_in_test_set - poi_predicted

print "poi predicted:", poi_predicted
print "non-poi predicted", non_pop_predicted
print "people in dataset:", people_in_test_set
print "accuracy", non_pop_predicted / float(people_in_test_set)

true_positives = 0
for prediction, actual in zip(pred, labels_test):
  if prediction == 1 and actual == 1:
    true_positives += 1

print "true positives:", true_positives
print "precision score", sklearn.metrics.precision_score(labels_test, pred)
print "recall score", sklearn.metrics.recall_score(labels_test, pred)

predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]


true_positives = 0
true_negatives = 0
false_postives = 0
false_negatives = 0
for prediction, actual in zip(predictions, true_labels):
  if prediction == 1 and actual == 1:
    true_positives += 1
  elif prediction == 0 and actual == 0:
    true_negatives += 1
  elif prediction == 1 and actual == 0:
    false_postives += 1
  else:
    false_negatives += 1

print "true positives:", true_positives
print "true negatives:", true_negatives
print "false positives:", false_postives
print "false negatives:", false_negatives

print "precision", true_positives / float(true_positives + false_postives)
print "recall", true_positives / float(true_positives + false_negatives)
