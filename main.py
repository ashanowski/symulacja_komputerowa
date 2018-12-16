from queues import Queue
from clients import Client
import numpy as np
import progressbar as pb

def create_queues(queue_type, quantity):
	""" Create a list of list of Queues with given quantity

		Parameters
		----------
			queue_type : int [1, 2, 3]
				type of the queue

			quantity : int
				number of queues to return

		Returns
		-------
			list
				a list of Queues
	"""
	return [Queue(queue_type) for _ in range(quantity)]

def add_people(queue, quantity):
	""" Enqueue given quantity of clients to a queue

		Parameters
		----------
			queue : Queue
				choice of queue to add clients
			quantity : int
				number of clients to be enqueued

		Returns
		-------
			list 
				a list of consequetive enqueues to given queue
	"""
	return [queue.enqueue(Client()) for _ in range(quantity)]

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
		return("%d:%d:%d" % (0, 0, time))

	elif time >= 60 and time < 3600:
		minutes = int(time/60)
		seconds = time - 60*minutes
		return("%d:%d:%d" 
			% (0, minutes, seconds))

	elif time >= 3600:
		hours = int(time/3600)
		minutes = int( (time - hours*3600) / 60)
		seconds = int (time - hours*3600 - minutes*60)
		return("%d:%d:%d"
			% (hours, minutes, seconds))

def procedure_test(people_num, end_time, test='register_time'):
	""" Perform a test for register, selection
		or signoff procedure.
		If register time test is selected,
		combine it with selection time test, as
		client will always take a game after registering.
		
		Parameters
		----------
			people_num : int
				how many clients in a queue
			end_time : int 
				maximum time for registration in seconds from 0
			test : str
				'register_time' for registration test
				'selection_time' for selection test
				'signoff_time' for signoff_time

		Returns
		-------
			Array [time_sum, queue_pos, completed]
				time_sum : int
					how many seconds were used for registration
				queue_pos : int
					how many people were served
				completed : bool
					True if queue was emptied, false if time has
					passed with clients still in queue
	"""
	if test not in ['register_time', 'selection_time', 'signoff_time']:
		print("Type of test (%s) not appropriate!" % (test))
		return

	q1 = Queue(1)
	add_people(q1, people_num)
	time_sum = 0
	queue_pos = 0
	
	while time_sum < end_time:
		# break if queue is empty
		if q1.isempty():
			# debugging
			#print("The queue is empty!")
			completed = True
			break

		# get the value of time needed for one client

		test_time = getattr(q1.get_obj(q1.get_len()-1), test)

		# if register_time is chosen, add selection time
		if test == 'register_time':
			test_time += getattr(q1.get_obj(q1.get_len()-1), 'selection_time')

		# break if time passed
		if time_sum + test_time >= end_time:
			# debugging
			#print("We have no time left!")
			completed = False
			break

		# add the reg_time, dequeue a client and change pos
		time_sum += test_time
		q1.dequeue()
		queue_pos += 1

	# debugging
	#print("We've managed to handle %d clients within %s!"\
	#			% (queue_pos+1, manage_time(time_sum)))

	return [time_sum, queue_pos, completed]

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

def main():
	print(procedure_test(50, 3600, 'selection_time'))

if __name__ == '__main__':
	main()

	# TODO:
	# ---> jak obsłużyć inne typy kolejek
	# ---> rozpoznawanie klientów, przydzielanie typów
	#	   (wchodzący, zmieniający grę, wychodzący)
	#	   po zarejestrowaniu zmienia flagę na inną,
	#	   ale musi zostać w pamięci
	#	   KLIENCI GRAJĄCY MOGĄ BYĆ PRZENOSZENI DO NP.ARRAY