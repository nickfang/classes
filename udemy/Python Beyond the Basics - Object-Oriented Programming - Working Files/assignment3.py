#!usr/bin/python
import os

class DoThis(dict):

	def __setitem__(self,key,val):

		# OOPS! does endless recursion
		# self[key] = val
		# do this instead
		dict.__setitem__(self, key, val)

class ConfigDict(dict):

	def __init__(self, filename):
		self._filename = filename
		if os.path.isfile(self._filename):
			with open(self._filename, 'r') as f:
				for line in f:
					# need to remove the "\n"'s that are read in from the file
					key, value = line.rstrip("\n").split("=", 1)
					dict.__setitem__(self, key, value)

	def __setitem__(self, key, val):
		dict.__setitem__(self, key, val)
		with open(self._filename, 'w') as f:
			for key, val in self.items():
				f.write("{0}={1}\n".format(key, val))