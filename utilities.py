"""
Module containing utility functions

manage_time - HH:MM:SS formatted string from
			  given seconds int
save_to_csv - saves given data in a csv file

"""
def manage_time(time):
	""" Shorten time frame to minutes or hours

		Parameters
		----------
			time : int
				time in seconds

		Returns
		-------
			string
				time in HH:MM:SS format
	"""

	if time < 60:
		return("{:02}:{:02}:{:02}".format(0, 0, time))

	elif time >= 60 and time < 3600:
		minutes = int(time/60)
		seconds = time - 60*minutes
		return("{:02}:{:02}:{:02}".format(0, minutes, seconds))

	elif time >= 3600:
		hours = int(time/3600)
		minutes = int( (time - hours*3600) / 60)
		seconds = int (time - hours*3600 - minutes*60)
		return("{:02}:{:02}:{:02}".format(hours, minutes, seconds))
			

def save_to_csv(data, filename):
	""" Save given data to a csv file

		Parameters
		----------
			data : list
				data to be saved and splitted by commas
			filename : str
				filename of the file to save the data to

		Returns
		-------
			file : file
				saves data to the output csv file
		"""
	# if given filename doesn't end with .csv:
	if filename[-4:] is not '.csv':
		filename = "%s.csv" % (filename)

	with open(filename, 'w') as file:
		for line in data:
			file.write("%d,%d,%s\n" % (line[0], line[1], line[2]))