import numpy as np

class Client:
	""" Basic type of a client """

	def __init__(self):
		self.register_time = np.random.randint(45, 90)
		self.selection_time = np.random.randint(30, 300)
		self.signoff_time = np.random.randint(10, 60)

	def print_info(self):
		print("""Jestem klientem, wymagam %d sekund na rejestrację, 
				%d sekund na dobranie gry 
				%d sekund na wypisanie."""
				% (self.register_time, self.selection_time, 
				   self.signoff_time))

	def get_reg_time(self):
		return self.register_time
