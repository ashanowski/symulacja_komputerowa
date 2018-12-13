from queues import Queue
from clients import Client
import numpy as np
import progressbar as pb

def create_queues(quantity):
	return [Queue() for _ in range(quantity)]

def add_people(queue, quantity):
	return [queue.enqueue(Client) for _ in range(quantity)]


if __name__ == '__main__':
	# time in seconds
	start_time, end_time = 0, 1000

	time_sum = 0
	q1 = Queue()
	add_people(q1, 1000)
	
	hehe

	
