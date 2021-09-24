"""Finding average mean deviation of a data set with basic python function"""

import conf_

def find_mad(data_set):

	population = len(data_set)

	total = 0

	for element in data_set:
		total += int(element)

	mean = round((total / population),conf_.decimal_points)


	total_ = 0

	for element in data_set:
		total_ += abs(int(element) - mean)

	mad = total_ / population


	return {"mean":mean,
			"population":population,
			"mad":round(mad,conf_.decimal_points) }

