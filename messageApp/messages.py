"""
 Return a (title, message) given a datetime object
"""

from messageApp.intervals import Interval

class Messages():
	# instanciate with a messageObject like defined in messages_object.yaml
	def __init__(self, messageObject):
		self._title = messageObject['title']
		self._defaultMessage = messageObject['default'] if 'default' in messageObject else ''
		self._intervals = self._createIntervals(messageObject['messages'])

	# given a datetime object
	# return an estcequecestbientot : ((string) _title, (string) message)
	# (_title, _defaultMessage) if no message at that time
	# None if no _defaultMessage #TODO TEST that
	def getMessage(self, time):
		for interval in self._intervals:
			message = interval.getMessage(time)
			if message:
				return (self._title, message)
		
		if self._defaultMessage:
			return (self._title, self._defaultMessage)
		
		return None

	# given a list…
	# return an [ (object) Interval list ]
	def _createIntervals(self, intervals):
		intervalList = []
		for interval in intervals:
			relative       = interval['relative'] if 'relative' in interval else False
			intervalString = interval['interval'] if 'interval' in interval else '* * * * * *'
			intervalObject = Interval(intervalString, interval['messages'].items(), relative)
			if intervalObject:
				intervalList.append(intervalObject)
		return intervalList

	def __str__(self):
		txt =  "Title   : " + self._title + "\n"
		txt += "Default : " + self._defaultMessage + "\n"
		txt += "Messages:\n"
		for i in self._intervals:
			txt += str(i) + "\n"
		return txt
