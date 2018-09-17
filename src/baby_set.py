# baby_set.py
# Nicholas Newman

class BabySet:
	"""A class the mimics the behavior of python's built in 
	Set class. Implemented as a list."""

	def __init__(self, d=[]):
		self.__data = []
		self.addSeq(d)

	def __repr__(self):
		"""Returns a string representation of the set."""

		s = ', '.join([str(i) for i in self.__data])
		return s

	def __str__(self):
		"""Returns a string representation of the set."""

		s = ', '.join([str(i) for i in self.__data])
		return s

	def add(self, elem):
		"""Add element elem to the set only if it is 
		unique to the set."""

		for i in self.__data:
			if i == elem:
				return None

		self.__data.append(elem)

	def addSeq(self, seq):
		"""Add contents of seq to the set where each item in contents 
		is unique to the set."""
		for i in seq:
			self.add(i)

	def remove(self, elem):
		"""Removes and returns the element elem from the set. 
		Raises KeyError if elem is not contained in the set.
		"""
		try:
			self.__data.remove(elem)
		
		except Exception as e:
			raise KeyError

	def get(self, elem):
		"""Returns element elem from the set. 
		Raises KeyError if elem is not contained in the set.
		"""
		try:
			return self.__data[self.__data.index(elem)]
		except ValueError:
			raise KeyError
	
	def clear(self):
		"""Remove all elements from the set."""
		self.__data = []

	def size(self):
		"""Returns the size of the set."""
		return len(self.__data)

# End of class BabySet
