from queues import Queue
from clients import Client
import numpy as np
from utilities import *

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

def simulate_test():
	""" Simulate behavior of one client

		Returns
		-------
			current_time : int
				How many se

	"""
	#Creating queues, a client, and enqueueing the client
	print('Utworzono kolejki!')
	q1 = Queue(queue_type=1)
	q2 = Queue(queue_type=2)
	q3 = Queue(queue_type=3)
	print('Utworzono klienta!')
	c1 = Client(1)
	print('Dołączam do kolejki')
	q1.enqueue(c1)	
	# max time equals 9 hours
	max_time = 9 * 3600

	# time spent on registering
	current_time = c1.register_time

	while current_time < max_time:
		if current_time + c1.selection_time + 1800 >= max_time:
			print("Nie zdążę już wybrać innej gry, wychodzę!")
			c1.set_type(3)
			# find best queue
			q3.enqueue(3)
			# wait for your turn
			current_time += c1.signoff_time
			q3.dequeue()
			break
		selection_time = c1.selection_time
		print('Wybrałem grę w {}!'.format(manage_time(selection_time)))
		game_time = int(np.random.normal(1800, 900))
		print("Grałem w grę przez {}!".format(manage_time(game_time)))
		current_time += selection_time + game_time
	print("Kończę zabawę w czasie {}".format(manage_time(current_time)))
	return current_time

def main():
	simulate_test()


if __name__ == '__main__':
	main()

	# TODO:
	# ---> jak obsłużyć inne typy kolejek
	# ---> po zarejestrowaniu zmienia flagę na inną,
	#	   ale musi zostać w pamięci
	#	   KLIENCI GRAJĄCY MOGĄ BYĆ PRZENOSZENI DO NP.ARRAY
	# ---> potrzebna funkcja do wyszukiwania najlepszej
	#	   możliwej kolejki, czyli takiej w której jest
	#	   najmniej osób