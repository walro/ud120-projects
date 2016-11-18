#!/usr/bin/env python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### your code goes here
    residuals = [p - n for p, n in zip(predictions, net_worths)]
    result = zip(ages, net_worths, residuals)
    result.sort(key=lambda tuple: tuple[2])

    length = int(len(result) * 0.9)
    cleaned_data = result[:length]

    return cleaned_data

