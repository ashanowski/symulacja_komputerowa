""" Queues module

This module defines class Queue and some other classes based
on that one to provide simulation of real-life working
queue. 
"""
import numpy as np

class Queue:
	""" Basic type of queue 
		
		...

		Attributes
		----------

		_queue : numpy.array
			an array that stores objects in queue based
			data structure (First In, First Out)
		queue_type : int [1, 2, 3, 4]
			1 - for registering clients
			2 - for clients that want to change the game
			3 - for clients that want to quit
			4 - for all type of clients

		Methods
		-------
		enqueue(obj)
			Adds a new object to the end of queue
		dequeue()
			Deletes the first object in the queue
		get_len()
			Returns length of queue
		show()
			Prints out the content of queue
		get_obj(pos=0)
			Returns object from queue with given position
		isempty()
			Checks if queue is empty
	"""

	def __init__(self, queue_type=1):
		self.queue_type = queue_type
		self._queue = np.array([], dtype=object)

	def enqueue(self, obj):
		""" Adds a new client object to the end of queue 
			if the client type attribute of given object
			matches the type of queue

			Parameters
			----------
				obj : object
					object to be added
		"""
		if getattr(obj, 'client_type') == self.queue_type \
					or self.queue_type == 4:
			self._queue = np.insert(self._queue, 0, obj)
		else:
			print("Client type does not match queue type!")

	def dequeue(self):
		""" Deletes the first object in the queue 
			
			Returns
			-------
				obj : object
					The first object in the queue that has
					been deleted
		"""
		obj = self._queue[-1]
		self._queue = np.delete(self._queue, -1)
		return obj

	def get_len(self):
		""" Returns length of queue 
			
			Returns
			-------
				length : int
					Length of queue, as numpy.shape 0th index
		"""
		return np.shape(self._queue)[0]

	def show(self):
		""" Prints out the content of queue 

		"""
		print(self._queue)

	def get_obj(self, pos=0):
		""" Returns object from queue with given position 
			
			Parameters
			----------
				pos : int
					Position of object in the queue

			Returns
			-------
				object
					Object of given position
		"""
		try:
			return self._queue[pos]
		except IndexError:
			print("There's no such object position")

	def isempty(self):
		""" Checks if queue is empty

		"""
		if np.shape(self._queue)[0] == 0: return True
