#!/usr/bin/env python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
number_of_employees = len(enron_data)
an_employee = enron_data.keys()[0]
features = enron_data[an_employee].keys()
number_of_features = len(features)

print features

number_of_poi = 0
for person in enron_data:
  if enron_data[person]["poi"] == 1:
    number_of_poi += 1

james_prentice_stock = enron_data["PRENTICE JAMES"]["total_stock_value"]
wesley_colwell_to_poi = enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

jeffrey_k_skilling = enron_data["SKILLING JEFFREY K"]
jeffrey_k_skilling_stock_options = jeffrey_k_skilling["exercised_stock_options"]

kenneth_l_lay = enron_data["LAY KENNETH L"]
andrew_s_fastow = enron_data["FASTOW ANDREW S"]
persons = (jeffrey_k_skilling, kenneth_l_lay, andrew_s_fastow)
max_person = sorted(persons, reverse=True, key=lambda person: person["total_payments"])[0]


print "quantified salary:", len(dict((key, person) for key, person in enron_data.items() if person["salary"] != "NaN"))
print "email_address:", len(dict((key, person) for key, person in enron_data.items() if person["email_address"] != "NaN"))
total_payments_as_nan = len(dict((key, person) for key, person in enron_data.items() if person["total_payments"] == "NaN"))

print "% of total payments as NaN", total_payments_as_nan / float(number_of_employees)
print "total payments as NaN", total_payments_as_nan

poi_total_payments_as_nan = len(dict((key, person) for key, person in enron_data.items() if person["total_payments"] == "NaN" and person["poi"] == 1))
print "% of total poi payments as NaN", poi_total_payments_as_nan / float(number_of_poi)

print "maximum payments:{0} person:{1}".format(max_person["total_payments"], max_person["email_address"])

print "number of employees:", number_of_employees
print "number of features:", number_of_features
print "number of people of interest", number_of_poi
print "James Prentice stockvalue", james_prentice_stock
print "Wesley Colwell emails to poi", wesley_colwell_to_poi
print "Jaffrey K Skilling exercised stock options", jeffrey_k_skilling_stock_options
