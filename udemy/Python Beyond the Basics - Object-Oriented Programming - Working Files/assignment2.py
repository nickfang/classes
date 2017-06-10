import abc
import datetime


class WriteFile(object):
	def __init__(self, filename):
		self.filename = filename

	def write_line(self, text):
		file = open(self.filename, 'a')
		file.write(text + '\n')
		file.close()

	@abc.abstractmethod
	def write(self):
		return

class DelimFile(WriteFile):
	def __init__(self, filename, delim):
		super(DelimFile, self).__init__(filename)
		self.delim = delim

	def write(self, input):
		temp = []
		for item in input:
			if item.find(self.delim) > -1:
				temp.append("\"" + item + "\"")
			else:
				temp.append(item)

		line = self.delim.join(temp)
		self.write_line(line)

class LogFile(WriteFile):
	def __init__(self, filename):
		super(LogFile, self).__init__(filename)

	def write(self, input):
		dtStr = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
		self.write_line('{0}   {1}'.format(dtStr, input))

