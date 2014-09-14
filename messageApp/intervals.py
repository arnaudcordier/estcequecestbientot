"""
 There should be a insightful documentation here
"""

"""

interval : 'year month dayOfMonth dayOfWeek hour minute seconde',
messages : [('hh:mm', 'message'), ('hh:mm', 'message'), ('hh:mm', 'message')]

"""
from messageApp.intervalBit import IntervalBit
from messageApp.messageList import MessageList

class Interval():
	def __init__(self, interval, messages,  timeIsRelative = False):
		self._intervals      = self._createInterval(interval)
		self._messages       = MessageList(messages)
		self.timeIsRelative = timeIsRelative

	def getMessage(self, time):
		times  = self._formatTime(time)
		itFits = self._doesItFit(times)
		if itFits:
			now = times[5] + times[4] * 60
			if self.timeIsRelative:
				now = now + self._getTimeOffset(itFits)
			return self._messages.getMessage(now)
 
	def _createInterval(self, interval):
		intervals = []
		for (position, bit) in enumerate(interval.split()):
			intervals.append(IntervalBit(bit, position+1))
		return intervals

	def _formatTime(self, time):
		formated = time.strftime('%Y %m %d %w %H %M')
		bits = formated.split()
		bitsInt = [int(x) for x in bits]
		bitsInt[3] = ((bitsInt[3] + 6) % 7) + 1 # weekdays from 1 to 7 not 0 to 6
		return bitsInt

	def _doesItFit(self, times):
		fitingInterval = []
		if len(times) == len(self._intervals):
			for i in range(len(times)):
				itFits = self._intervals[i].doesItFit(times[i])
				if itFits:
					fitingInterval.append(itFits)
				else:
					print(str(times[i]), "does nots fit in", self._intervals[i])
					return None
			return fitingInterval
		return None

	def _getTimeOffset(self, itFits):
		return 0

	def __str__(self):
		txt = ''
		for bit in self._intervals:
			txt = txt + str(bit) + " "
		txt += str(self._messages)
		return txt
