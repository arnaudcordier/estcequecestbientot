"""
 Return a (title, message) given a datetime object
"""

import yaml
from messageApp.intervals import Interval

class Messages():
	# instanciate with a messageObject like defined in messages_object.yaml
	def __init__(self, messagesFile):
		self.load(messagesFile)
#TODO
#set _title and _default
#use ['messages'] to create _intervals = [Interval]

#TODO no need
	def load(self, messagesFile):
		self.messagesFile = messagesFile
		self._populateObject(self.messagesFile)

#TODO no need
	# initialise from a file and create messages dict from it
	def reload(self):
		self.load(self.messagesFile)

	# return ((string) title, (string) message) given a datetime object
	# _default if no message
	# None on failure
	def getMessage(self, time):
		for interval in self.intervals:
			message = interval.getMessage(time)
			if message:
				return (self.title, message)
		
		if self.defaultMessage:
			return (self.title, self.defaultMessage)
		
		return None

#TODO
	# set _intervals an [ (object) Interval list ]
	def _populateObject(self, messagesFile):
		f = open(messagesFile, 'r')
		variables = yaml.load(f)
		self.title = variables['title']
		self.defaultMessage = variables['default'] if 'default' in variables else ''
		self.intervals = []
		for messages in variables['messages']:
			relative = messages['relative'] if 'relative' in messages else False
			interval = messages['interval'] if 'interval' in messages else '* * * * * *'
			intervals = Interval(interval, messages['messages'].items(), relative)
			self.intervals.append(intervals)

	def __str__(self):
		txt =  "Title   : " + self.title + "\n"
		txt += "Default : " + self.defaultMessage + "\n"
		txt += "Messages:\n"
		for i in self.intervals:
			txt += str(i) + "\n"
		return txt
