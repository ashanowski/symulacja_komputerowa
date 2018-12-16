""" Clients module

This module defines class Client that simulates
a real-life client that enqueues to the queue
and wants to be served.

"""
import numpy as np

class Client:
	""" Basic type of a client

	...

	Attributes
	----------
		client_type : int [1, 2, 3]
			1 - first-commer
			2 - will change a game
			3 - is going to leave
		register_time : int
			Time needed by client to be registered
		selection_time : int
			Time needed by client to select a game
		signoff_time : int
			Time needed by client to be signed off

	Methods
	-------
	print_info()
		Prints info about time needed by client

	"""

	def __init__(self, type_=1):
		self.client_type = type_
		self.register_time = np.random.randint(45, 90)
		self.selection_time = np.random.randint(30, 300)
		self.signoff_time = np.random.randint(10, 60)

	def print_info(self):
		""" Prints info about time needed by client

		"""
		print("""Jestem klientem, wymagam %d sekund na rejestrację, 
				%d sekund na dobranie gry 
				%d sekund na wypisanie."""
				% (self.register_time, self.selection_time, 
				   self.signoff_time))

	def set_type(self, type_):
		self.client_type = type_