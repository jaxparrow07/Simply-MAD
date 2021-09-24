import mad
import sys
import conf_

def main():

	data_set = sys.argv
	del data_set[0]

	if len(data_set) == 1:
		t_data = []
		for element in  data_set[0].replace(' ','').split(','):
			t_data.append(element)
		data_set = t_data

	# After getting the dataset as list.. Do the actual math in the mad module

	formatted_set:str = str(data_set).replace('[','{').replace(']','}').replace("\"","").replace("'",'') # I am lazy to do a hard way.. So, easy way go brr

	value = mad.find_mad(data_set)

	if conf_.formatted_steps:
		print("Steps")

	elif conf_.only_mad:
		print(value['mad'])

	else:
		print("""Data set = %s
Mean : %s
Population : %s

The Mean Average Deviation is %s""" % (formatted_set,str(value['mean']),str(value['population']),str(value['mad'])))


	


if __name__ == '__main__':
	main()