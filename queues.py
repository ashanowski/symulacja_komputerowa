import numpy as np

class Queue:
	""" Main type of queue """

	def __init__(self):
		self._queue = np.array([], dtype=object)

	def enqueue(self, obj):
		"""Adds a new object to the end of queue """
		self._queue = np.insert(self._queue, 0, obj)

	def dequeue(self):
		""" Deletes the first object in the queue """
		self._queue = np.delete(self._queue, -1)

	def get_len(self):
		"""Returns length of queue """
		return np.shape(self._queue)[0]

	def show(self):
		""" Print out the content of queue """
		print(self._queue)

	def get_obj(self, pos=0):
		""" Return object from queue with given position """
		try:
			return self._queue[pos]
		except IndexError:
			print("There's no such object position")