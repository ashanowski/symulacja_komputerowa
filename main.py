from queues import Queue
from clients import Client
import numpy as np
import progressbar as pb

def create_queues(quantity):
	""" Create a list of list of Queues with given quantity

		Parameters
		----------
			quantity : int
				number of queues to return

		Returns
		-------
			list
				a list of Queues
	"""
	return [Queue() for _ in range(quantity)]

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

def registration_test(people_num, max_time):
	""" Perform a test for registration procedure
		
		Parameters
		----------
			people_num : int
				how many clients in a queue
			max_time : int 
				maximum time for registration in seconds

		Returns
		-------
			Array [time_sum, queue_pos]:
				time_sum : int
					how many seconds were used for registration
				queue_pos : int
					how many people were served
	"""
	start_time, end_time = 0, max_time

	q1 = Queue()
	add_people(q1, people_num)
	time_sum = 0
	queue_pos = 0
	
	while time_sum < end_time:
		# break if queue is empty
		if q1.isempty():
			print("The queue is empty!")
			break
		# take time var for one client
		reg_time = q1.get_obj(q1.get_len()-1).register_time
		# break if time passed
		if time_sum + reg_time >= end_time:
			print("We have no time left!")
			break
		# add the reg_time, dequeue a client and change pos
		time_sum += reg_time
		q1.dequeue()
		queue_pos += 1

	print("We've managed to handle %d clients within %s!"\
				% (queue_pos+1, manage_time(time_sum)))

	return [time_sum, queue_pos]

def main():
	registration_test(100, 3600)
	registration_test(50, 3600)

if __name__ == '__main__':
	main()
	

	# TODO:
	# ---> registration_test:
	# 	-> flagi - czy obsłużono wszystkich czy nie
	#	-> export danych do pliku (najlepiej .csv)
	# ---> jak obsłużyć inne typy kolejek
	# ---> rozpoznawanie klientów, przydzielanie typów
	#	   (wchodzący, zmieniający grę, wychodzący)
	#	   po zarejestrowaniu zmienia flagę na inną,
	#	   ale musi zostać w pamięci
